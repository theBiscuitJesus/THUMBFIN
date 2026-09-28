"""Builds the Thumb Fin campaign emails in the site's design.

Email clients ignore most CSS, so everything is table-based with inline styles;
Oswald is loaded where supported (Apple Mail, iOS) and falls back to a condensed
system font elsewhere. Run: python3 emails/build.py
"""
import html, pathlib

IMG = "https://thumbfin.com/cdn/shop/files/"
LOGO = IMG + "ThumbFin-logo_dfe5b37d-9553-4fcf-aea2-d18fcc1e93eb.png?width=240"
HERO = IMG + "IMG_0004.jpg?width=1200"
COMBO_IMG = IMG + "BJO02840.jpg?width=1200&height=560&crop=center"
VERSIONS = [
    ("Original", "The first Thumb Fin shape, and our tallest profile.", IMG + "IMG_8472.jpg?width=300"),
    ("Low Profile", "Sits 4mm lower than the Original, for a slimmer feel.", IMG + "IMG_3373.jpg?width=300"),
    ("Contoured Low Profile", "4mm lower, with more concave sides that cradle your thumb.",
     IMG + "IMG_3371_0425e0db-2728-4a1b-8af0-f3c4b63549f9.jpg?width=300"),
]
# Site palette (assets/thumbfin.css)
BG, PANEL, PANEL2 = "#241408", "#2f1c0e", "#1a0e05"
CREAM, MUTED, BRASS, BRASS_DIM, NEON, ON_NEON, HEADER = "#f4ecdd", "#c2ab8c", "#cf9d3e", "#8a6a2b", "#c3ff5c", "#1a2400", "#ffd59a"
HEAD = "'Oswald','Arial Narrow','Helvetica Neue',Arial,sans-serif"
BODY = "'Work Sans','Helvetica Neue',Arial,sans-serif"
ENDS = "Tuesday, September 29 at 2:52 PM ET"


def button(label, url, ghost=False):
    bg, fg, border = ("transparent", CREAM, BRASS_DIM) if ghost else (NEON, ON_NEON, NEON)
    return f"""<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="margin:0 auto;"><tr>
  <td align="center" bgcolor="{'' if ghost else NEON}" style="border-radius:3px;border:1px solid {border};background:{bg};">
    <a href="{url}" target="_blank" style="display:inline-block;padding:15px 30px;font-family:{BODY};font-size:16px;font-weight:600;line-height:1.2;color:{fg};text-decoration:none;border-radius:3px;">{html.escape(label)}</a>
  </td></tr></table>"""


def version_rows():
    rows = []
    for name, desc, img in VERSIONS:
        rows.append(f"""<tr><td style="padding:0 0 14px 0;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{PANEL}" style="background:{PANEL};border:1px solid #3d2a1a;border-radius:6px;">
    <tr>
      <td width="110" valign="top" style="padding:14px 0 14px 14px;"><img src="{img}" width="96" height="96" alt="Thumb Fin {html.escape(name)} on a bass" style="display:block;width:96px;height:96px;object-fit:cover;border-radius:4px;border:0;"></td>
      <td valign="middle" style="padding:14px 16px 14px 14px;">
        <div style="font-family:{HEAD};font-size:19px;font-weight:600;color:{CREAM};line-height:1.2;">{html.escape(name)} <span style="color:{BRASS};font-size:16px;">&middot; $20</span></div>
        <div style="font-family:{BODY};font-size:14px;color:{MUTED};line-height:1.5;padding-top:4px;">{html.escape(desc)}</div>
      </td>
    </tr>
  </table>
</td></tr>""")
    return "\n".join(rows)


def code_box(code, note=None):
    note = note or f"Applied automatically from the buttons in this email. Ends {ENDS}."
    return f"""<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border:1px dashed {BRASS};border-radius:6px;">
  <tr><td align="center" style="padding:16px 18px;">
    <div style="font-family:{BODY};font-size:13px;color:{MUTED};letter-spacing:.04em;text-transform:uppercase;">Your code</div>
    <div style="font-family:{HEAD};font-size:28px;font-weight:700;color:{NEON};letter-spacing:.06em;padding:4px 0;">{code}</div>
    <div style="font-family:{BODY};font-size:13px;color:{MUTED};line-height:1.5;">{note}</div>
  </td></tr>
</table>"""


