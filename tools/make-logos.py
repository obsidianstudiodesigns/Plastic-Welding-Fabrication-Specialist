"""Draw the Plastic Welding & Fabrication Specialist logo options as pure-vector SVG (text as outlines).

Needs the typefaces in research/fonts/ (Archivo variable and JetBrains Mono from Google Fonts)
and fontTools.  Run from the project root:  python tools/make-logos.py

The mark is a butt-fusion joint seen from the side: two pipe ends meeting at the double-rolled
weld bead that a good HDPE fusion weld leaves behind.

Writes brand/logo-1.svg ... logo-3.svg in graphite and *-light.svg versions for dark backgrounds,
plus brand/mark*.svg (the joint on its own) and favicon.svg.
"""
import math
from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

ROOT = Path(__file__).resolve().parent.parent
FONTS = ROOT / "research" / "fonts"
OUT = ROOT / "brand"
OUT.mkdir(exist_ok=True)

GRAPHITE = "#16171a"
BONE = "#ecede8"
FUSION = "#dd6a2c"
FUSION_ON_DARK = "#ef7a3a"


def ntos(v):
    s = f"{v:.2f}".rstrip("0").rstrip(".")
    return "0" if s in ("-0", "") else s


class Face:
    def __init__(self, name, axes=None):
        f = TTFont(FONTS / name)
        if axes:
            f = instantiateVariableFont(f, axes)
        self.gs = f.getGlyphSet()
        self.cmap = f.getBestCmap()
        self.upm = f["head"].unitsPerEm
        self.hmtx = f["hmtx"]

    def advances(self, text, size, tracking=0.0):
        s = size / self.upm
        names = [self.cmap[ord(c)] for c in text]
        return names, [self.hmtx[g][0] * s + (tracking * size if i < len(names) - 1 else 0)
                       for i, g in enumerate(names)]

    def width(self, text, size, tracking=0.0):
        return sum(self.advances(text, size, tracking)[1])

    def path(self, text, size, x, y, tracking=0.0, anchor="start"):
        w = self.width(text, size, tracking)
        x -= {"start": 0, "middle": w / 2, "end": w}[anchor]
        s = size / self.upm
        pen = SVGPathPen(self.gs, ntos=ntos)
        names, adv = self.advances(text, size, tracking)
        for g, a in zip(names, adv):
            self.gs[g].draw(TransformPen(pen, (s, 0, 0, -s, x, y)))
            x += a
        return pen.getCommands()

    def fit(self, text, width, tracking=0.0):
        """Font size at which text fills width exactly."""
        return width / self.width(text, 100, tracking) * 100

    def arc(self, text, size, cx, cy, r, tracking=0.0, bottom=False):
        """Text set on a circle, centred on the top (reading clockwise) or the bottom."""
        s = size / self.upm
        names, adv = self.advances(text, size, tracking)
        pen = SVGPathPen(self.gs, ntos=ntos)
        pos = -sum(adv) / r / 2
        for g, a in zip(names, adv):
            gw = self.hmtx[g][0] * s
            mid = pos + (gw / 2) / r
            th = mid if not bottom else -mid
            if not bottom:
                px, py = cx + r * math.sin(th), cy - r * math.cos(th)
            else:
                px, py = cx - r * math.sin(th), cy + r * math.cos(th)
            c, sn = math.cos(th), math.sin(th)
            self.gs[g].draw(TransformPen(pen, (c * s, sn * s, sn * s, -c * s, px - c * gw / 2, py - sn * gw / 2)))
            pos += a / r
        return pen.getCommands()


WIDE_BLACK = Face("Archivo.ttf", {"wdth": 125, "wght": 850})
WIDE_SEMI = Face("Archivo.ttf", {"wdth": 125, "wght": 600})
WIDE_MED = Face("Archivo.ttf", {"wdth": 112, "wght": 500})
MONO = Face("JetBrainsMono.ttf", {"wght": 500})


def svg(w, h, body, title):
    title = title.replace("&", "&amp;")
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {ntos(w)} {ntos(h)}" '
            f'width="{ntos(w)}" height="{ntos(h)}" role="img" aria-label="{title}">'
            f"<title>{title}</title>{body}</svg>\n")


def P(d, fill):
    return f'<path fill="{fill}" d="{d}"/>'


def rrect(x, y, w, h, r, fill):
    return f'<rect x="{ntos(x)}" y="{ntos(y)}" width="{ntos(w)}" height="{ntos(h)}" rx="{ntos(r)}" fill="{fill}"/>'


# ---------- the mark: a butt-fusion joint ----------

def joint(cx, cy, size, ink, accent, gap_fill=None, compact=False):
    """Two pipe ends meeting at a double-rolled weld bead, centred on (cx, cy), `size` wide.

    compact=True draws shorter, fatter pipe ends so the mark still reads at favicon size."""
    u = size / 440
    pipe_h = (190 if compact else 132) * u
    roll_w, roll_h = (40 if compact else 30) * u, (270 if compact else 196) * u
    seam = (6 if compact else 3.2) * u
    stripe_h = (14 if compact else 9) * u
    b = ""
    # pipe halves, outer ends square, inner ends tucked under the bead
    b += rrect(cx - 220 * u, cy - pipe_h / 2, 200 * u, pipe_h, 6 * u, ink)
    b += rrect(cx + 20 * u, cy - pipe_h / 2, 200 * u, pipe_h, 6 * u, ink)
    # a pipe stripe, like the colour-coded stripes extruded into HDPE pipe
    if gap_fill:
        for x0 in (cx - 206 * u, cx + 34 * u):
            b += rrect(x0, cy - pipe_h / 2 + pipe_h * 0.18, 172 * u, stripe_h, stripe_h / 2, gap_fill)
    # the two rolls of the weld bead, with the fusion seam between them
    b += rrect(cx - roll_w - seam / 2, cy - roll_h / 2, roll_w, roll_h, roll_w / 2, accent)
    b += rrect(cx + seam / 2, cy - roll_h / 2, roll_w, roll_h, roll_w / 2, accent)
    return b


