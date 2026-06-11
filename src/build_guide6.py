# -*- coding: utf-8 -*-
import os
from PIL import Image, ImageDraw, ImageFont, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
from fpdf import FPDF
import guide6_content as G

BASE = r"C:/Users/Athanase-Chrisbert J/Downloads/PDFs"
FONTS = r"C:/Users/Athanase-Chrisbert J/_fonts"
DM_B = os.path.join(FONTS, "DMSans-Bold.ttf")
DM_R = os.path.join(FONTS, "DMSans-Regular.ttf")
COVER_SRC = os.path.join(BASE, "_cover", "eq_cover_src.jpg")
COVER_OUT = os.path.join(BASE, "_cover", "eq_cover.png")
OUT_PDF = os.path.join(BASE, "_final", "The-Grounded-Mama_EQ-Toolkit.pdf")

ACCENT = (122, 106, 144)      # lavender
CHARCOAL = (61, 53, 50)
CREAM = (246, 242, 236)
CALLOUT_BG = (236, 231, 240)  # light lavender

# ---------------------------------------------------------------- COVER (PIL)
def build_cover():
    W, H = 1240, 1754
    img = Image.open(COVER_SRC).convert("RGB").resize((W, H))
    # gradient scrims for legibility
    ov = Image.new("L", (W, H), 0)
    px = ov.load()
    for y in range(H):
        a_top = max(0, int(150 * (1 - y / (H * 0.34)))) if y < H * 0.34 else 0
        a_bot = max(0, int(185 * ((y - H * 0.58) / (H * 0.42)))) if y > H * 0.58 else 0
        a = max(a_top, a_bot)
        for x in range(W):
            px[x, y] = a
    black = Image.new("RGB", (W, H), (20, 16, 24))
    img = Image.composite(black, img, ov)
    d = ImageDraw.Draw(img)
    fb = lambda s: ImageFont.truetype(DM_B, s)

    def ctext(y, text, size, fill=(255, 255, 255), ls=0):
        f = fb(size)
        if ls:
            # letter-spaced
            total = sum(d.textlength(c, font=f) + ls for c in text) - ls
            x = (W - total) / 2
            for c in text:
                d.text((x, y), c, font=f, fill=fill)
                x += d.textlength(c, font=f) + ls
        else:
            w = d.textlength(text, font=f)
            d.text(((W - w) / 2, y), text, font=f, fill=fill)

    # Title (top)
    ctext(96,  '“MY CHILD HAS BIG', 78)
    ctext(188, 'EMOTIONAL OUTBURSTS”', 78)
    # lavender accent rule
    d.rectangle([W/2-70, 300, W/2+70, 307], fill=ACCENT)
    # Subtitle (lower)
    ctext(1470, "THE COMPLETE EMOTIONAL", 50)
    ctext(1532, "INTELLIGENCE TOOLKIT", 50)
    # Byline
    ctext(1628, "By The Grounded Mama", 40, fill=(238, 232, 240))
    img.save(COVER_OUT)
    return COVER_OUT

# ---------------------------------------------------------------- PDF
class Book(FPDF):
    def header(self):
        if self.page_no() == 1:
            return
        self.set_fill_color(*CREAM)
        self.rect(0, 0, self.w, self.h, "F")
    def footer(self):
        if self.page_no() == 1:
            return
        self.set_y(-32)
        self.set_font("DM", "", 8)
        self.set_text_color(150, 142, 150)
        self.cell(0, 10, "The Grounded Mama", align="C")

WHEEL_OUT = os.path.join(BASE, "_cover", "feelings_wheel.png")
WHEEL_EMOTIONS = [
    ("ANGRY", (201,131,122)), ("FRUSTRATED", (198,123,92)), ("SAD", (90,122,138)),
    ("SCARED", (74,122,122)), ("WORRIED", (122,106,144)), ("JEALOUS", (90,122,90)),
    ("EMBARRASSED", (180,140,150)), ("DISAPPOINTED", (140,120,150)), ("OVERWHELMED", (110,100,140)),
    ("EXCITED", (212,184,150)), ("SHY", (150,160,180)), ("LONELY", (120,135,150)),
]
def build_wheel():
    import math
    S = 1100; img = Image.new("RGB", (S, S), (255, 255, 255)); d = ImageDraw.Draw(img)
    cx = cy = S / 2; R = S / 2 - 30
    fb = lambda s: ImageFont.truetype(DM_B, s)
    n = len(WHEEL_EMOTIONS)
    for i, (name, col) in enumerate(WHEEL_EMOTIONS):
        a0 = -90 + i * (360 / n); a1 = a0 + 360 / n
        d.pieslice([cx-R, cy-R, cx+R, cy+R], a0, a1, fill=col, outline=(255,255,255), width=6)
    # center hub
    r2 = R * 0.34
    d.ellipse([cx-r2, cy-r2, cx+r2, cy+r2], fill=(255,255,255), outline=(122,106,144), width=6)
    f = fb(40)
    for j, line in enumerate(["HOW DO", "I FEEL?"]):
        w = d.textlength(line, font=f); d.text((cx-w/2, cy-44+j*46), line, font=f, fill=(122,106,144))
    # labels
    for i, (name, col) in enumerate(WHEEL_EMOTIONS):
        mid = math.radians(-90 + (i + 0.5) * (360 / n))
        lr = R * 0.66
        x = cx + lr * math.cos(mid); y = cy + lr * math.sin(mid)
        fs = 30 if len(name) <= 9 else 24
        f = fb(fs); w = d.textlength(name, font=f)
        d.text((x - w/2, y - fs/2), name, font=f, fill=(255,255,255))
    img.save(WHEEL_OUT); return WHEEL_OUT