def page(title, preheader, blocks):
    return f"""<!doctype html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="dark"><meta name="supported-color-schemes" content="dark">
<title>{html.escape(title)}</title>
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@600;700&family=Work+Sans:wght@400;600&display=swap" rel="stylesheet">
<style>
  body {{ margin:0; padding:0; background:{BG}; }}
  a {{ color:{NEON}; }}
  @media (max-width:620px) {{ .px {{ padding-left:20px !important; padding-right:20px !important; }} .h1 {{ font-size:32px !important; }} }}
</style>
</head>
<body style="margin:0;padding:0;background:{BG};">
<div style="display:none;max-height:0;overflow:hidden;opacity:0;color:{BG};">{html.escape(preheader)}&#8199;&#65279;&#847;&#8199;&#65279;&#847;&#8199;&#65279;&#847;</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{BG}" style="background:{BG};">
<tr><td align="center" style="padding:0;">
<table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0" style="width:100%;max-width:600px;">
  <!-- Header: same cream-gold band as the site header -->
  <tr><td align="center" bgcolor="{HEADER}" style="background:{HEADER};padding:18px 0;">
    <a href="https://thumbfin.com" target="_blank"><img src="{LOGO}" width="90" alt="Thumb Fin" style="display:block;width:90px;height:auto;border:0;"></a>
  </td></tr>
{blocks}
  <!-- Footer. {{ unsubscribe_link }} is required by Shopify Email for custom HTML; it renders a complete link, so it stands on its own. -->
  <tr><td align="center" class="px" style="padding:28px 40px 36px;border-top:1px solid #3d2a1a;">
    <div style="font-family:{HEAD};font-size:16px;font-weight:600;color:{CREAM};letter-spacing:.04em;">THUMB <span style="color:{BRASS};">FIN</span></div>
    <div style="font-family:{BODY};font-size:13px;color:{MUTED};line-height:1.6;padding-top:6px;">The patented suction-cup thumb rest. No drilling, no screws, no adhesive.<br><a href="https://thumbfin.com" style="color:{MUTED};">thumbfin.com</a></div>
    <div style="font-family:{BODY};font-size:12px;color:{MUTED};line-height:1.6;padding-top:14px;">You're receiving this because you subscribed to emails from Thumb Fin.<br>{{{{ unsubscribe_link }}}}</div>
  </td></tr>
</table>
</td></tr>
</table>
{{{{ open_tracking_block }}}}
</body>
</html>
"""


def text(s, size=16, color=MUTED, pad="0 0 18px"):
    return f'<div style="font-family:{BODY};font-size:{size}px;line-height:1.6;color:{color};padding:{pad};">{s}</div>'


def section(inner, pad="0 40px 28px"):
    return f'  <tr><td class="px" style="padding:{pad};">{inner}</td></tr>'


def hero_block(badge, heading):
    return (f'  <tr><td style="padding:0;"><img src="{HERO}" width="600" alt="Thumb Fin thumb rests on a bass" style="display:block;width:100%;max-width:600px;height:auto;border:0;"></td></tr>\n'
            + section(f"""<div style="padding-top:30px;"><span style="display:inline-block;border:1px solid {BRASS_DIM};border-radius:999px;padding:6px 12px;font-family:{BODY};font-size:13px;color:{BRASS};">&#9733; <b style="color:{CREAM};">4.84</b> from 145 reviews &middot; Patented design</span></div>
<h1 class="h1" style="margin:18px 0 0;font-family:{HEAD};font-size:38px;line-height:1.1;font-weight:700;color:{CREAM};">{heading}</h1>""", "0 40px 18px"))


def combo_block(price_line, url, label):
    return section(f"""<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{PANEL2}" style="background:{PANEL2};border:1px solid {BRASS};border-radius:6px;">
  <tr><td style="padding:0;"><img src="{COMBO_IMG}" width="518" alt="Thumb Fin Combo 3 Pack" style="display:block;width:100%;height:auto;border:0;border-radius:6px 6px 0 0;"></td></tr>
  <tr><td style="padding:22px 24px 24px;">
    <span style="display:inline-block;background:{NEON};color:{ON_NEON};font-family:{BODY};font-size:12px;font-weight:600;padding:4px 10px;border-radius:999px;">Save $10</span>
    <div style="font-family:{HEAD};font-size:22px;font-weight:600;color:{CREAM};padding:12px 0 6px;">Can't decide? Get all three.</div>
    {text(price_line, 15, MUTED, "0 0 18px")}
    {button(label, url)}
  </td></tr>
</table>""")


def email_non_buyers():
    code, shop = "NEWSITE10", "https://thumbfin.com/discount/NEWSITE10?redirect=/#thumbfin-shop"
    blocks = "\n".join([
        hero_block(True, "10% off the no-drill bass thumb rest"),
        section(text("Hi {{ customer.first_name | default: 'there' }},", 16, CREAM, "0 0 12px")
                + text("Thanks for signing up with Thumb Fin. We just rebuilt our site, and to celebrate, <b style=\"color:#f4ecdd;\">you get 10% off for the next 48 hours.</b>")
                + text("Thumb Fin is a patented suction-cup thumb rest. It gives your thumb a relaxed, natural place to rest without drilling, screws or adhesive. Press it on, move it anytime, and take it off without a mark.", pad="0 0 24px")
                + button("Get 10% off", shop)),
        section(f'<div style="font-family:{HEAD};font-size:26px;font-weight:600;color:{CREAM};padding:8px 0 16px;">Pick your shape</div>'
                + f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{version_rows()}</table>'
                + text("Each one is $20, in six colors.", 14, MUTED, "4px 0 0")),
        combo_block("One of each version for $50 (only $45 with your code). Find your favorite before committing to one.",
                    "https://thumbfin.com/discount/NEWSITE10?redirect=/products/combo-3-pack-one-of-each-version", "Get the Combo 3 Pack"),
        section(code_box(code)),
        section(text("Playing a matte or satin bass? Add our $2 <a href=\"https://thumbfin.com/discount/NEWSITE10?redirect=/products/contact-paper-for-matte-finish\" style=\"color:#c3ff5c;\">contact paper</a> so the suction cup has a surface to grip.", 14)
                + text("Thanks for playing,<br><b style=\"color:#f4ecdd;\">Thumb Fin</b>", 15, MUTED, "0")),
    ])
    return page("10% off the no-drill bass thumb rest", "Our new site is live, with three shapes and six colors. 10% off for 48 hours.", blocks)


