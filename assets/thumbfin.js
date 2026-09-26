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
  // Phone-only Add to cart bar (snippets/thumbfin-sticky-atc.liquid). Shows while the
  // page's real Add to cart button is off screen and forwards clicks to it.
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
      if (!this.target || !('IntersectionObserver' in window)) return;

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

      new IntersectionObserver(([entry]) => {
        const show = !entry.isIntersecting && entry.boundingClientRect.top < 0;
        this.hidden = !show;
        document.body.classList.toggle('tfr-has-sticky-atc', show);
      }).observe(this.target);
    }
  });
}
