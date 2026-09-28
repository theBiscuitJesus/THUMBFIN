// Thumb Fin redesign: variant swatches and click-to-load video, shared by the
// sections/thumbfin-*.liquid sections.
(function () {
  if (!customElements.get('thumbfin-spotlight')) {
    // Keeps the submitted variant id, price, sold-out state and image in sync with the
    // chosen swatch. Adding to cart itself is handled by Dawn's <product-form>.
    customElements.define('thumbfin-spotlight', class extends HTMLElement {
      connectedCallback() {
        if (this._bound) return;
        this._bound = true;
        this.addEventListener('change', (event) => {
          if (event.target.matches('[data-tfr-variant-input]')) this.update(event.target);
        });
      }

      update(input) {
        const source = input.tagName === 'SELECT' ? input.selectedOptions[0] : input;
        if (!source) return;
        const data = source.dataset;

        const idInput = this.querySelector('[data-tfr-variant-id]');
        if (idInput) idInput.value = source.value;

        const price = this.querySelector('[data-tfr-price]');
        if (price) price.textContent = data.price;
        const compare = this.querySelector('[data-tfr-compare]');
        if (compare) compare.textContent = data.compare || '';
        const title = this.querySelector('[data-tfr-variant-title]');
        if (title) title.textContent = data.title;

        const button = this.querySelector('[data-tfr-submit]');
        if (button) {
          const available = data.available === 'true';
          button.disabled = !available;
          button.querySelector('[data-tfr-submit-label]').textContent = available
            ? button.dataset.labelAdd
            : button.dataset.labelSoldOut;
        }

        if (data.url) {
          this.querySelectorAll('[data-tfr-product-link]').forEach((link) => { link.href = data.url; });
        }

        const image = this.querySelector('.tfr-spot-img');
        if (image && data.image) {
          image.removeAttribute('srcset');
          image.src = data.image;
        }
      }
    });
  }

  if (!customElements.get('thumbfin-video')) {
    // Click-to-load video: nothing from YouTube/Vimeo loads until the visitor asks for it.
    customElements.define('thumbfin-video', class extends HTMLElement {
      connectedCallback() {
        if (this._bound) return;
        this._bound = true;
        this.querySelectorAll('[data-tfr-play]').forEach((trigger) => {
          trigger.addEventListener('click', (event) => {
            event.preventDefault();
            this.play();
          });
        });
      }

      play() {
        const frame = this.querySelector('[data-tfr-frame]');
        if (!frame || frame.querySelector('iframe')) return;
        const id = encodeURIComponent(this.dataset.videoId);
        const src = this.dataset.videoType === 'vimeo'
          ? `https://player.vimeo.com/video/${id}?autoplay=1`
          : `https://www.youtube-nocookie.com/embed/${id}?autoplay=1&rel=0&playsinline=1`;
        const iframe = document.createElement('iframe');
        iframe.src = src;
        iframe.title = this.querySelector('h2')?.textContent || 'Thumb Fin demo video';
        iframe.allow = 'autoplay; encrypted-media; picture-in-picture; fullscreen';
        iframe.allowFullscreen = true;
        frame.replaceChildren(iframe);
        frame.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
      }
    });
  }
})();

if (!customElements.get('thumbfin-sticky-atc')) {
  // Phone-only Add to cart bar (snippets/thumbfin-sticky-atc.liquid). Shows once the
  // page's real Add to cart button has scrolled above the screen, and forwards clicks to it.
  customElements.define('thumbfin-sticky-atc', class extends HTMLElement {
    connectedCallback() {
      // Move to <body> so no product-info layout rule can clip or reposition the bar;
      // moving reconnects the element, which runs this callback again.
      if (this.parentElement !== document.body) {
        document.body.appendChild(this);
        return;
      }
      if (this._bound) return;
      this._bound = true;
      this.target = document.getElementById(this.dataset.target);
      if (!this.target) return;

      this.button = this.querySelector('[data-sticky-button]');
      this.button.addEventListener('click', () => this.target.click());

      const syncState = () => {
        const disabled = this.target.disabled || this.target.getAttribute('aria-disabled') === 'true';
        this.button.disabled = disabled;
        const label = this.target.querySelector('span');
        this.button.textContent = label ? label.textContent.trim() : 'Add to cart';
        const price = document.querySelector('.product__info-container .price .price-item--last, .product__info-container .price-item--regular');
        if (price) this.querySelector('[data-price]').textContent = price.textContent.trim();
      };
      new MutationObserver(syncState).observe(this.target, { attributes: true, childList: true, subtree: true });
      syncState();

      // Checked on every scroll (throttled to one check per frame) rather than with an
      // IntersectionObserver, which misses fast flicks that jump past the button.
      let queued = false;
      const update = () => {
        queued = false;
        const show = this.target.getBoundingClientRect().bottom < 0;
        if (this.hidden === !show) return;
        this.hidden = !show;
        document.body.classList.toggle('tfr-has-sticky-atc', show);
      };
      const queue = () => {
        if (queued) return;
        queued = true;
        requestAnimationFrame(update);
      };
      window.addEventListener('scroll', queue, { passive: true });
      window.addEventListener('resize', queue, { passive: true });
      update();
    }
  });
}

