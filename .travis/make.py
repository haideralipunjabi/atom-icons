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

def make_macOS():
    if not os.path.exists('macOS'):
        os.makedirs('macOS')
    for file in os.listdir('linux'):
        if file.endswith(".png"):
                Image.open("linux/"+file).save("macOS/"+file.split('.')[0]+".icns")

def make_readme():
    readme = open('READMETEMPLATE.md', 'r+')
    lines = readme.readlines()
    target_index = lines.index("## Available Icons\n")
    endlines = lines[target_index+1:]
    lines = lines[:target_index+1]
    series = json.load(open('.travis/series.json'))
    for s in series:
        lines.append("\n### " + s['name'] + "\n")
        lines.append("These icons were contributed by: [@" + s['contributor'] + "](https://github.com/"+s['contributor']+")\n\n")
        for file in os.listdir('svg'):
            if(file.split('_')[0] == s['prefix'] and file.endswith('.svg')):
                lines.append("<img title=\"%s\" src=\"%s\" width=\"128px\">"%(file, 'svg/'+file))
    lines.append("\n### Others\n")
    for file in os.listdir('svg'):
        if(not file.__contains__('_') and file.endswith('.svg')):
            lines.append("<img title=\"%s\" src=\"%s\" width=\"128px\">"%(file, 'svg/'+file))
    lines.append("\n")
    lines.extend(endlines)
    print(' '.join(lines), file=open('README.md', 'w'))
make_linux()
make_windows()
make_macOS()
make_readme()