def mark(ink, accent, stripe, bg=None, radius=0.0):
    W = H = 512
    if not bg:
        return svg(W, H, joint(W / 2, H / 2, 440, ink, accent, stripe, compact=True), "Butt-fusion joint mark")
    # on a tile the pipe runs off both edges, so the joint fills a favicon
    b = f'<clipPath id="t"><rect width="{W}" height="{H}" rx="{ntos(W * radius)}"/></clipPath>'
    b += rrect(0, 0, W, H, W * radius, bg)
    b += f'<g clip-path="url(#t)">{joint(W / 2, H / 2, 600, ink, accent, stripe, compact=True)}</g>'
    return svg(W, H, b, "Butt-fusion joint mark")


# ---------- 1. Horizontal lockup: mark + two-line wordmark ----------

def logo1(ink, accent, stripe):
    H = 220
    b = joint(110, H / 2, 200, ink, accent, stripe)
    x = 252
    line1, line2 = "PLASTIC WELDING", "& FABRICATION SPECIALIST"
    width = 760
    s1 = WIDE_BLACK.fit(line1, width, 0.01)
    s2 = WIDE_SEMI.fit(line2, width, 0.06)
    b += P(WIDE_BLACK.path(line1, s1, x, 108, tracking=0.01), ink)
    b += P(WIDE_SEMI.path(line2, s2, x, 108 + 14 + s2 * 0.74, tracking=0.06), accent)
    W = x + width + 6
    return svg(W, H, b, "Plastic Welding & Fabrication Specialist")


# ---------- 2. The badge: joint inside a ring of type ----------

def logo2(ink, accent, stripe):
    W = H = 600
    cx = cy = 300
    b = f'<circle cx="{cx}" cy="{cy}" r="288" fill="none" stroke="{ink}" stroke-width="10"/>'
    b += f'<circle cx="{cx}" cy="{cy}" r="196" fill="none" stroke="{ink}" stroke-width="3"/>'
    b += P(WIDE_BLACK.arc("PLASTIC WELDING", 40, cx, cy, 226, tracking=0.12), ink)
    b += P(WIDE_SEMI.arc("& FABRICATION SPECIALIST", 25, cx, cy, 252, tracking=0.16, bottom=True), ink)
    for side in (-1, 1):  # bead dots at 3 and 9 o'clock
        b += rrect(cx + side * 242 - 7, cy - 18, 14, 36, 7, accent)
    b += joint(cx, cy - 18, 300, ink, accent, stripe)
    b += P(MONO.path("LLOYD MTHEMBU", 22, cx, cy + 108, tracking=0.12, anchor="middle"), ink)
    return svg(W, H, b, "Plastic Welding & Fabrication Specialist badge")


# ---------- 3. Stacked lockup ----------

def logo3(ink, accent, stripe):
    W = 760
    b = joint(W / 2, 120, 300, ink, accent, stripe)
    width = 700
    l1, l2 = "PLASTIC WELDING", "& FABRICATION"
    s1 = WIDE_BLACK.fit(l1, width, 0.0)
    s2 = WIDE_BLACK.fit(l2, width, 0.0)
    y1 = 262 + s1 * 0.72
    b += P(WIDE_BLACK.path(l1, s1, (W - width) / 2, y1), ink)
    y2 = y1 + 14 + s2 * 0.72
    b += P(WIDE_BLACK.path(l2, s2, (W - width) / 2, y2), ink)
    y3 = y2 + 26
    b += rrect((W - width) / 2, y3, width, 10, 5, accent)
    s3 = WIDE_SEMI.fit("SPECIALIST", width, 0.42)
    b += P(WIDE_SEMI.path("SPECIALIST", s3, (W - width) / 2, y3 + 32 + s3 * 0.72, tracking=0.42), ink)
    y4 = y3 + 32 + s3 * 0.72 + 50
    b += P(MONO.path("LLOYD MTHEMBU  /  HDPE WELDER", 22, W / 2, y4, tracking=0.1, anchor="middle"), ink)
    return svg(W, y4 + 30, b, "Plastic Welding & Fabrication Specialist, Lloyd Mthembu")


for n, fn in enumerate((logo1, logo2, logo3), 1):
    (OUT / f"logo-{n}.svg").write_text(fn(GRAPHITE, FUSION, BONE), encoding="utf-8")
    (OUT / f"logo-{n}-light.svg").write_text(fn(BONE, FUSION_ON_DARK, GRAPHITE), encoding="utf-8")
(OUT / "mark.svg").write_text(mark(GRAPHITE, FUSION, BONE), encoding="utf-8")
(OUT / "mark-light.svg").write_text(mark(BONE, FUSION_ON_DARK, GRAPHITE), encoding="utf-8")
(OUT / "mark-tile.svg").write_text(mark(BONE, FUSION_ON_DARK, GRAPHITE, bg=GRAPHITE), encoding="utf-8")
(ROOT / "favicon.svg").write_text(mark(BONE, FUSION_ON_DARK, GRAPHITE, bg=GRAPHITE, radius=0.2), encoding="utf-8")
print("wrote", sorted(p.name for p in OUT.glob("*.svg")))
