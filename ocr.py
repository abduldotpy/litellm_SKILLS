#!/usr/bin/env python3
"""Send one image to the Zong OCR service and print the recognized text."""
import sys
import requests

URL = "https://aiapplicationsdev.zong.com.pk:8787/v1/chat/completions"


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python ocr.py <image>")
    path = sys.argv[1]
    with open(path, "rb") as f:
        resp = requests.post(URL, files={"file": (path, f)})
    resp.raise_for_status()
    print(resp.json().get("text", ""))


if __name__ == "__main__":
    main()
