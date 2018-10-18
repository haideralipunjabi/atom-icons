from cairosvg import svg2png
import os
from PIL import Image
import simplejson
import json
import random
import requests

ICNS_SIZES = [
[16,72,],
[32,144],
[32,72],
[64,144],
[128,72],
[256,144],
[256,72],
[512,144],
[512,72],
[1024,144]
]
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

def get_size_name(size):
    if size[1] == 144:
        return str(size[0]//2) + 'x' + str(size[0]//2) + '@2x'
    return str(size[0]) + 'x' + str(size[0])

# def prep_macOS():
#     if not os.path.exists('macOS'):
#         os.makedirs('macOS')
#     for file in os.listdir('svg'):
#         if file.endswith(".svg"):
#             if not os.path.exists('macOS/'+file.split('.')[0] + '.iconset/'):
#                 os.makedirs('macOS/'+file.split('.')[0] + '.iconset/')
#             for size in ICNS_SIZES:
#                 svg2png(url="svg/"+file, write_to="macOS/"+file.split('.')[0] + '.iconset/icon_' + get_size_name(size) + ".png", parent_width=size[0], parent_height=size[0], dpi=size[1])

def make_readme():
    readme = open('READMETEMPLATE.md', 'r+')
    lines = readme.readlines()
    target_index = lines.index("## Available Icons\n")
    endlines = lines[target_index+1:]
    lines = lines[:target_index+1]
    lines.append("Total Icons Available: " +    str(os.listdir('svg').__len__()) + "\n")
    series = json.load(open('.travis/series.json'))
    for s in series:
        files = []
        for file in os.listdir('svg'):
            if(file.split('_')[0] == s['prefix'] and file.endswith('.svg')):
                files.append(file)
        len = files.__len__()
        lines.append("\n### " + s['name'] +"\n")
        lines.append("These icons were contributed by: [@" + s['contributor'] + "](https://github.com/"+s['contributor']+")  \n\n")
        lines.append("Icons in this series: " + str(len) + "\n\n")

        if(len > 16):
            random.shuffle(files)
            len = 16
        for i in range(0,len):
            lines.append("<img title=\"%s\" src=\"%s\" width=\"128px\">"%(files[i], 'svg/'+files[i]))
    lines.append("\n### Others\n")
    for file in os.listdir('svg'):
        if(not file.__contains__('_') and file.endswith('.svg')):
            lines.append("<img title=\"%s\" src=\"%s\" width=\"128px\">"%(file, 'svg/'+file))
    lines.append("\n")
    lines.extend(endlines)

    target_index = lines.index("## Non Series Contributions\n")
    endlines = lines[target_index+1:]
    lines = lines[:target_index+1]
    nonseries = json.load(open('.travis/nonseries.json'))
    for c in nonseries:
        if c['contributions'].__len__() == 1:
            lines.append("* [%s](svg/%s.svg) by [@%s](https://github.com/%s)\n"%(c['contributions'][0],c['contributions'][0],c['name'],c['name']))
        else:
            lines.append("* [@%s](https://github.com/%s)\n"%(c['name'], c['name']))
            for contribution in c['contributions']:
                lines.append("    * [%s](svg/%s.svg)\n"%(contribution,contribution))
    lines.append("\n")
    lines.extend(endlines)
    print(' '.join(lines), file=open('README.md', 'w'))

def make_listoffiles():
    files = []
    for file in os.listdir('svg'):
        if file.endswith('.svg'):
            files.append(file.split('.')[0])
    files_data = {}
    nonseries = json.load(open('.travis/nonseries.json'))
    for c in nonseries:
        for contribution in c['contributions']:
            if files.__contains__(contribution):
                files_data[contribution] = c['name']
                files.remove(contribution)
    series = json.load(open('.travis/series.json'))
    for s in series:
        for file in list(files):
            if file.split('_')[0] == s['prefix']:
                files_data[file] = s['contributor']
                files.remove(file)
    json.dump(files_data, fp=open(".travis/files.json","w"))

def make_statistics():
    stats = {}
    stats["icons"] = len([name for name in os.listdir('svg') if name.endswith('.svg')])
    stats["prs"] = requests.get("https://api.github.com/repos/hackesta/atom-icons/pulls?state=all").json().__len__()
    stats["contributors"] = requests.get("https://api.github.com/repos/hackesta/atom-icons/contributors").json().__len__()
    stats["stargazers"] = requests.get("https://api.github.com/repos/hackesta/atom-icons/stargazers").json().__len__()
    stats["forks"] = requests.get("https://api.github.com/repos/hackesta/atom-icons/forks").json().__len__()
    json.dump(stats,fp=open(".travis/stats.json","w"))

make_linux()
make_windows()
# prep_macOS()
make_readme()
make_listoffiles()
make_statistics()
