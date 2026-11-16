#!/usr/bin/env python3
"""Entry point for ai-excited-01 bounty."""
import os
import shutil
import struct
import sys

MAX_SIZE = 1048576
MAX_DIM = 1024
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(script_dir, "entry.png")

    with open(src, "rb") as f:
        header = f.read(24)

    if len(header) < 24:
        sys.exit("entry.png: file too small to be a valid PNG")

    if header[:8] != PNG_SIGNATURE:
        sys.exit("entry.png: not a PNG file (invalid signature)")

    stat = os.stat(src)
    if stat.st_size > MAX_SIZE:
        sys.exit(f"entry.png: file size {stat.st_size} exceeds {MAX_SIZE} bytes")

    width, height = struct.unpack(">II", header[16:24])
    if width > MAX_DIM or height > MAX_DIM:
        sys.exit(f"entry.png: dimensions {width}x{height} exceed {MAX_DIM}x{MAX_DIM}")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    dst = os.path.join(output_dir, "entry.png")
    shutil.copy2(src, dst)

    print(f"source={src} dest={dst} width={width} height={height} bytes={stat.st_size}")

if __name__ == "__main__":
    main()