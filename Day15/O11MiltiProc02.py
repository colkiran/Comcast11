

import os
import time
# PIL = Pillow
from PIL import Image, ImageFilter
import concurrent.futures


path = "C:/images/"
files = os.listdir(path)
imgFiles = []
for fl in files:
    if fl.endswith("jpg"):
        imgFiles.append(fl)

# print(imgFiles)

st = time.perf_counter()
pxlSize = (1200, 1200)

def ImagePrc(imgFl):
    img = Image.open(path + imgFl)

    img = img.filter(ImageFilter.GaussianBlur(15))
    img.thumbnail(pxlSize)
    img.save(f"{path}processed/{imgFl}")
    print(f"{imgFl} was processed......")

if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(ImagePrc, imgFiles)

    et = time.perf_counter()

    print(f"Completed processing of all images in {et-st} seconds")

