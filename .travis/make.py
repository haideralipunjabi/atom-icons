from cairosvg import svg2png
import os
from PIL import Image
def make_linux():
    for file in os.listdir('svg'):
        if file.endswith(".svg"):
            svg2png(url="svg/"+file, write_to="linux/" + file.split('.')[0] + ".png", parent_width=256, parent_height=256)
def make_windows():
    for file in os.listdir('linux'):
        if file.endswith(".png"):
                Image.open("linux/"+file).save("windows/"+file.split('.')[0]+".ico")

#def make_macOS():
    # TODO: macOS generation pending, until I can find a way to convert SVG/PNG to ICNS

make_linux()
make_windows()
