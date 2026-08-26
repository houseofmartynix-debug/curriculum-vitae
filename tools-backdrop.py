# -*- coding: utf-8 -*-
"""Prepare a photo as the page backdrop and write bg.b64.

    python tools-backdrop.py <image>

Kept recognisable (only a light blur) but tonally pushed back, because body
text sits above it. The veil that keeps the centre readable is applied in CSS
(`.ambient-photo::after`), not baked in here.
"""
import base64
import pathlib
import sys

from PIL import Image, ImageEnhance, ImageFilter, ImageOps

HERE = pathlib.Path(__file__).parent
OUT_B64 = HERE / 'bg.b64'

# Cap rather than upscale: the browser stretches this to viewport width anyway,
# so enlarging a small source only costs bytes and buys no detail.
MAX_W = 800
QUALITY = 72

if len(sys.argv) < 2:
    sys.exit(f'usage: python {pathlib.Path(__file__).name} <image>')
src = pathlib.Path(sys.argv[1])
if not src.is_file():
    sys.exit(f'not a file: {src}')

im = ImageOps.exif_transpose(Image.open(src)).convert('RGB')
print('source', im.size)

w = min(MAX_W, im.size[0])
im = im.resize((w, round(w * im.size[1] / im.size[0])), Image.LANCZOS)

# Push the wall back, keep the subject's colour alive.
im = im.filter(ImageFilter.GaussianBlur(radius=1.4))
im = ImageEnhance.Brightness(im).enhance(0.62)
im = ImageEnhance.Contrast(im).enhance(1.14)
im = ImageEnhance.Color(im).enhance(1.18)
print('final', im.size)

tmp = HERE / '.backdrop.tmp.jpg'
im.save(tmp, 'JPEG', quality=QUALITY, optimize=True, progressive=True)
raw = tmp.read_bytes()
tmp.unlink()

OUT_B64.write_text(base64.b64encode(raw).decode('ascii'), encoding='utf-8')
print(f'jpeg {len(raw)} bytes -> {OUT_B64.name} ({OUT_B64.stat().st_size} bytes)')
print('now run: python build.py')
