"""Write the legal pages, the 404 page and the logo options page from one shared template.

Run from the project root:  python tools/make-pages.py
Edit the page bodies below, then re-run.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://obsidianstudiodesigns.github.io/Plastic-Welding-Fabrication-Specialist/"
NAME = "Plastic Welding &amp; Fabrication Specialist"
UPDATED = "23 October 2026"
WA = "https://wa.me/27734688916?text=Hi%20Lloyd%2C%20I%20found%20your%20website.%20I%27d%20like%20to%20ask%20about%20plastic%20welding%20work."

HEAD = """<!doctype html>
<html lang="en-ZA">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{title} | {name}</title>
  <meta name="description" content="{desc}">
  {canonical}
  <meta name="theme-color" content="#16171a">
  <meta name="color-scheme" content="light dark">
  <link rel="icon" href="favicon.ico" sizes="48x48">
  <link rel="icon" href="favicon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="apple-touch-icon.png">
  <link rel="manifest" href="site.webmanifest">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="{name}">
  <meta property="og:locale" content="en_ZA">
  <meta property="og:title" content="{title} | {name}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="{base}og-image.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,100..900&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@phosphor-icons/web@2.1.1/src/fill/style.css">
  <link rel="stylesheet" href="assets/css/style.css?v=1">
</head>
<body>
  <header class="site-header legal-header is-solid">
    <div class="wrap header-inner">
      <a class="brand" href="./" aria-label="{name}, home">
        <img class="brand-mark" src="brand/mark-light.svg" alt="" width="44" height="44">
        <span class="brand-name"><b>Plastic Welding</b><span>&amp; Fabrication Specialist</span></span>
      </a>
      <a class="btn btn-accent btn-sm" href="{wa}" target="_blank" rel="noopener"><i class="ph-fill ph-whatsapp-logo" aria-hidden="true"></i>WhatsApp Lloyd</a>
    </div>
  </header>
"""

FOOT = """
  <footer class="site-footer" style="padding-top:0">
    <div class="wrap footer-base">
      <p>&copy; <span data-year>2026</span> Plastic Welding &amp; Fabrication Specialist, Lloyd Mthembu.</p>
      <nav class="legal-nav" aria-label="Legal">
        <a href="privacy.html"{cur_privacy}>Privacy policy</a>
        <a href="terms.html"{cur_terms}>Terms of use</a>
      </nav>
      <p class="credit">Website designed by <a href="https://obsidianstudiodesigns.co.za/" target="_blank" rel="noopener">Obsidian Studio Designs</a></p>
    </div>
  </footer>
  <script>document.querySelectorAll('[data-year]').forEach(function (e) {{ e.textContent = new Date().getFullYear(); }});</script>
