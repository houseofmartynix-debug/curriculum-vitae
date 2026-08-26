# -*- coding: utf-8 -*-
"""Turn a raw photo into the CV portrait and write photo.b64.

    python tools-portrait.py <image>

Pipeline: EXIF-normalise -> head-and-shoulders crop -> depth-of-field falloff
over the background -> vignette -> tone -> resize -> JPEG -> Base64.

The crop box is expressed as fractions of the source so it survives a
different resolution; the values are tuned for a square, centred portrait.
"""
import base64
import pathlib
import sys

from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageFilter, ImageOps

HERE = pathlib.Path(__file__).parent
OUT_B64 = HERE / 'photo.b64'

# left, top, right, bottom as fractions of the source: eyes land ~37% down the
# frame, the hair keeps ~16% headroom, and the aspect matches the 142x158 avatar.
CROP = (0.2914, 0.2809, 0.6768, 0.7098)
TARGET_W = 600
QUALITY = 84

if len(sys.argv) < 2:
    sys.exit(f'usage: python {pathlib.Path(__file__).name} <image>')
src = pathlib.Path(sys.argv[1])
if not src.is_file():
    sys.exit(f'not a file: {src}')

im = ImageOps.exif_transpose(Image.open(src)).convert('RGB')
W, H = im.size
print('source', W, H)

im = im.crop((round(CROP[0] * W), round(CROP[1] * H),
              round(CROP[2] * W), round(CROP[3] * H)))
cw, ch = im.size
print('cropped', im.size)

# ---- depth of field: sharp subject, softened surroundings ------------------
blurred = im.filter(ImageFilter.GaussianBlur(radius=max(cw, ch) * 0.055))
# Knock any background signage back so no stray text competes with the face.
blurred = ImageEnhance.Brightness(blurred).enhance(0.70)
blurred = ImageEnhance.Color(blurred).enhance(0.40)
blurred = ImageEnhance.Contrast(blurred).enhance(0.80)

# Focus mask = vertical ramp (kills whatever sits above the head) combined
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
ImageDraw.Draw(mask_e).ellipse(
    (cw * 0.10, ch * 0.12, cw * 0.90, ch * 1.08), fill=255)

mask = ImageChops.darker(mask_v, mask_e)
mask = mask.filter(ImageFilter.GaussianBlur(radius=max(cw, ch) * 0.045))
im = Image.composite(im, blurred, mask)

# ---- vignette --------------------------------------------------------------
vig = Image.new('L', (cw, ch), 0)
ImageDraw.Draw(vig).ellipse(
    (-cw * 0.16, -ch * 0.16, cw * 1.16, ch * 1.16), fill=255)
vig = vig.filter(ImageFilter.GaussianBlur(radius=max(cw, ch) * 0.13))
im = Image.composite(im, ImageEnhance.Brightness(im).enhance(0.55), vig)

# ---- tone ------------------------------------------------------------------
im = ImageEnhance.Color(im).enhance(0.97)
im = ImageEnhance.Contrast(im).enhance(1.12)
im = ImageEnhance.Brightness(im).enhance(1.05)

# ---- final size + sharpen --------------------------------------------------
im = im.resize((TARGET_W, round(TARGET_W * ch / cw)), Image.LANCZOS)
im = im.filter(ImageFilter.UnsharpMask(radius=1.6, percent=95, threshold=3))
print('final', im.size)

tmp = HERE / '.portrait.tmp.jpg'
im.save(tmp, 'JPEG', quality=QUALITY, optimize=True, progressive=True)
raw = tmp.read_bytes()
tmp.unlink()

OUT_B64.write_text(base64.b64encode(raw).decode('ascii'), encoding='utf-8')
print(f'jpeg {len(raw)} bytes -> {OUT_B64.name} ({OUT_B64.stat().st_size} bytes)')
print('now run: python build.py')
