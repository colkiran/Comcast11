
import os
import time
# PIL = Pillow
from PIL import Image, ImageFilter

path = "C:/images/"
files = os.listdir(path)
imgFiles = []
for fl in files:
    if fl.endswith("jpg"):
        imgFiles.append(fl)

# print(imgFiles)

st = time.perf_counter()
pxlSize = (1200, 1200)

for imgFl in imgFiles:
    img = Image.open(path + imgFl)

    img = img.filter(ImageFilter.GaussianBlur(15))
    img.thumbnail(pxlSize)
    img.save(f"{path}processed/{imgFl}")
    print(f"{imgFl} was processed......")

et = time.perf_counter()

print(f"Completed processing of all images in {et-st} seconds")

