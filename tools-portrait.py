# -*- coding: utf-8 -*-
"""Turn the raw cafe selfie into a CV-grade portrait.

Steps: EXIF-normalise -> head-and-shoulders crop -> depth-of-field blur on the
background -> vignette -> tone/sharpen -> resize -> JPEG -> base64.
"""
import base64
import pathlib
from PIL import Image, ImageOps, ImageFilter, ImageEnhance, ImageDraw, ImageChops

SRC = pathlib.Path('source.jpg')
OUT = pathlib.Path('.')

im = ImageOps.exif_transpose(Image.open(SRC)).convert('RGB')
W, H = im.size
print('source', W, H)

# Head-and-shoulders box in source pixels: eyes land ~37% down, hair keeps
# ~16% headroom, aspect matches the 142x158 avatar frame (0.899).
box = (951, 917, 2209, 2317)
im = im.crop(box)
print('cropped', im.size)

# ---- depth of field: sharp subject, softened surroundings ------------------
cw, ch = im.size
blurred = im.filter(ImageFilter.GaussianBlur(radius=max(cw, ch) * 0.055))
# Knock the cafe signage back so no stray text competes with the face.
blurred = ImageEnhance.Brightness(blurred).enhance(0.70)
blurred = ImageEnhance.Color(blurred).enhance(0.40)
blurred = ImageEnhance.Contrast(blurred).enhance(0.80)

# Focus mask = vertical ramp (kills the menu boards above the head) combined
# with an ellipse hugging the head and torso.
ramp = Image.new('L', (1, ch), 0)
top_end, ramp_end = 0.08 * ch, 0.36 * ch
for y in range(ch):
    if y <= top_end:
        v = 0
    elif y >= ramp_end:
        v = 255
    else:
        v = round(255 * (y - top_end) / (ramp_end - top_end))
    ramp.putpixel((0, y), v)
mask_v = ramp.resize((cw, ch), Image.BILINEAR)

mask_e = Image.new('L', (cw, ch), 0)
d = ImageDraw.Draw(mask_e)
fx, fy = cw * 0.50, ch * 0.60
rx, ry = cw * 0.40, ch * 0.48
d.ellipse((fx - rx, fy - ry, fx + rx, fy + ry), fill=255)

mask = ImageChops.darker(mask_v, mask_e)
mask = mask.filter(ImageFilter.GaussianBlur(radius=max(cw, ch) * 0.045))
im = Image.composite(im, blurred, mask)

# ---- vignette --------------------------------------------------------------
vig = Image.new('L', (cw, ch), 0)
dv = ImageDraw.Draw(vig)
dv.ellipse((-cw * 0.16, -ch * 0.16, cw * 1.16, ch * 1.16), fill=255)
vig = vig.filter(ImageFilter.GaussianBlur(radius=max(cw, ch) * 0.13))
dark = ImageEnhance.Brightness(im).enhance(0.55)
im = Image.composite(im, dark, vig)

# ---- tone ------------------------------------------------------------------
im = ImageEnhance.Color(im).enhance(0.97)
im = ImageEnhance.Contrast(im).enhance(1.12)
im = ImageEnhance.Brightness(im).enhance(1.05)

# ---- final size + sharpen --------------------------------------------------
TARGET_W = 600
im = im.resize((TARGET_W, round(TARGET_W * ch / cw)), Image.LANCZOS)
im = im.filter(ImageFilter.UnsharpMask(radius=1.6, percent=95, threshold=3))
print('final', im.size)

im.save(OUT / 'portrait_preview.jpg', 'JPEG', quality=84, optimize=True, progressive=True)
raw = (OUT / 'portrait_preview.jpg').read_bytes()
print('jpeg bytes', len(raw), '-> base64', len(base64.b64encode(raw)))
(OUT / 'portrait.b64').write_text(base64.b64encode(raw).decode('ascii'))
