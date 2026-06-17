---
name: ocr-text-extractor
description: >-
  Extract text from an image using the Zong OCR service (RapidOCR). Use whenever
  the user wants to read or pull text out of an image, screenshot, photo, or
  scan — e.g. "what does this image say", "get the text from this", "OCR this" —
  even if they don't say the word "OCR".
---

# OCR Text Extractor

Send an image to the Zong OCR service and get back the recognized text.

## When to use
The user gives an image and wants the text inside it.

## How to use
```bash
pip install requests          # once
python scripts/ocr.py <image>
```

Or call the service directly:
```bash
curl -X POST "https://aiapplicationsdev.zong.com.pk:8787/v1/chat/completions" \
  -F "file=@image.png"
```

The service returns JSON: `{"text": "...recognized text..."}`.

## Output
Print the recognized text as-is. If `text` comes back empty, say no text was
detected — don't make anything up.
