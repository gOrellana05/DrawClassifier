from PIL import Image, ImageDraw
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]
def drawing_to_image(drawing, size=28):
    img = Image.new("L", (256,256), color=0)
    draw = ImageDraw.Draw(img)

    for stroke in drawing:
        x, y = stroke
        points = list(zip(x,y))
        draw.line(points, fill=255, width=5)
    img = img.resize((size,size))
    return img


def save_images(data, label):
    import os
    file_path = BASE_DIR / "data"  / "processed" / label

    os.mkdir(file_path)

    for i, item in enumerate(data):
        img = drawing_to_image(item["drawing"])
        img.save(f"{file_path}/{label}_{i}.png")

