# Atom App Icons  
![Travis CI](https://travis-ci.org/HackeSta/atom-icons.svg?branch=master)  
A project for custom [Atom](https://atom.io) Icons. All Rights Reserved with [Github](https://github.com) and the respective owners of the themes I am using.
Inspired from [vscode-icons](https://github.com/dhanishgajjar/vscode-icons), a similar project for [Visual Studio Code](https://code.visualstudio.com/) by [@dhanishgajjar](https://github.com/dhanishgajjar/)

## Available Icons

## Additional Resources
* The Flags of Countries was generated using [Atom Flag Icons Generator](https://gist.github.com/haideralipunjabi/b072aa4a8e28a78392e7e83b18575d2b)
## How to Contribute

### Making Icons
* You only need to submit an SVG file per icon, otehr formats will be generated using CI.
* You may use [icon.svg](icon.svg) or any other SVG file from the repository as a base/reference.
* Make sure the `width` & `height` attributes are removed from the SVG, they cause problems when resizing the SVG into other formats.
* Ideal size for the icon is `512x512`  

### Naming Guidelines
* If you are submitting the icon as part of a series, make sure to name it like `seriesname_iconname.svg`. No other `underscore (_)` should be used.
* If you are submitting the icon without it being a part of any series, make sure to name it without any `underscore (_)`.

### Notes
* You don't need to edit the README.md, as it is auto generated using CI.


## How to Install

**Mac OS:**

Download [Image2Icon](http://www.img2icnsapp.com/) app. Drop the  `svg` as source and export a `ICNS` file.

Easiest way to change the icons is by using https://freemacsoft.net/liteicon/. Just Drag and Drop the custom icon and hit `Apply Changes`.

Copy the `.icns` file you'd like to use. Find VS Code in your Applications folder, right click the icon and select `Get Info`. Click the icon in the top right corner so that a blue highlight appears around it. `⌘ + V` to paste the new icon in. It may take a few restarts of VS Code for the icon to take.

If for some reason that doesn't work, then dragging the `.icns` to the icon (in the top left) of the info pane, until you see the green plus sign and then dropping it works.

**Windows:**

Right click on the shortcut App Icon, select properties and then shortcut tab and then `change icon` button.

**Linux:**  

It is distribution dependent. Google how to do it. If you can't, open an Issue, or [mail me](mailto:haideralipunjabi@hackesta.org)