// Email signup popup (sections/thumbfin-signup-popup.liquid). Opens after a delay or on
// desktop exit intent, once per visitor: closing hides it for `data-days`, signing up hides
// it for good. After the form posts, the page reloads and the popup reopens with the code.
if (!customElements.get('thumbfin-signup')) {
  customElements.define('thumbfin-signup', class extends HTMLElement {
    connectedCallback() {
      this.storeKey = 'tfr-signup';
      this.card = this.querySelector('[role="dialog"]');
      this.querySelectorAll('[data-signup-close]').forEach((el) => el.addEventListener('click', () => this.close(true)));
      this.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') this.close(true);
        if (e.key === 'Tab') this.trapFocus(e);
      });

      const form = this.querySelector('form');
      if (form) form.addEventListener('submit', () => this.store({ sent: Date.now() }));
      const done = this.querySelector('[data-signup-done]');
      if (done) done.addEventListener('click', () => this.store({ subscribed: true }));

      const preview = /[?&]signup-preview\b/.test(location.search);
      const saved = this.read();
      const justSent = location.hash === '#TfrSignup' || (saved.sent && Date.now() - saved.sent < 10 * 60 * 1000);

      if (justSent) {
        // Back from submitting: show the code (or the error), then never show it again once it worked.
        if (this.querySelector('[data-signup-done]')) this.store({ subscribed: true });
        else this.store({});
        this.open();
        return;
      }
      if (window.Shopify && Shopify.designMode) {
        document.addEventListener('shopify:section:select', (e) => { if (e.target.contains(this)) this.open(); });
        document.addEventListener('shopify:section:deselect', (e) => { if (e.target.contains(this)) this.close(false); });
        return;
      }
      if (preview) { this.open(); return; }
      if (this.dataset.enabled !== 'true' || saved.subscribed || (saved.until && Date.now() < saved.until)) return;

      const delay = Math.max(1, parseInt(this.dataset.delay, 10) || 10) * 1000;
      this.timer = setTimeout(() => this.open(), delay);
      if (this.dataset.exitIntent === 'true' && window.matchMedia('(pointer: fine)').matches) {
        const onLeave = (e) => {
          if (e.clientY > 0 || e.relatedTarget) return;
          document.removeEventListener('mouseout', onLeave);
          this.open();
        };
        setTimeout(() => document.addEventListener('mouseout', onLeave), 3000);
        this.removeExit = () => document.removeEventListener('mouseout', onLeave);
      }
    }

    read() {
      try { return JSON.parse(localStorage.getItem(this.storeKey)) || {}; } catch (e) { return {}; }
    }

    store(value) {
      try { localStorage.setItem(this.storeKey, JSON.stringify(value)); } catch (e) { /* storage blocked: popup just shows again next visit */ }
    }

    open() {
      if (this.isOpen) return;
      clearTimeout(this.timer);
      if (this.removeExit) this.removeExit();
      this.isOpen = true;
      this.lastFocus = document.activeElement;
      this.hidden = false;
      document.documentElement.classList.add('tfr-signup-open');
      this.card.focus({ preventScroll: true });
    }

    close(remember) {
      if (!this.isOpen) return;
      this.isOpen = false;
      this.hidden = true;
      document.documentElement.classList.remove('tfr-signup-open');
      if (remember && !this.read().subscribed) {
        const days = parseInt(this.dataset.days, 10) || 14;
        this.store({ until: Date.now() + days * 86400000 });
      }
      if (this.lastFocus && this.lastFocus.focus) this.lastFocus.focus({ preventScroll: true });
    }

    trapFocus(e) {
      const items = [...this.card.querySelectorAll('a[href], button, input:not([type="hidden"])')].filter((el) => !el.disabled && el.offsetParent !== null);
      if (!items.length) return;
      const first = items[0], last = items[items.length - 1];
      if (e.shiftKey && (document.activeElement === first || document.activeElement === this.card)) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    }
  });
}
