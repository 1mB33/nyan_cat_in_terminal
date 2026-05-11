from PIL import Image
import numpy as np

ASCII = " .:-=+*#%@"

def img_to_ascii(img, size=(32, 32)):
    img = img.convert("L").resize(size)

    pixels = np.array(img)

    result = []
    for row in pixels:
        line = ""
        for px in row:
            idx = int(px / 255 * (len(ASCII) - 1))
            line += ASCII[idx]
        result.append(line)

    return "\n".join(result)


gif = Image.open("nyan_cat.gif")

frames = []

for i in range(0, 20):
    gif.seek(i)
    frame = gif.copy()
    w, h = frame.size
    frame = frame.crop((w / 4, h / 4, w - w / 4, h - h / 4))
    frames.append(img_to_ascii(frame))

for i, f in enumerate(frames):
    print(f"\nFRAME {i+1}\n")
    print(f)
