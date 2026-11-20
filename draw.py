#!/usr/bin/env python3
"""Render the 20 November 2026 front-page poster (1024x1024 PNG).

Draws the day's ten verified stories as a newspaper front page: a navy
masthead, one lead story with a cyclone graphic, a 2x2 grid of ranked
stories, and a five-column strip for the remaining headlines.
Run:  python3 draw.py [output-path]   (default: entry.png)
"""

import sys

from PIL import Image, ImageDraw, ImageFont

CANVAS_W = 1024
CANVAS_H = 1024

PAPER = (246, 241, 231)
NAVY = (26, 35, 64)
NAVY_DEEP = (18, 25, 48)
RED = (179, 39, 46)
GOLD = (212, 160, 32)
INK = (24, 24, 24)
BODY_INK = (38, 38, 38)
MUTED = (110, 105, 95)
CARD_EDGE = (210, 203, 190)
WHITE = (255, 255, 255)
TEAL_A = (64, 164, 178)
TEAL_B = (38, 122, 140)
TEAL_C = (110, 200, 210)
CYCLONE_GOLD = (232, 178, 44)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(f"{FONT_DIR}/{name}", size)


def split_lines(draw, text, fnt, max_w):
    """Greedy word wrap: returns the lines that fit inside max_w pixels."""
    lines = []
    current = ""
    for word in text.split(" "):
        trial = word if not current else current + " " + word
        if draw.textlength(trial, font=fnt) <= max_w or not current:
            current = trial
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_lines(draw, lines, x, y, fnt, fill, leading):
    """Draw wrapped lines top-down; returns the y just past the last line."""
    cursor = y
    for line in lines:
        draw.text((x, cursor), line, font=fnt, fill=fill)
        cursor += leading
    return cursor


def masthead(draw):
    draw.rectangle([0, 0, CANVAS_W, 104], fill=NAVY)
    title_font = font("DejaVuSans-Bold.ttf", 48)
    draw.text((28, 20), "THE WORLD IN ONE DAY", font=title_font, fill=WHITE)
    tag_font = font("DejaVuSans-Bold.ttf", 30)
    tag = "WORLD NEWS"
    draw.text(
        (CANVAS_W - 28 - draw.textlength(tag, font=tag_font), 32),
        tag,
        font=tag_font,
        fill=GOLD,
    )
    date_font = font("DejaVuSans.ttf", 23)
    draw.text((28, 72), "Friday, 20 November 2026", font=date_font, fill=WHITE)
    draw.rectangle([0, 104, CANVAS_W, 110], fill=RED)


def cyclone_panel(draw, box):
    """Navy panel with concentric storm rings and a gold eye."""
    x0, y0, x1, y1 = box
    draw.rectangle(box, fill=NAVY_DEEP)
    cx = (x0 + x1) // 2
    cy = (y0 + y1) // 2 + 6
    ring = 14
    shades = [TEAL_A, TEAL_B, TEAL_C]
    step = 0
    while ring <= 124:
        shade = shades[step % len(shades)]
        draw.ellipse(
            [cx - ring, cy - ring, cx + ring, cy + ring],
            outline=shade,
            width=7,
        )
        # A lighter arc segment on each ring suggests the spin.
        draw.arc(
            [cx - ring, cy - ring, cx + ring, cy + ring],
            start=200 + step * 37,
            end=320 + step * 37,
            fill=TEAL_C,
            width=7,
        )
        ring += 16
        step += 1
    draw.ellipse([cx - 15, cy - 15, cx + 15, cy + 15], fill=CYCLONE_GOLD)
    label_font = font("DejaVuSans-Bold.ttf", 20)
    top_label = "BAY OF BENGAL"
    draw.rectangle(
        [x0 + 8, y0 + 8, x0 + 14 + draw.textlength(top_label, font=label_font) + 8, y0 + 38],
        fill=NAVY_DEEP,
    )
    draw.text((x0 + 14, y0 + 12), top_label, font=label_font, fill=WHITE)
    bottom_label = "NOON IST \u00b7 GOPALPUR"
    draw.rectangle(
        [x0 + 8, y1 - 42, x0 + 14 + draw.textlength(bottom_label, font=label_font) + 8, y1 - 8],
        fill=NAVY_DEEP,
    )
    draw.text((x0 + 14, y1 - 38), bottom_label, font=label_font, fill=WHITE)