def main():
    build_cover()
    doc = Book(orientation="P", unit="pt", format="A4")  # 595 x 842
    doc.add_font("DM", "", DM_R); doc.add_font("DM", "B", DM_B)
    doc.set_auto_page_break(True, margin=58)
    ML = 64; doc.set_margins(ML, 64, ML)
    CW = doc.w - 2 * ML

    # ---- COVER PAGE ----
    doc.is_cover = True
    doc.add_page()
    doc.image(COVER_OUT, 0, 0, doc.w, doc.h)
    doc.is_cover = False

    def heading(txt):
        doc.add_page()
        doc.set_font("DM", "B", 15); doc.set_text_color(*ACCENT)
        doc.multi_cell(CW, 21, txt.upper(), align="C")
        doc.ln(10)
    def subhead(txt):
        doc.ln(4); doc.set_font("DM", "B", 12); doc.set_text_color(*CHARCOAL)
        doc.multi_cell(CW, 17, txt); doc.ln(3)
    def body(txt, bold=False):
        doc.set_font("DM", "B" if bold else "", 11); doc.set_text_color(*CHARCOAL)
        doc.multi_cell(CW, 16.5, txt, align="J"); doc.ln(4)
    def bullets(items):
        doc.set_font("DM", "", 11); doc.set_text_color(*CHARCOAL)
        for it in items:
            x = doc.get_x()
            doc.set_text_color(*ACCENT); doc.set_font("DM", "B", 11)
            doc.cell(14, 16, "•")
            doc.set_text_color(*CHARCOAL); doc.set_font("DM", "", 11)
            doc.multi_cell(CW - 14, 16, it)
            doc.set_x(x)
        doc.ln(4)
    def callout(txt):
        doc.ln(2)
        pad = 12
        doc.set_font("DM", "B", 11)
        h = doc.multi_cell(CW - 2 * pad, 16.5, txt, dry_run=True, output="HEIGHT")
        if doc.get_y() + h + 2 * pad > doc.h - 58:
            doc.add_page()
        y = doc.get_y()
        doc.set_fill_color(*CALLOUT_BG); doc.set_draw_color(*ACCENT)
        doc.rect(ML, y, CW, h + 2 * pad, "F")
        doc.rect(ML, y, 4, h + 2 * pad, "F")  # accent bar (uses fill=lavender? set below)
        doc.set_fill_color(*ACCENT); doc.rect(ML, y, 4, h + 2 * pad, "F")
        doc.set_xy(ML + pad, y + pad)
        doc.set_text_color(80, 68, 92)
        doc.multi_cell(CW - 2 * pad, 16.5, txt)
        doc.set_y(y + h + 2 * pad); doc.ln(8)
    def feeling(name, looks, needs, say):
        if doc.get_y() > doc.h - 150:
            doc.add_page()
        doc.set_font("DM", "B", 12); doc.set_text_color(*ACCENT)
        doc.multi_cell(CW, 17, name); doc.ln(1)
        for label, val in [("Looks like: ", looks), ("Needs: ", needs)]:
            doc.set_font("DM", "B", 10.5); doc.set_text_color(*CHARCOAL)
            doc.write(15, label)
            doc.set_font("DM", "", 10.5); doc.write(15, val); doc.ln(15)
        doc.set_font("DM", "B", 10.5); doc.set_text_color(*ACCENT); doc.write(15, "Say: ")
        doc.set_font("DM", "", 10.5); doc.set_text_color(90, 80, 100)
        doc.multi_cell(CW, 15, say); doc.ln(7)
    def script(say, do, follow):
        for label, val in [("Say this: ", say), ("Then do this: ", do), ("Follow up with: ", follow)]:
            doc.set_font("DM", "B", 11); doc.set_text_color(*ACCENT)
            doc.multi_cell(CW, 16, label)
            doc.set_font("DM", "", 11); doc.set_text_color(*CHARCOAL)
            doc.multi_cell(CW, 16, val); doc.ln(2)
        doc.ln(4)

    # ---- TABLE OF CONTENTS ----
    doc.add_page()
    doc.set_font("DM", "B", 18); doc.set_text_color(*ACCENT)
    doc.multi_cell(CW, 24, "WHAT'S INSIDE", align="C"); doc.ln(14)
    doc.set_font("DM", "", 12); doc.set_text_color(*CHARCOAL)
    for item in G.TOC:
        doc.set_font("DM", "B", 11); doc.set_text_color(*ACCENT); doc.cell(16, 20, "•")
        doc.set_font("DM", "", 11.5); doc.set_text_color(*CHARCOAL)
        doc.multi_cell(CW - 16, 20, item); doc.ln(2)

    # ---- CHAPTERS ----
    for title, blocks in G.CHAPTERS:
        heading(title)
        for b in blocks:
            t = b[0]
            if t == "h2": subhead(b[1])
            elif t == "p": body(b[1])
            elif t == "ul": bullets(b[1])
            elif t == "callout": callout(b[1])
            elif t == "script": script(*b[1])
            elif t == "feeling": feeling(*b[1])

    # ---- PRINTABLE 1: FEELINGS WHEEL ----
    build_wheel()
    doc.add_page()
    doc.set_font("DM", "B", 15); doc.set_text_color(*ACCENT)
    doc.multi_cell(CW, 21, "THE FEELINGS WHEEL", align="C"); doc.ln(6)
    doc.set_font("DM", "", 10.5); doc.set_text_color(*CHARCOAL)
    doc.multi_cell(CW, 15, "Print this page and keep it in the calm-down corner. When a feeling "
                   "is too big for words, your child can point to it. Naming it is the first step "
                   "to taming it.", align="C"); doc.ln(8)
    wsize = 360; doc.image(WHEEL_OUT, (doc.w - wsize) / 2, doc.get_y(), wsize, wsize)

    # ---- PRINTABLE 2: 30-DAY EQ TRACKER ----
    doc.add_page()
    doc.set_font("DM", "B", 15); doc.set_text_color(*ACCENT)
    doc.multi_cell(CW, 21, "30-DAY EQ TRACKER", align="C"); doc.ln(5)
    doc.set_font("DM", "", 10); doc.set_text_color(*CHARCOAL)
    doc.multi_cell(CW, 14, "Tick what you practised each day. Not for perfection — for showing up. "
                   "The four squares are: 1) Named a feeling  2) Used the calm corner  "
                   "3) 10 min of connection time  4) Repaired after a rupture.", align="C")
    doc.ln(10)
    cols, rows = 5, 6
    gap = 10; cellw = (CW - gap * (cols - 1)) / cols; cellh = 64
    y0 = doc.get_y()
    for r in range(rows):
        for c in range(cols):
            day = r * cols + c + 1
            x = ML + c * (cellw + gap); y = y0 + r * (cellh + gap)
            doc.set_draw_color(*ACCENT); doc.set_line_width(0.6)
            doc.rect(x, y, cellw, cellh)
            doc.set_xy(x, y + 5); doc.set_font("DM", "B", 9); doc.set_text_color(*ACCENT)
            doc.cell(cellw, 12, f"Day {day}", align="C")
            # 4 checkboxes (2x2)
            bs = 11; bx0 = x + cellw/2 - bs - 6; by0 = y + 24
            for bi in range(4):
                bx = bx0 + (bi % 2) * (bs + 12); by = by0 + (bi // 2) * (bs + 6)
                doc.set_draw_color(150, 140, 160); doc.set_line_width(0.5)
                doc.rect(bx, by, bs, bs)
    doc.set_y(y0 + rows * (cellh + gap) + 4)
    doc.set_font("DM", "B", 11); doc.set_text_color(*ACCENT)
    doc.multi_cell(CW, 16, "You are raising a deeply feeling human — and teaching them what to "
                   "do with it. Keep going, Mama.", align="C")

    os.makedirs(os.path.dirname(OUT_PDF), exist_ok=True)
    doc.output(OUT_PDF)
    print("WROTE", OUT_PDF, "pages:", doc.page)

if __name__ == "__main__":
    main()