</body>
</html>
"""

CONTACT = """<dl>
      <dt>Business</dt><dd>Plastic Welding &amp; Fabrication Specialist</dd>
      <dt>Owner</dt><dd>Lloyd Mthembu</dd>
      <dt>Address</dt><dd>104 Gordon Road, Bertrams, Johannesburg, 2094, Gauteng, South Africa</dd>
      <dt>WhatsApp and phone</dt><dd><a href="tel:+27734688916">073 468 8916</a></dd>
      <dt>Email</dt><dd><a href="mailto:mthembullyod@gmail.com">mthembullyod@gmail.com</a></dd>
      <dt>Website</dt><dd><a href="./">obsidianstudiodesigns.github.io/Plastic-Welding-Fabrication-Specialist</a></dd>
    </dl>"""

PAGES = {
    "privacy.html": dict(
        title="Privacy policy",
        desc="How Plastic Welding & Fabrication Specialist (Lloyd Mthembu) collects, uses and protects your personal information under the Protection of Personal Information Act (POPIA).",
        body=f"""
    <p class="lead">This policy explains how Plastic Welding &amp; Fabrication Specialist ("we", "us"), run by Lloyd Mthembu, collects, uses and protects the personal information of clients, employers and people who enquire, in line with the Protection of Personal Information Act 4 of 2013 (POPIA).</p>

    <h2>Who we are</h2>
    {CONTACT}
    <p>Lloyd Mthembu is our Information Officer under POPIA. Contact him on the details above about anything in this policy.</p>

    <h2>What we collect</h2>
    <p>We only collect what we need to answer enquiries, quote and do the work, such as:</p>
    <ul>
      <li>your name, company, cellphone number and email address (WhatsApp shares your number with us when you message us)</li>
      <li>job details: the site location, dates, pipe sizes and materials, drawings, photos and scope you send</li>
      <li>site contact details and access arrangements</li>
      <li>job offers, contracts, timesheets, quotes, invoices and payment records</li>
    </ul>

    <h2>Why we use it</h2>
    <ul>
      <li>to reply to your enquiry or job offer and prepare a quote or rate</li>
      <li>to plan, carry out and complete welding, fabrication and installation work</li>
      <li>to meet site safety, induction and access requirements you or the main contractor set</li>
      <li>to manage payments and keep the records the law requires</li>
    </ul>
    <p>We do not sell, rent or trade personal information, and we will not add you to a marketing list.</p>

    <h2>Who we share it with</h2>
    <p>We only share information when we need to: with the main contractor or site management on a job you are part of, with suppliers where needed for your order, or when the law requires it. WhatsApp (Meta) and Gmail (Google) carry our messages under their own privacy policies.</p>

    <h2>Photos of work</h2>
    <p>We may share photos of welds, fabrications and installations we have done. We focus on the work, not on people, and we do not share photos from sites where the client or contractor has asked us not to. If you would like a photo removed, tell us and we will take it down.</p>

    <h2>This website, cookies and third parties</h2>
    <p>This website has no accounts and no database. It does not set cookies and does not use analytics or advertising trackers. The enquiry form does not send anything to us or store anything: it only opens WhatsApp on your device with your message filled in, and nothing is sent unless you press send in WhatsApp yourself. The WhatsApp, phone, email and map links work the same way.</p>
    <p>To load the website, your browser fetches files from these providers, which may record your IP address and browser details in their standard server logs:</p>
    <ul>
      <li>GitHub Pages, which hosts this website</li>
      <li>Google Fonts, which supplies the typefaces</li>
      <li>jsDelivr, which supplies the icons</li>
    </ul>

    <h2>How long we keep it</h2>
    <p>We keep enquiry and job details for as long as we need them to do the work and answer questions afterwards. Financial records are kept for as long as tax law requires, usually five years, and then deleted.</p>

    <h2>How we protect it</h2>
    <p>We take reasonable steps to keep information safe, including keeping it on password-protected devices and accounts and only sharing it when needed.</p>

    <h2>Your rights</h2>
    <p>Under POPIA you may:</p>
    <ul>
      <li>ask what personal information we hold about you</li>
      <li>ask us to correct or delete it</li>
      <li>object to us using it, or withdraw consent you have given</li>
    </ul>
    <p>Contact us on the details above and we will respond within a reasonable time. If you are unhappy with how we handle your information, you may complain to the Information Regulator of South Africa at <a href="https://inforegulator.org.za" target="_blank" rel="noopener">inforegulator.org.za</a>.</p>

    <h2>Changes to this policy</h2>
    <p>We may update this policy from time to time. The date at the top shows when it last changed.</p>
