# -*- coding: utf-8 -*-
"""Prepare the Spider-Man mirror selfie as a page backdrop.

Kept recognisable (only a light blur) but tonally pushed back so body text
sitting above it stays readable.
"""
import base64
import pathlib
from PIL import Image, ImageOps, ImageFilter, ImageEnhance

SRC = pathlib.Path('source.jpg')
OUT = pathlib.Path('.')

im = ImageOps.exif_transpose(Image.open(SRC)).convert('RGB')
print('source', im.size)

# The source is only 736px wide, so upscaling adds bytes but no detail — the
# browser scales it up to viewport width anyway and the blur hides it.
TARGET_W = 800
im = im.resize((TARGET_W, round(TARGET_W * im.size[1] / im.size[0])), Image.LANCZOS)

# Push the wall back, keep the red of the mask alive.
im = im.filter(ImageFilter.GaussianBlur(radius=1.4))
im = ImageEnhance.Brightness(im).enhance(0.62)
im = ImageEnhance.Contrast(im).enhance(1.14)
im = ImageEnhance.Color(im).enhance(1.18)
print('final', im.size)

im.save(OUT / 'bg_preview.jpg', 'JPEG', quality=72, optimize=True, progressive=True)
raw = (OUT / 'bg_preview.jpg').read_bytes()
b64 = base64.b64encode(raw).decode('ascii')
print('jpeg bytes', len(raw), '-> base64', len(b64))
(OUT / 'bg.b64').write_text(b64)
