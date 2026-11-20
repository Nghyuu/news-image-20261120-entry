# Draws entry.png: a front-page poster summing up Friday 20 November 2026.
# Every headline was verified against a reputable outlet on 20 Nov 2026
# (IMD via India Today/Mint, Sensor Tower via GameSpot, Reuters, AP, BBC)
# before drawing. The lead is Cyclone Akvan's landfall at noon IST.
# Render: python3 draw.py  ->  entry.png (1024x1024, < 1 MiB)
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
NAVY = (22, 33, 62)
NAVY2 = (42, 58, 99)
TEAL = (46, 148, 158)
RED = (179, 49, 42)
GOLD = (217, 165, 33)
CREAM = (244, 239, 230)
CARD = (255, 255, 255)
BORDER = (201, 194, 178)
INK = (34, 34, 34)
GRAY = (107, 107, 107)

FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(d, text, f, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def para(d, x, y, text, f, max_w, lh, color=INK):
    for ln in wrap(d, text, f, max_w):
        d.text((x, y), ln, font=f, fill=color)
        y += lh
    return y


def fit(d, text, path, size, max_w):
    f = font(path, size)
    while size > 12 and d.textlength(text, font=f) > max_w:
        size -= 1
        f = font(path, size)
    return f


img = Image.new("RGB", (W, H), CREAM)
d = ImageDraw.Draw(img)

# --- masthead ---
d.rectangle([0, 0, W, 104], fill=NAVY)
f_title = fit(d, "THE WORLD IN ONE DAY", FB, 54, 700)
d.text((24, 18), "THE WORLD IN ONE DAY", font=f_title, fill=(255, 255, 255))
f_wn = font(FB, 30)
d.text((W - 24 - d.textlength("WORLD NEWS", font=f_wn), 26), "WORLD NEWS",
       font=f_wn, fill=GOLD)
d.text((24, 74), "Friday, 20 November 2026", font=font(FR, 19),
       fill=(230, 230, 230))
d.rectangle([0, 104, W, 110], fill=RED)


def card(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=CARD, outline=BORDER, width=1)


# --- lead: Cyclone Akvan ---
card(24, 122, 976, 252)
d.text((44, 138), "CYCLONE AKVAN MAKES LANDFALL",
       font=fit(d, "CYCLONE AKVAN MAKES LANDFALL", FB, 29, 546), fill=RED)
f_h = fit(d, "Storm hits India's east coast", FB, 33, 546)
d.text((44, 176), "Storm hits India's east coast", font=f_h, fill=INK)
d.text((44, 214), "at noon, 90–100 km/h winds", font=f_h, fill=INK)
para(d, 44, 260,
     "Severe Cyclone Akvan crosses near Gopalpur, Odisha. More than "
     "100,000 people moved to shelters; schools shut in 11 districts.",
     font(FR, 18), 540, 24)
# cyclone panel: spiral bands over a storm coast
px, py, pw, ph = 610, 142, 370, 212
d.rectangle([px, py, px + pw, py + ph], fill=NAVY)
cx, cy = px + pw // 2, py + ph // 2 + 10
for r in (96, 78, 60, 42, 26):
    d.arc([cx - r, cy - r, cx + r, cy + r], start=200, end=560, fill=TEAL, width=9)
    d.arc([cx - r, cy - r, cx + r, cy + r], start=20, end=200, fill=(120, 190, 200), width=9)
d.ellipse([cx - 12, cy - 12, cx + 12, cy + 12], fill=GOLD)
d.text((px + 16, py + 8), "BAY OF BENGAL", font=font(FB, 15), fill=(255, 255, 255))
d.text((px + 16, py + ph - 30), "NOON IST · GOPALPUR", font=font(FB, 15),
       fill=(255, 255, 255))

# --- row 2 ---
card(24, 392, 476, 196)
d.rectangle([24, 392, 32, 588], fill=RED)
d.text((48, 410), "GTA VI, DAY TWO", font=font(FB, 25), fill=INK)
para(d, 48, 452,
     "The biggest launch ever keeps rolling: $1.84bn and 19m copies on "
     "Sensor Tower's count, streams peaking at 7.9m. Take-Two's first "
     "official tally is expected today.",
     font(FR, 17), 428, 23)

card(524, 392, 476, 196)
d.rectangle([524, 392, 532, 588], fill=RED)
d.text((548, 410), "SHENZHEN SUMMIT", font=font(FB, 25), fill=INK)
para(d, 548, 452,
     "A day after the first Trump–Xi–Putin meeting, APEC leaders press "
     "on in Shenzhen. Nuclear arms and the Gulf war top the agenda.",
     font(FR, 17), 428, 23)

# --- row 3 ---
card(24, 604, 476, 196)
d.rectangle([24, 604, 32, 800], fill=RED)
d.text((48, 622), "WORLD COURT", font=font(FB, 25), fill=INK)
para(d, 48, 664,
     "The ICJ rules Myanmar committed genocide against the Rohingya. "
     "The ruling cannot be appealed; the world reacts.",
     font(FR, 17), 428, 23)

card(524, 604, 476, 196)
d.rectangle([524, 604, 532, 800], fill=RED)
d.text((548, 622), "SEOUL RETRIAL", font=font(FB, 25), fill=INK)
para(d, 548, 664,
     "South Korea's top court overturns ex-PM Han Duck-soo's 15-year "
     "sentence in part and sends the martial-law case back for retrial.",
     font(FR, 17), 428, 23)

# --- bottom strip: five minis ---
d.rectangle([24, 816, 1000, 948], fill=NAVY)
minis = [
    ("CRIMEAN BRIDGE",
     "Ukraine hits the bridge to Crimea; rail traffic halted."),
    ("FIJI DROUGHT",
     "Nationwide state of disaster as El Niño dries water supplies."),
    ("YONGBYON",
     "IAEA: North Korea is expanding its uranium enrichment plant."),
    ("US–VENEZUELA",
     "Washington and Caracas agree to restore military cooperation."),
    ("COP31",
     "Latest climate draft drops any reference to fossil fuels."),
]
col_w = 976 // 5
for i, (head, body) in enumerate(minis):
    x = 24 + i * col_w + 12
    d.text((x, 830), head, font=font(FB, 16), fill=GOLD)
    para(d, x, 856, body, font(FR, 14), col_w - 24, 19, color=(235, 235, 235))

# --- footer ---
d.text((24, 966), "Sources: IMD · Sensor Tower · Reuters · AP · BBC — 20 November 2026",
       font=font(FR, 15), fill=GRAY)
ftr = "make.fun · news-image-20261120"
d.text((W - 24 - d.textlength(ftr, font=font(FR, 15)), 966), ftr,
       font=font(FR, 15), fill=GRAY)

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)
