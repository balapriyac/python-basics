#!/usr/bin/env python3
"""
image_resizer_watermarker.py

Resize every image in a folder to a maximum width/height (keeping aspect
ratio) and stamp a text watermark in a corner. Originals are never
modified — output goes to a separate folder.

Requires pillow:
    pip install pillow

Usage:
    python 01_image_resizer_watermarker.py photos/ photos_out/ \
        --max-size 1200 --watermark "(c) My Studio" --position bottom-right
"""

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".webp", ".tiff"}

POSITIONS = ["top-left", "top-right", "bottom-left", "bottom-right", "center"]


def resize_keep_aspect(image, max_size):
    """Resize an image so neither dimension exceeds max_size, keeping aspect ratio."""
    width, height = image.size
    scale = min(max_size / width, max_size / height, 1.0)  # never upscale
    if scale == 1.0:
        return image
    new_size = (int(width * scale), int(height * scale))
    return image.resize(new_size, Image.LANCZOS)


def calculate_watermark_position(image_size, text_size, position, margin=10):
    img_w, img_h = image_size
    text_w, text_h = text_size

    positions = {
        "top-left": (margin, margin),
        "top-right": (img_w - text_w - margin, margin),
        "bottom-left": (margin, img_h - text_h - margin),
        "bottom-right": (img_w - text_w - margin, img_h - text_h - margin),
        "center": ((img_w - text_w) // 2, (img_h - text_h) // 2),
    }
    return positions[position]


def add_watermark(image, text, position="bottom-right", opacity=160, font_size=None):
    """Draw semi-transparent watermark text onto a copy of the image."""
    image = image.convert("RGBA")
    overlay = Image.new("RGBA", image.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)

    if font_size is None:
        font_size = max(14, image.size[0] // 40)

    try:
        font = ImageFont.truetype("DejaVuSans-Bold.ttf", font_size)
    except OSError:
        font = ImageFont.load_default()

    bbox = draw.textbbox((0, 0), text, font=font)
    text_size = (bbox[2] - bbox[0], bbox[3] - bbox[1])

    xy = calculate_watermark_position(image.size, text_size, position)
    draw.text(xy, text, font=font, fill=(255, 255, 255, opacity))

    watermarked = Image.alpha_composite(image, overlay)
    return watermarked.convert("RGB")


def process_folder(input_dir, output_dir, max_size, watermark_text, position):
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    processed, skipped = 0, 0

    for file_path in sorted(input_path.iterdir()):
        if not file_path.is_file() or file_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
            if file_path.is_file():
                print(f"  skipping unsupported file: {file_path.name}")
                skipped += 1
            continue

        try:
            with Image.open(file_path) as img:
                resized = resize_keep_aspect(img, max_size)
                if watermark_text:
                    resized = add_watermark(resized, watermark_text, position)
                out_file = output_path / file_path.name
                resized.save(out_file)
                processed += 1
                print(f"  processed: {file_path.name} -> {out_file}")
        except Exception as e:
            print(f"  ERROR processing {file_path.name}: {e}")
            skipped += 1

    return processed, skipped


def main():
    parser = argparse.ArgumentParser(
        description="Batch resize images and optionally add a text watermark."
    )
    parser.add_argument("input_dir", help="Folder containing the original images")
    parser.add_argument("output_dir", help="Folder to write resized/watermarked images to")
    parser.add_argument("--max-size", type=int, default=1200,
                         help="Maximum width/height in pixels (default: 1200)")
    parser.add_argument("--watermark", default=None,
                         help="Watermark text to stamp on each image (omit to skip watermarking)")
    parser.add_argument("--position", choices=POSITIONS, default="bottom-right",
                         help="Watermark position (default: bottom-right)")
    args = parser.parse_args()

    print(f"Processing images in {args.input_dir} ...")
    processed, skipped = process_folder(
        args.input_dir, args.output_dir, args.max_size, args.watermark, args.position
    )

    print(f"\nDone. {processed} image(s) processed, {skipped} skipped.")
    print(f"Output saved to {args.output_dir}")


if __name__ == "__main__":
    main()
