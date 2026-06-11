import fitz, os
FONTS = r"C:/Users/Athanase-Chrisbert J/_fonts"
SRC = r"C:/Users/Athanase-Chrisbert J/Downloads/PDFs"
OUT = os.path.join(SRC, "_final"); REND = os.path.join(SRC, "_render")
os.makedirs(OUT, exist_ok=True)

FF = {
 "dmbold":  os.path.join(FONTS,"DMSans-Bold.ttf"),
 "antonio": os.path.join(FONTS,"Antonio-Regular.ttf"),
 "mulbold": os.path.join(FONTS,"Mulish-Bold.ttf"),
 "mulreg":  os.path.join(FONTS,"Mulish-Regular.ttf"),
}
FONTOBJ = {k: fitz.Font(fontfile=v) for k,v in FF.items()}
def rgb01(c): return (c[0]/255,c[1]/255,c[2]/255)

def redact_band(pg, rect):
    pg.add_redact_annot(rect, fill=None, cross_out=False)
    pg.apply_redactions(images=fitz.PDF_REDACT_IMAGE_NONE,
                        graphics=fitz.PDF_REDACT_LINE_ART_NONE)

def center_text(pg, fontkey, text, size, baseline_y, color):
    tl = FONTOBJ[fontkey].text_length(text, size)
    x = (pg.rect.width - tl)/2
    pg.insert_text((x, baseline_y), text, fontsize=size, fontname="F_"+fontkey,
                   fontfile=FF[fontkey], color=rgb01(color))

def left_text(pg, fontkey, text, size, x, baseline_y, color):
    pg.insert_text((x, baseline_y), text, fontsize=size, fontname="F_"+fontkey,
                   fontfile=FF[fontkey], color=rgb01(color))

def find_union(pg, subs):
    u=None
    for b in pg.get_text("dict")["blocks"]:
        for l in b.get("lines",[]):
            for s in l["spans"]:
                if any(x in s["text"] for x in subs):
                    r=fitz.Rect(s["bbox"]); u = r if u is None else (u|r)
    return u

def go(fn, fn_out):
    return fitz.open(os.path.join(SRC, fn)), os.path.join(OUT, fn_out)

W = 595  # all pages 595 wide

# ---- SLEEP ----
d=fitz.open(os.path.join(SRC,"The 7-Day Gentle Sleep Reset From Exhausted to Empowered 2 main .pdf")); pg=d[0]
redact_band(pg, fitz.Rect(0,672,pg.rect.width,710))
center_text(pg,"antonio","THE GROUNDED MAMA",27,700,(255,255,255))
out=os.path.join(OUT,"The 7-Day Gentle Sleep Reset From Exhausted to Empowered 2 main .pdf")
d.save(out,garbage=4,deflate=True); d.close()
fitz.open(out)[0].get_pixmap(dpi=90).save(os.path.join(REND,"sleep_NEW.png"))

# ---- IDENTITY ----
d=fitz.open(os.path.join(SRC,"I Don't Recognise Myself.pdf")); pg=d[0]
u=find_union(pg,["BRIGITTE","SCHWARTZ"])
redact_band(pg, fitz.Rect(u.x0-1,u.y0-1,u.x0+220,u.y1+2))
left_text(pg,"mulreg","THE GROUNDED MAMA",10,u.x0, u.y1-1,(248,246,241))
out=os.path.join(OUT,"I Don't Recognise Myself.pdf")
d.save(out,garbage=4,deflate=True); d.close()
fitz.open(out)[0].get_pixmap(dpi=90).save(os.path.join(REND,"identity_NEW.png"))

# ---- TODDLER (redraw bottom band) ----
d=fitz.open(os.path.join(SRC,"my toddler wont listen.pdf")); pg=d[0]
redact_band(pg, fitz.Rect(0,684,pg.rect.width,752))
center_text(pg,"dmbold","FOR MELTDOWNS",31,711,(255,255,255))
center_text(pg,"dmbold","By The Grounded Mama",20,739,(255,255,255))
out=os.path.join(OUT,"my toddler wont listen.pdf")
d.save(out,garbage=4,deflate=True); d.close()
fitz.open(out)[0].get_pixmap(dpi=90).save(os.path.join(REND,"toddler_NEW.png"))

# ---- SCREENS ----
d=fitz.open(os.path.join(SRC,"detox digital.pdf")); pg=d[0]
u=find_union(pg,["By mom of 3"])
redact_band(pg, fitz.Rect(0,u.y0-1,pg.rect.width,u.y1+2))
center_text(pg,"dmbold","By The Grounded Mama",20, u.y1-3,(255,255,255))
out=os.path.join(OUT,"detox digital.pdf")
d.save(out,garbage=4,deflate=True); d.close()
fitz.open(out)[0].get_pixmap(dpi=90).save(os.path.join(REND,"screens_NEW.png"))

# ---- POSTPARTUM (add byline) ----
d=fitz.open(os.path.join(SRC,"A MOM'S PRACTICAL GUIDE TO POSTPARTUM RECOVERY.pdf")); pg=d[0]
center_text(pg,"mulbold","The Grounded Mama",13,776,(255,255,255))
out=os.path.join(OUT,"A MOM'S PRACTICAL GUIDE TO POSTPARTUM RECOVERY.pdf")
d.save(out,garbage=4,deflate=True); d.close()
fitz.open(out)[0].get_pixmap(dpi=90).save(os.path.join(REND,"postpartum_NEW.png"))

print("DONE all 5")