"""),
    "terms.html": dict(
        title="Terms of use",
        desc="Terms for using the Plastic Welding & Fabrication Specialist website, and general information about quotes, rates and work.",
        body=f"""
    <p class="lead">These terms cover your use of this website and general information about hiring Plastic Welding &amp; Fabrication Specialist. By using the website you agree to them.</p>

    <h2>About us</h2>
    {CONTACT}

    <h2>Information on this website</h2>
    <p>We keep the information on this website as accurate as we can, but it is general information, not a quote or a technical specification. The photographs on this website are illustrations of the type of work described. Please confirm details with us before you rely on them.</p>

    <h2>Quotes, rates and bookings</h2>
    <p>Rates and prices are given per job once we know the scope, location, dates and materials. Work is only booked once it has been confirmed in writing, including WhatsApp or email. Payment terms, travel, accommodation, equipment and consumables are set out in the quote, contract or job offer, and form part of the agreement.</p>

    <h2>Site requirements</h2>
    <p>The client or main contractor is responsible for site access, safe working conditions, permits and inductions, and for supplying approved drawings, specifications and materials unless agreed otherwise in writing.</p>

    <h2>Photos</h2>
    <p>We may share photos of work we have done. See our <a href="privacy.html">privacy policy</a> for how this works and how to opt out.</p>

    <h2>Using this website</h2>
    <p>The text, logo and images on this website belong to Plastic Welding &amp; Fabrication Specialist or are used with permission. Please do not copy or reuse them without written consent.</p>
    <p>Links to WhatsApp, Google Maps and other websites are provided for convenience. We are not responsible for their content or their privacy practices.</p>

    <h2>Liability</h2>
    <p>As far as the law allows, we are not liable for any loss arising from use of this website or reliance on information on it. Nothing in these terms limits your rights under the Consumer Protection Act 68 of 2008.</p>

    <h2>Governing law</h2>
    <p>These terms are governed by the laws of the Republic of South Africa.</p>

    <h2>Changes</h2>
    <p>We may update these terms from time to time. The date at the top shows when they last changed.</p>
"""),
}

for name, page in PAGES.items():
    html = HEAD.format(title=page["title"], desc=page["desc"].replace("&", "&amp;"), base=BASE, wa=WA, name=NAME,
                       canonical=f'<link rel="canonical" href="{BASE}{name}">')
    html += f"""
  <main class="wrap legal" id="main">
    <h1>{page["title"]}</h1>
    <p class="updated">Last updated {UPDATED}</p>
{page["body"]}  </main>
"""
    html += FOOT.format(cur_privacy=' aria-current="page"' if name == "privacy.html" else "",
                        cur_terms=' aria-current="page"' if name == "terms.html" else "")
    (ROOT / name).write_text(html, encoding="utf-8")
    print("wrote", name)


def absolute(html):
    """GitHub Pages serves 404.html from any path, so its links need the full base."""
    for a, b in (('href="./"', f'href="{BASE}"'), ('="favicon', f'="{BASE}favicon'), ('="apple-touch', f'="{BASE}apple-touch'),
                 ('="site.webmanifest', f'="{BASE}site.webmanifest'), ('="assets/', f'="{BASE}assets/'), ('="brand/', f'="{BASE}brand/'),
                 ('href="privacy.html"', f'href="{BASE}privacy.html"'), ('href="terms.html"', f'href="{BASE}terms.html"')):
        html = html.replace(a, b)
    return html


notfound = HEAD.format(title="Page not found", desc="This page could not be found.", base=BASE, wa=WA, name=NAME,
                       canonical='<meta name="robots" content="noindex">')
notfound += """
  <main class="wrap notfound" id="main">
    <h1>404</h1>
    <p>This page isn't on the drawings. Head back to the home page for welding, fabrication and contact details.</p>
    <a class="btn btn-accent" href="./">Back to the home page</a>
  </main>
