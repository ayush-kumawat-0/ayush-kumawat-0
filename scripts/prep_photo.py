"""
Prepare Ayush's headshot for the ASCII renderer.

The profile uses a head-only source image with a deliberately clean,
high-key background. This script keeps the workflow deterministic:
- convert to grayscale
- smooth photographic noise while retaining facial edges
- increase local/global contrast
- turn very bright background pixels into pure white
- save a square grayscale image for make_ascii_svg.py

Usage:
    python scripts/prep_photo.py
    python scripts/prep_photo.py input.png output.png
"""
import os
import sys

import numpy as np
from PIL import Image, ImageEnhance, ImageFilter, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
INP = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "source-photo.png")
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "..", "source-prepped.png")

img = Image.open(INP).convert("RGB")
gray = ImageOps.grayscale(img)

# Remove fine photographic noise without destroying eyes, hair and beard.
gray = gray.filter(ImageFilter.GaussianBlur(0.45))
gray = ImageEnhance.Contrast(gray).enhance(1.28)
gray = ImageEnhance.Sharpness(gray).enhance(1.15)

arr = np.asarray(gray, dtype=np.uint8)

# The source is intentionally framed against a bright sky/background.
# Anything this bright becomes the blank ASCII background.
arr = np.where(arr >= 205, 255, arr).astype(np.uint8)

Image.fromarray(arr, mode="L").save(OUT)
print(f"wrote {OUT}: {arr.shape[1]}x{arr.shape[0]}")
