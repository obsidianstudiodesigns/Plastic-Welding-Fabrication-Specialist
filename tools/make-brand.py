"""Render the favicon set, PNG logo exports and og-image.jpg with headless Chrome.

Run after tools/make-logos.py and tools/make-assets.py, from the project root:  python tools/make-brand.py
Needs Google Chrome and Pillow, and internet access for the web fonts in tools/og.html.
"""
import subprocess
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
TMP = ROOT / "research" / "render"
TMP.mkdir(parents=True, exist_ok=True)
(ROOT / "brand" / "png").mkdir(exist_ok=True)


def shoot(html_path, out_png, w, h, transparent=True, budget=4000):
    args = [CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--allow-file-access-from-files",
            f"--window-size={w},{h}", f"--virtual-time-budget={budget}", f"--screenshot={out_png}"]
    if transparent:
        args.append("--default-background-color=00000000")
    subprocess.run(args + [html_path.as_uri()], check=True, capture_output=True)
    return Image.open(out_png).crop((0, 0, w, h))


def render_svg(svg, w, h):
    page = TMP / "svg.html"
    page.write_text(f"""<!doctype html><style>html,body{{margin:0;background:transparent}}
      img{{display:block;width:{w}px;height:{h}px;object-fit:contain}}</style>
      <img src="{svg.as_uri()}">""", encoding="utf-8")
    return shoot(page, TMP / "shot.png", w, h)


# Favicons and app icons from the joint tile.
big = render_svg(ROOT / "brand" / "mark-tile.svg", 1024, 1024)
for size, name in ((512, "icon-512.png"), (192, "icon-192.png"), (180, "apple-touch-icon.png"), (32, "favicon-32.png"), (16, "favicon-16.png")):
    big.resize((size, size), Image.LANCZOS).save(ROOT / name, optimize=True)
rounded = render_svg(ROOT / "favicon.svg", 512, 512)
rounded.save(ROOT / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])

# PNG exports of the logo options and the mark, 2400px on the long side.
for svg in sorted((ROOT / "brand").glob("*.svg")):
    vb = svg.read_text(encoding="utf-8").split('viewBox="')[1].split('"')[0].split()
    vw, vh = float(vb[2]), float(vb[3])
    scale = 2400 / max(vw, vh)
    render_svg(svg, round(vw * scale), round(vh * scale)).save(ROOT / "brand" / "png" / f"{svg.stem}.png", optimize=True)

# Social share image for WhatsApp, Facebook and Google.
og = shoot(ROOT / "tools" / "og.html", TMP / "og.png", 1200, 630, transparent=False, budget=8000)
og.convert("RGB").save(ROOT / "og-image.jpg", quality=86, optimize=True, progressive=True)
print("brand assets done")
