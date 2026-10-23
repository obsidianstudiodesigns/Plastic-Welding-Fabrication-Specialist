# Plastic Welding & Fabrication Specialist

Landing page for Lloyd Mthembu, HDPE and PP plastic welder based in Bertrams, Johannesburg. Butt fusion, electrofusion, extrusion and socket fusion welding; HDPE and PP fabrication (manholes, manifolds, bends, laterals, fittings, tanks and pipelines); pipe installation. Construction, industrial and civils work in South Africa and Zimbabwe. Enquiries on WhatsApp: 073 468 8916.

Live: https://obsidianstudiodesigns.github.io/Plastic-Welding-Fabrication-Specialist/

Logo options for the client: https://obsidianstudiodesigns.github.io/Plastic-Welding-Fabrication-Specialist/logos.html (not linked from the site and not indexed).

## What's on the site

- `index.html`
  - **Hero.** A generated photo of a dusk butt-fusion weld on a Joburg civils site, with the city skyline behind. The photo settles in, and an orange weld bead line "fuses" out from the centre under the headline. Phones get a tall version of the same scene.
  - **The pipe.** A full-width black HDPE pipe band with a blue stripe. The services scroll along it like the inkjet print line on real pipe, with orange weld beads at the joints.
  - **Welding methods.** Butt fusion, electrofusion, extrusion and socket fusion. On desktop the photo beside the list follows the method you point at; on phones each method opens with its own photo.
  - **Fabrication.** Manholes and manifolds, bends, laterals and fittings, and tanks and pipeline fabrication, plus a materials strip (HDPE and PP).
  - **Installation** band, **About Lloyd** (available for job opportunities, contracts, shutdowns and project work), **Questions**, and **Contact**: a form that writes the job enquiry into a WhatsApp message. Nothing is sent to or stored on the website.
  - On phones a WhatsApp button docks at the bottom between the hero and the contact section.
- Light and dark mode follow the visitor's device.
- `privacy.html` (POPIA), `terms.html`, `404.html`, `logos.html`.
- SEO and sharing: canonical URL, Open Graph and Twitter tags with `og-image.jpg` (1200 x 630) for WhatsApp and Facebook previews, LocalBusiness, WebSite and FAQPage JSON-LD, `sitemap.xml`, `robots.txt`, favicon set (SVG, ICO, PNG, Apple touch icon) and web manifest.

## Brand

One mark: a butt-fusion joint seen from the side (two pipe ends and the double-rolled weld bead between them). Three lockups, all true vector outlines, in `brand/`:

1. `logo-1` **The joint, horizontal.** Mark beside "Plastic Welding / & Fabrication Specialist". Used in the header, footer and share image.
2. `logo-2` **The badge.** The joint inside a ring of type, with Lloyd's name.
3. `logo-3` **The stacked lockup.** The joint over the full name, an orange bead line and "Lloyd Mthembu / HDPE welder".

`mark*.svg` is the joint on its own (the favicon and app icon use `mark-tile.svg`). Each logo has a `-light` version for dark backgrounds, and 2400px PNGs are in `brand/png/`.

Colours: graphite `#16171a`, fusion orange `#dd6a2c` (`#ef7a3a` on dark), bone `#ecede8`, concrete `#e7e8e4`. Type: Archivo (wide and heavy for headings) and JetBrains Mono (the pipe print line only), from Google Fonts.

## Content sources

- The client's own flyer text: skills and services list, availability (job opportunities, contracts, shutdowns and project work in Zimbabwe and South Africa) and the line "Skilled hands. Quality welding. Reliable work."
- Contact details from the client: 104 Gordon Road, Bertrams, Johannesburg 2094; 073 468 8916; mthembullyod@gmail.com.
- All photos are generated (Canva AI), not Lloyd's work: hero (wide and tall), butt fusion bead, electrofusion, extrusion, socket fusion, manholes, bends and fittings, PP tank, pipeline and the welder portrait.

## To confirm with Lloyd before promoting the site

- **Logo choice.** Option 1 is on the site. Swapping is a file change: the header uses `brand/mark-light.svg`, the footer `brand/logo-1-light.svg`.
- **Email spelling.** The site shows `mthembullyod@gmail.com` exactly as supplied. Check it is not `mthembulloyd@gmail.com`.
- **Photos are generated**, including the portrait in "About Lloyd", which is not Lloyd. Swap in real photos of his welds, fabrications and of him on site as soon as he has them (`research/gen/`, then `python tools/make-assets.py`).
- **Address.** The full street address is shown, in the footer, contact section and structured data. Remove it if he works from site to site and would rather not publish it.
- **Equipment.** The copy does not say whether Lloyd supplies his own fusion machines or works on the contractor's equipment. Add it if he has his own kit.
- **Tickets and experience.** Add welding certificates, years of experience and past projects or employers if he wants them shown.
- **Domain.** The site runs on GitHub Pages. If a domain is bought, add a `CNAME` file and update `BASE` in `tools/make-pages.py`, the canonical and Open Graph URLs in `index.html`, `robots.txt` and `sitemap.xml`.

## Tools

- `tools/make-logos.py`: draws the logos, the mark and the favicon SVG (needs fontTools and the fonts in `research/fonts/`)
- `tools/make-assets.py`: builds the web images from `research/gen/` (local only)
- `tools/make-brand.py`: renders the favicons, PNG logos and `og-image.jpg` with headless Chrome (uses `tools/og.html`)
- `tools/make-pages.py`: writes the legal pages, 404 and logo options page from one template

## Local preview

```bash
python -m http.server 5203
```

## Deploying

GitHub Pages serves the `main` branch root. Commit and push to `main`.

Website designed by [Obsidian Studio Designs](https://obsidianstudiodesigns.co.za/).
