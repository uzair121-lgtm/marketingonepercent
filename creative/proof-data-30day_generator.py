#!/usr/bin/env python3
"""Animatic for the proof-through-data Reel: '30 days of 1%. Here's the graph.'
9:16, no faces, app-style data reveal. Placeholder data, clearly labelled."""
import os, sys, math
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1920
FPS = 30
DUR = 24
NFRAMES = FPS * DUR  # 720
OUT = sys.argv[1] if len(sys.argv) > 1 else "frames"
os.makedirs(OUT, exist_ok=True)

FD = "/mnt/skills/examples/canvas-design/canvas-fonts"
def F(name, size): return ImageFont.truetype(f"{FD}/{name}.ttf", size)
disp   = lambda s: F("BigShoulders-Bold", s)
sans_b = lambda s: F("InstrumentSans-Bold", s)
sans   = lambda s: F("InstrumentSans-Regular", s)
mono_b = lambda s: F("GeistMono-Bold", s)

BG    = (10, 11, 13)
CARD  = (20, 22, 26)
GRID  = (34, 38, 44)
WHITE = (245, 247, 250)
MUTE  = (138, 144, 153)
ACC   = (124, 245, 110)   # emerald-lime
ACCd  = (60, 120, 55)

def lerp(a, b, t): return a + (b - a) * t
def clamp(x, lo=0.0, hi=1.0): return max(lo, min(hi, x))
def ease(t): return t * t * (3 - 2 * t)  # smoothstep
def mix(c1, c2, t): return tuple(int(lerp(c1[i], c2[i], t)) for i in range(3))

def ctext(d, xy, s, font, fill, anchor="mm", spacing=0):
    d.text(xy, s, font=font, fill=fill, anchor=anchor, spacing=spacing)

# compounding model: value = 1.01^day ; pct improvement = (1.01^day - 1)*100
def pct_at(day): return (1.01 ** day - 1) * 100.0

# --- timeline: reveal_day and active caption as a function of frame ---
def state(f):
    if f < 15:            # intro: ghost of the finished curve
        return dict(day=30, ghost=1.0, ui=0.0)
    if f < 45:            # retract to day 0
        t = ease((f - 15) / 30)
        return dict(day=lerp(30, 0.6, t), ghost=lerp(1.0, 0.0, t), ui=t)
    if f < 120:           # hold on day 1
        return dict(day=1.0, ghost=0.0, ui=1.0)
    if f < 270:           # timelapse 1 -> 30
        t = ease((f - 120) / 150)
        return dict(day=lerp(1.0, 30.0, t), ghost=0.0, ui=1.0)
    return dict(day=30.0, ghost=0.0, ui=1.0)  # land + hold

CAPS = [  # (start, end, text, font_size)
    (0,   45,  "30 DAYS OF 1%", 150),
    (45,  120, "Day 1. One 1% action.", 96),
    (120, 270, "1% better. Every day.", 104),
    (270, 480, "+35% in a month.", 132),
    (480, 630, "The gains hide in\nthe boring days.", 100),
    (630, 720, "Day 60 loads next.\nFollow →", 108),
]

def caption_for(f):
    for s, e, txt, sz in CAPS:
        if s <= f < e:
            # fade in/out 8 frames
            a = clamp((f - s) / 8) * clamp((e - f) / 8)
            return txt, sz, a
    return None, 0, 0

# graph geometry (card)
GX, GY, GW, GH = 90, 250, W - 180, 760