def lead_story(draw):
    draw.rectangle([24, 122, 1000, 452], fill=WHITE, outline=CARD_EDGE, width=2)
    kicker_font = font("DejaVuSans-Bold.ttf", 28)
    draw.text((44, 138), "CYCLONE AKVAN MAKES LANDFALL", font=kicker_font, fill=RED)
    head_font = font("DejaVuSans-Bold.ttf", 44)
    head_lines = split_lines(
        draw,
        "Cyclone Akvan hits India's east coast at noon",
        head_font,
        604,
    )
    end_y = draw_lines(draw, head_lines, 44, 176, head_font, INK, 52)
    body_font = font("DejaVuSans.ttf", 22)
    body_lines = split_lines(
        draw,
        "Severe Cyclone Akvan made landfall near Gopalpur, Odisha, with "
        "winds of 90\u2013100 km/h (IMD). More than 100,000 people were "
        "evacuated to shelters.",
        body_font,
        604,
    )
    draw_lines(draw, body_lines, 44, end_y + 14, body_font, BODY_INK, 29)
    cyclone_panel(draw, (668, 138, 984, 436))


def grid_card(draw, box, kicker, body):
    x0, y0, x1, y1 = box
    draw.rectangle(box, fill=WHITE, outline=CARD_EDGE, width=2)
    draw.rectangle([x0, y0, x0 + 8, y1], fill=RED)
    kicker_font = font("DejaVuSans-Bold.ttf", 27)
    draw.text((x0 + 28, y0 + 14), kicker, font=kicker_font, fill=INK)
    body_font = font("DejaVuSans.ttf", 20)
    body_lines = split_lines(draw, body, body_font, x1 - x0 - 56)
    draw_lines(draw, body_lines, x0 + 28, y0 + 52, body_font, BODY_INK, 26)


def ranked_grid(draw):
    stories = [
        (
            "GTA VI, DAY TWO",
            "$1.84bn and 19.05m copies on Sensor Tower's count; streams "
            "peaked at 7.91m viewers. Take-Two's first official tally is "
            "expected today.",
        ),
        (
            "SHENZHEN SUMMIT",
            "A day after the first Trump\u2013Xi\u2013Putin meeting, leaders "
            "press on in Shenzhen on day two of the summit.",
        ),
        (
            "WORLD COURT",
            "The ICJ ruled Myanmar committed genocide against the "
            "Rohingya. The ruling, handed down on 19 November, cannot be "
            "appealed.",
        ),
        (
            "SEOUL RETRIAL",
            "South Korea's top court overturns ex-PM Han Duck-soo's "
            "15-year sentence in part and sends the martial-law case back "
            "for retrial.",
        ),
    ]
    boxes = [
        (24, 468, 500, 652),
        (524, 468, 1000, 652),
        (24, 668, 500, 852),
        (524, 668, 1000, 852),
    ]
    for box, (kicker, body) in zip(boxes, stories):
        grid_card(draw, box, kicker, body)


def bottom_strip(draw):
    draw.rectangle([24, 868, 1000, 968], fill=NAVY)
    items = [
        ("CRIMEAN BRIDGE", "Ukraine hits the bridge; rail traffic halted."),
        (
            "FIJI DROUGHT",
            "Nationwide state of disaster declared over El Ni\u00f1o drought.",
        ),
        (
            "YONGBYON",
            "IAEA: North Korea is expanding its uranium enrichment plant.",
        ),
        (
            "US\u2013VENEZUELA",
            "US and Venezuela restore military cooperation.",
        ),
        (
            "COP31",
            "Latest climate draft drops any reference to fossil fuels.",
        ),
    ]
    col_x = 36
    col_w = 182
    gap = 12
    kicker_font = font("DejaVuSans-Bold.ttf", 18)
    body_font = font("DejaVuSans.ttf", 16)
    for kicker, body in items:
        draw.text((col_x, 878), kicker, font=kicker_font, fill=GOLD)
        body_lines = split_lines(draw, body, body_font, col_w)
        draw_lines(draw, body_lines, col_x, 902, body_font, WHITE, 20)
        col_x += col_w + gap


def footer(draw):
    small = font("DejaVuSans.ttf", 16)
    left = "Sources: IMD \u00b7 Sensor Tower \u00b7 Reuters \u00b7 AP \u00b7 BBC \u2014 20 November 2026"
    draw.text((24, 978), left, font=small, fill=MUTED)
    right = "make.fun \u00b7 news-image-20261120"
    draw.text(
        (CANVAS_W - 24 - draw.textlength(right, font=small), 978),
        right,
        font=small,
        fill=MUTED,
    )


def build():
    canvas = Image.new("RGB", (CANVAS_W, CANVAS_H), PAPER)
    draw = ImageDraw.Draw(canvas)
    masthead(draw)
    lead_story(draw)
    ranked_grid(draw)
    bottom_strip(draw)
    footer(draw)
    return canvas


def main():
    target = sys.argv[1] if len(sys.argv) > 1 else "entry.png"
    poster = build()
    poster.save(target, format="PNG")
    print(f"wrote {target} ({poster.size[0]}x{poster.size[1]})")


if __name__ == "__main__":
    main()
