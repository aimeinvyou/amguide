from PIL import Image
import glob

for file in glob.glob("*.png"):
    image = Image.open(file).convert("RGB")
    image.save(file.replace("png", "jpg"))