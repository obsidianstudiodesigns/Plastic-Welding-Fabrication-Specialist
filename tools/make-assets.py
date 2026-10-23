"""Build the web images for the Plastic Welding & Fabrication Specialist site.

Sources (local only, not committed):
  research/gen/  photoreal images generated for the site (Canva AI): hero, hero-tall, butt, electro,
                 extrusion, socket, manhole, bends, pipeline, tank, portrait (.jpg)

Run from the project root:  python tools/make-assets.py
"""
from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent.parent
GEN = ROOT / "research" / "gen"
OUT = ROOT / "assets" / "img"
OUT.mkdir(parents=True, exist_ok=True)


def gen(name):
    return ImageOps.exif_transpose(Image.open(GEN / f"{name}.jpg")).convert("RGB")


def crop_ratio(img, ratio, fy=0.5, fx=0.5):
    """Crop to width/height = ratio around a focus point (0..1)."""
    w, h = img.size
    if w / h > ratio:
        nw = round(h * ratio)
        left = round((w - nw) * fx)
        return img.crop((left, 0, left + nw, h))
    nh = round(w / ratio)
    top = round((h - nh) * fy)
    return img.crop((0, top, w, top + nh))


def fit(img, width):
    if img.width <= width:
        return img
    return img.resize((width, round(img.height * width / img.width)), Image.LANCZOS)


def out(img, name, width, small=None, q=78):
    fit(img, width).save(OUT / f"{name}.webp", "WEBP", quality=q, method=6)
    if small:
        fit(img, small).save(OUT / f"{name}-sm.webp", "WEBP", quality=q - 4, method=6)


# Hero: dusk butt-fusion weld on a Joburg civils site, wide for desktop and tall for phones.
out(gen("hero"), "hero", 1920, small=1100, q=80)
out(gen("hero-tall"), "hero-tall", 944, small=600, q=78)

# Welding methods, 4:5.
for name in ("butt", "electro", "extrusion", "socket", "tank", "portrait"):
    out(crop_ratio(gen(name), 4 / 5), name, 900, small=520)

# Fabrication, 4:3, and the pipeline band, wide.
out(gen("manhole"), "manhole", 1200, small=640)
out(gen("bends"), "bends", 1200, small=640)
out(gen("pipeline"), "pipeline", 1680, small=900)

print("done:", len(list(OUT.glob("*.webp"))), "images")
