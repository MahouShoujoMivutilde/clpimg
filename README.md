# clpimg

...is a script to copy images to clipboard on linux.

## Why not xclip?

* [unlike xclip](https://github.com/astrand/xclip/issues/43), does not care about
image size within reason (chromium did not like 100mb+ Hubble images, however telegram-desktop was just fine, ~10-15mb works on both, but it might take a few second to process)
* thanks to PyQt, automatically provides a lot of targets for an image (see below)

```
> xclip -sel clip -t image/jpeg image.jpeg
```

```
> xclip -sel clip -t TARGETS -o
TARGETS
image/jpeg
```

```
> clpimg.py image.jpeg
```

```
> xclip -sel clip -t TARGETS -o
application/x-qt-image
image/png
image/bmp
image/cur
image/icns
image/ico
image/jp2
image/jpeg
image/jpg
image/pbm
BITMAP
image/pgm
image/ppm
PIXMAP
image/tif
image/tiff
image/wbmp
image/webp
image/xbm
image/xpm
TARGETS
MULTIPLE
TIMESTAMP
SAVE_TARGETS
```

## Installation

```
git clone https://github.com/MahouShoujoMivutilde/clpimg
cd clpimg
make install
```

Don't forget to install PyQt5.

## Usage

```
clpimg.py is a simple script to copy images to clipboard

usage:
    clpimg.py image.png - copy to clipboard
    clpimg.py -s        - show supported image formats

inspired by:
    https://github.com/astrand/xclip/issues/43 (why)
    https://github.com/m13253/linux-copy-image (how)
```


## Tips

notify-send supports images, so you could wrap this script in something like

```
#!/usr/bin/env sh

thumb="$XDG_RUNTIME_DIR/thumb.jpg"
convert -thumbnail x150 -unsharp 0x.5 "$1" "$thumb" &

clpimg.py "$1"
echo -n "$(realpath "$1")" | xclip

wait
notify-send "clipped image" "$(basename "$1")" -i "$thumb"
```
...to get

![](https://i.imgur.com/1DnThks.jpg)

## Downsides

* does not support reading images from stdin (yet)
* does not like wrong icc profiles (just strip them with `mogrify`)
