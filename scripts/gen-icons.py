from PIL import Image, ImageDraw, ImageFont
import os

base = os.path.join(os.path.dirname(__file__), "..", "icons")
os.makedirs(base, exist_ok=True)


def draw_icon(size, path):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    margin = int(size * 0.06)
    d.rounded_rectangle(
        [margin, margin, size - margin, size - margin],
        radius=int(size * 0.22),
        fill="#2B4DA8",
    )
    inner = int(size * 0.78)
    off = (size - inner) // 2
    d.rounded_rectangle(
        [off, off, off + inner, off + inner],
        radius=int(size * 0.18),
        fill="#4BBFEA",
    )
    font_size = int(size * 0.42)
    try:
        font = ImageFont.truetype("arialbd.ttf", font_size)
    except OSError:
        font = ImageFont.load_default()
    text = "A"
    bbox = d.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    d.text(
        ((size - tw) / 2 - bbox[0], (size - th) / 2 - bbox[1] - size * 0.02),
        text,
        fill="white",
        font=font,
    )
    img.save(path, "PNG")


for s in [72, 96, 128, 144, 152, 180, 192, 384, 512]:
    draw_icon(s, os.path.join(base, f"icon-{s}.png"))

print("icons ok")