"""
notfound += FOOT.format(cur_privacy="", cur_terms="")
(ROOT / "404.html").write_text(absolute(notfound), encoding="utf-8")
print("wrote 404.html")

# Logo options page for the client to choose from (not linked from the site, not indexed).
OPTIONS = [
    ("logo-1", "The joint, horizontal", "A butt-fusion joint (two pipe ends and the double weld bead between them) beside the name on two lines. Used in the website header, footer and share image. Best for letterheads, invoices, email signatures and vehicle doors."),
    ("logo-2", "The badge", "The joint inside a ring of type with Lloyd's name below. Works as a round sticker, a hard-hat decal, a stamp on reports, or a WhatsApp and Facebook profile picture."),
    ("logo-3", "The stacked lockup", "The joint over the full name, with an orange bead line and Lloyd's name. Best for overalls, banners, site boards and the front of a company profile."),
]
cards = "".join(f"""
      <article class="option">
        <div class="option-art">
          <img class="on-light" src="brand/{key}.svg" alt="{title} logo option on a light background" loading="lazy">
          <img class="on-dark" src="brand/{key}-light.svg" alt="{title} logo option on a dark background" loading="lazy">
        </div>
        <h2>{n}. {title}</h2>
        <p>{text}</p>
        <p class="files">Files: <a href="brand/{key}.svg" download>SVG</a> <a href="brand/png/{key}.png" download>PNG</a> <a href="brand/{key}-light.svg" download>SVG for dark backgrounds</a> <a href="brand/png/{key}-light.png" download>PNG for dark backgrounds</a></p>
      </article>""" for n, (key, title, text) in enumerate(OPTIONS, 1))
cards += """
      <article class="option">
        <div class="option-art">
          <img class="on-light" src="brand/mark.svg" alt="The joint mark on a light background" loading="lazy">
          <img class="on-dark" src="brand/mark-tile.svg" alt="The joint mark as an app icon" loading="lazy">
        </div>
        <h2>The mark on its own</h2>
        <p>The joint alone, for the favicon, app icon, social avatars and anywhere the name is already written nearby.</p>
        <p class="files">Files: <a href="brand/mark.svg" download>SVG</a> <a href="brand/png/mark.png" download>PNG</a> <a href="brand/png/mark-tile.png" download>App icon PNG</a></p>
      </article>"""
brand = HEAD.format(title="Logo options", desc="Logo options for Plastic Welding and Fabrication Specialist.", base=BASE, wa=WA, name=NAME,
                    canonical='<meta name="robots" content="noindex, nofollow">')
brand = brand.replace("</head>", """  <style>
    .options { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 56px 40px; margin-top: 48px; }
    .option-art { display: grid; grid-template-columns: 1fr 1fr; border-radius: var(--radius); overflow: hidden; }
    .option-art img { width: 100%; aspect-ratio: 1; object-fit: contain; padding: 12%; }
    .option-art .on-light { background: #ecede8; }
    .option-art .on-dark { background: #16171a; }
    .option h2 { font-weight: 800; font-stretch: 116%; font-size: 1.4rem; text-transform: uppercase; margin-top: 22px; }
    .option p { margin-top: 10px; color: var(--ink-soft); max-width: 56ch; }
    .option .files { font-size: 0.92rem; display: flex; flex-wrap: wrap; gap: 6px 16px; }
    .option .files a { color: var(--accent-text); }
    .palette { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 20px; }
    .palette div { width: 150px; border-radius: var(--radius); overflow: hidden; box-shadow: inset 0 0 0 1px var(--line); font-size: 0.86rem; }
    .palette span { display: block; height: 72px; }
    .palette p { padding: 8px 10px; margin: 0; }
    @media (max-width: 860px) { .options { grid-template-columns: 1fr; } }
  </style>
</head>""")
brand += f"""
  <main class="wrap" id="main" style="padding-block:64px 104px">
    <h1 class="h2">Logo options</h1>
    <p class="lede">Three lockups built on one mark: a butt-fusion joint, the two pipe ends and the double-rolled weld bead a good HDPE fusion weld leaves behind. All are vector files, so they stay sharp from a favicon to a site board.</p>
    <div class="palette">
      <div><span style="background:#16171a"></span><p>Graphite #16171a</p></div>
      <div><span style="background:#dd6a2c"></span><p>Fusion orange #dd6a2c</p></div>
      <div><span style="background:#ecede8"></span><p>Bone #ecede8</p></div>
      <div><span style="background:#e7e8e4"></span><p>Concrete #e7e8e4</p></div>
    </div>
    <div class="options">{cards}
    </div>
  </main>
"""
brand += FOOT.format(cur_privacy="", cur_terms="")
(ROOT / "logos.html").write_text(brand, encoding="utf-8")
print("wrote logos.html")
