import os
import json
import requests
from xml.dom import minidom

errors = []

def raise_errors():
    url = "https://api.github.com/repos/hackesta/atom-icons/issues/"+os.environ.TRAVIS_PULL_REQUEST+"/comments"
    if errors.__len__() > 0:
        for i in range(0, errors.__len__() -1):
            errors[i] = errors[i] + " \n "
        data = {
        "body": "".join(errors)
        }
        print(data)
        requests.post(url,data)

def list_files():
    url = "https://api.github.com/repos/hackesta/atom-icons/commits/" + os.environ.TRAVIS_PULL_REQUEST_SHA + "?access_token=" + os.environ.GH_TOKEN
    data = requests.get(url).json()
    files = []
    for file in data['files']:
        files.append(file['filename'])
    return files


def height_width_test():
    for file in list_files():
        doc = minidom.parse(file)
        svg = doc.getElementsByTagName('svg')[0]
        if svg.hasAttribute('height') or svg.hasAttribute('width'):
            errors.append(file + " has height and/or width attributes")

height_width_test()
raise_errors()
