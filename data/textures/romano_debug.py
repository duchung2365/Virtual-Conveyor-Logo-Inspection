from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024

img = Image.new("RGB", (W, H), (245, 242, 232))
draw = ImageDraw.Draw(img)

# Font mặc định để tránh phụ thuộc font ngoài
font_big = ImageFont.load_default()
font_small = ImageFont.load_default()

# Hexagon
cx, cy = W // 2, H // 2
r = 430

points = []
import math

for i in range(6):
    a = math.radians(60 * i - 30)
    points.append((
        cx + r * math.cos(a),
        cy + r * math.sin(a)
    ))

draw.polygon(points, fill=(35, 35, 35))

# Inner hexagon
r2 = 390
points2 = []

for i in range(6):
    a = math.radians(60 * i - 30)
    points2.append((
        cx + r2 * math.cos(a),
        cy + r2 * math.sin(a)
    ))

draw.polygon(points2, fill=(238, 235, 222))

# Debug text
draw.text((cx - 35, cy - 20), "ROMANO", fill=(20, 20, 20), font=font_big)
draw.text((cx - 35, cy + 10), "MATTE WAX", fill=(20, 20, 20), font=font_small)

# Một vài đường nét giả lập print detail
for y in range(cy + 60, cy + 180, 25):
    draw.line(
        (cx - 180, y, cx + 180, y),
        fill=(30, 30, 30),
        width=4
    )

output = "romano_debug_texture.png"
img.save(output)

print(f"Created: {output}")