def draw_graph(d, day, ghost):
    # card
    d.rounded_rectangle([GX, GY, GX+GW, GY+GH], radius=40, fill=CARD)
    pad = 60
    x0, y0 = GX + pad, GY + GH - pad
    x1, y1 = GX + GW - pad, GY + pad + 20
    # gridlines
    for i in range(5):
        gy = lerp(y0, y1, i/4)
        d.line([x0, gy, x1, gy], fill=GRID, width=2)
    ymax = pct_at(30)
    def pt(dd):
        x = lerp(x0, x1, clamp(dd/30))
        y = lerp(y0, y1, clamp(pct_at(dd)/ymax))
        return x, y
    # ghost full curve (intro)
    if ghost > 0:
        gc = mix(CARD, ACC, 0.35*ghost)
        pts = [pt(k*30/60) for k in range(61)]
        d.line(pts, fill=gc, width=6, joint="curve")
    # live curve up to current day
    if day > 0.6:
        n = 80
        pts = [pt(k*day/n) for k in range(n+1)]
        if len(pts) > 1:
            d.line(pts, fill=ACC, width=10, joint="curve")
        hx, hy = pt(day)
        d.ellipse([hx-16, hy-16, hx+16, hy+16], fill=ACC)
        d.ellipse([hx-7, hy-7, hx+7, hy+7], fill=BG)
    # axis labels
    ctext(d, (x0, y0+42), "Day 1", sans(30), MUTE, "lm")
    ctext(d, (x1, y0+42), "Day 30", sans(30), MUTE, "rm")

def draw_ui(d, day, ui):
    if ui <= 0: return
    a = ui
    def fade(c): return mix(BG, c, a)
    # brand row
    ctext(d, (90, 150), "1%", disp(84), fade(ACC), "lm")
    ctext(d, (170, 158), "DAILY PROGRESS", sans_b(34), fade(MUTE), "lm")
    # streak pill (top right)
    streak = max(1, round(day))
    pill = f"{streak}-DAY STREAK"
    pw = sans_b(34).getlength(pill) + 90
    px1 = W - 90
    d.rounded_rectangle([px1-pw, 128, px1, 190], radius=31, outline=fade(ACCd), width=3)
    ctext(d, (px1-45, 159), pill, sans_b(34), fade(ACC), "rm")
    d.ellipse([px1-pw+40, 149, px1-pw+60, 169], fill=fade(ACC))
    # big cumulative number below the graph
    pct = pct_at(day)
    ctext(d, (W/2, GY+GH+120), f"+{pct:04.1f}%", mono_b(150), fade(WHITE), "mm")
    ctext(d, (W/2, GY+GH+215), "cumulative improvement", sans(38), fade(MUTE), "mm")

def draw_caption(d, f):
    txt, sz, a = caption_for(f)
    if not txt or a <= 0: return
    y = 1560
    # subtle backing
    ctext(d, (W/2, y), txt, disp(sz), mix(BG, ACC if f>=630 else WHITE, a), "mm", spacing=12)
    # 'Save this' flash
    if 470 <= f < 560:
        sa = clamp((f-470)/8) * clamp((560-f)/8)
        tag = "  SAVE THIS  "
        tw = sans_b(40).getlength(tag)
        d.rounded_rectangle([W/2-tw/2-20, 1770, W/2+tw/2+20, 1850], radius=40,
                            fill=mix(BG, ACC, sa))
        ctext(d, (W/2, 1810), "SAVE THIS", sans_b(40), mix(BG, (10,11,13), 1), "mm")

def draw_progress(d, f):
    # thin progress bar at very bottom
    d.rectangle([0, H-8, W*f/NFRAMES, H], fill=ACC)

def render(f):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img, "RGBA")
    st = state(f)
    draw_graph(d, st["day"], st["ghost"])
    draw_ui(d, st["day"], st["ui"])
    draw_caption(d, f)
    # watermark: placeholder-data honesty
    ctext(d, (W/2, 1890), "illustrative data · replace with your screen recording",
          sans(24), (70, 74, 80), "mm")
    draw_progress(d, f)
    return img

if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "test":
        for tf in (5, 30, 80, 200, 380, 520, 680):
            render(tf).save(f"{OUT}/test_{tf:03d}.png")
        print("test frames written")
    else:
        for f in range(NFRAMES):
            render(f).save(f"{OUT}/f{f:04d}.png")
            if f % 120 == 0: print("frame", f)
        print("done", NFRAMES)