def email_past_buyers():
    code, shop = "THANKYOU10", "https://thumbfin.com/discount/THANKYOU10?redirect=/#thumbfin-shop"
    combo = "https://thumbfin.com/discount/THANKYOU10?redirect=/products/combo-3-pack-one-of-each-version"
    blocks = "\n".join([
        hero_block(True, "A thank-you: 10% off your next Thumb Fin"),
        section(text("Hi {{ customer.first_name | default: 'there' }},", 16, CREAM, "0 0 12px")
                + text("Thanks for playing with Thumb Fin. Since you ordered, we've added new shapes and rebuilt our site, and as a thank-you <b style=\"color:#f4ecdd;\">you get 10% off for the next 48 hours.</b>")
                + text("Every Thumb Fin is suction-mounted, so you can keep one on each bass and move them between instruments anytime.", pad="0 0 24px")
                + button("Shop with 10% off", shop)),
        section(f'<div style="font-family:{HEAD};font-size:26px;font-weight:600;color:{CREAM};padding:8px 0 16px;">Found your favorite shape yet?</div>'
                + f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{version_rows()}</table>'),
        combo_block("One of each version: $50, or only $45 with your code. That's $15 less than buying three separately.", combo, "Get the Combo 3 Pack"),
        section(code_box(code)),
        section(text("Thanks again,<br><b style=\"color:#f4ecdd;\">Thumb Fin</b>", 15, MUTED, "0")),
    ])
    return page("A thank-you: 10% off your next Thumb Fin", "Two more shapes you may not have tried. 10% off for 48 hours.", blocks)


def email_welcome():
    code, shop = "WELCOME10", "https://thumbfin.com/discount/WELCOME10?redirect=/#thumbfin-shop"
    combo = "https://thumbfin.com/discount/WELCOME10?redirect=/products/combo-3-pack-one-of-each-version"
    blocks = "\n".join([
        hero_block(True, "Welcome. Here's 10% off your first order."),
        section(text("Hi {{ customer.first_name | default: 'there' }},", 16, CREAM, "0 0 12px")
                + text("Thanks for joining the Thumb Fin list. As promised, <b style=\"color:#f4ecdd;\">here's 10% off your first order.</b>")
                + text("Thumb Fin is a patented suction-cup thumb rest. It gives your thumb a relaxed, natural place to rest without drilling, screws or adhesive. Press it on, move it anytime, and take it off without a mark.", pad="0 0 24px")
                + button("Get 10% off", shop)),
        section(code_box(code, "Applied automatically from the buttons in this email, or enter it at checkout. One use per customer.")),
        section(f'<div style="font-family:{HEAD};font-size:26px;font-weight:600;color:{CREAM};padding:8px 0 16px;">Pick your shape</div>'
                + f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{version_rows()}</table>'
                + text("Each one is $20, in six colors.", 14, MUTED, "4px 0 0")),
        combo_block("One of each version for $50 (only $45 with your code). Find your favorite before committing to one.", combo, "Get the Combo 3 Pack"),
        section(text("Playing a matte or satin bass? Add our $2 <a href=\"https://thumbfin.com/discount/WELCOME10?redirect=/products/contact-paper-for-matte-finish\" style=\"color:#c3ff5c;\">contact paper</a> so the suction cup has a surface to grip.", 14)
                + text("Thanks for playing,<br><b style=\"color:#f4ecdd;\">Thumb Fin</b>", 15, MUTED, "0")),
    ])
    return page("Welcome to Thumb Fin: 10% off your first order", "Your 10% code is inside, plus how to pick your shape.", blocks)


import re


def escape_urls(doc):
    """Write & as &amp; inside src/href attributes, as HTML requires."""
    return re.sub(r'((?:src|href)=")([^"]*)(")',
                  lambda m: m.group(1) + re.sub(r'&(?!amp;)', '&amp;', m.group(2)) + m.group(3), doc)


out = pathlib.Path(__file__).parent
(out / "email-1-non-buyers.html").write_text(escape_urls(email_non_buyers()))
(out / "email-2-past-buyers.html").write_text(escape_urls(email_past_buyers()))
(out / "email-3-welcome.html").write_text(escape_urls(email_welcome()))
print("built", sorted(p.name for p in out.glob("*.html")))
