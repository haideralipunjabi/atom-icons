from cairosvg import svg2png
import os
from PIL import Image
import simplejson
import json
def make_linux():
    if not os.path.exists('linux'):
        os.makedirs('linux')
    for file in os.listdir('svg'):
        if file.endswith(".svg"):
            svg2png(url="svg/"+file, write_to="linux/" + file.split('.')[0] + ".png", parent_width=256, parent_height=256)
def make_windows():
    if not os.path.exists('windows'):
        os.makedirs('windows')
    for file in os.listdir('linux'):
        if file.endswith(".png"):
                Image.open("linux/"+file).save("windows/"+file.split('.')[0]+".ico")

#def make_macOS():
    # TODO: macOS generation pending, until I can find a way to convert SVG/PNG to ICNS


def make_readme():
    readme = open('READMETEMPLATE.md', 'r+')
    lines = readme.readlines()
    target_index = lines.index("## Available Icons\n")
    endlines = lines[target_index+1:]
    lines = lines[:target_index+1]
    series = json.load(open('.travis/series.json'))
    for s in series:
        lines.append("### " + s['name'] + "\n")
        lines.append("These icons were contributed by: @" + s['contributor'] + "\n")
        for file in os.listdir('svg'):
            if(file.split('_')[0] == s['prefix'] and file.endswith('.svg')):
                lines.append("![%s](%s)"%(file, 'svg/'+file))
    lines.append("### Others\n")
    for file in os.listdir('svg'):
        if(not file.__contains__('_') and file.endswith('.svg')):
            lines.append("![%s](%s)"%(file, 'svg/'+file))
    lines.append("\n")
    lines.extend(endlines)
    print(' '.join(lines), file=open('README.md', 'w'))
make_linux()
make_windows()
make_readme()
