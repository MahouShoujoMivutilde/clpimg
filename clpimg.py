#!/usr/bin/env python3

from PyQt5 import QtCore, QtGui
from os import path
import sys
import re
import subprocess as sp

DESC = f"""
{path.basename(__file__)} is a simple script to copy images to clipboard

usage:
    {path.basename(__file__)} image.png - copy to clipboard
    {path.basename(__file__)} -s        - show supported image formats

inspired by:
    https://github.com/astrand/xclip/issues/43 (why)
    https://github.com/m13253/linux-copy-image (how)
"""

def list_supported():
    return sorted(re.findall(
        r"b'([a-z]+)'",
        str(QtGui.QImageReader.supportedImageFormats())
    ))


if __name__ == '__main__':
    app = QtGui.QGuiApplication(sys.argv)

    if '-h' in sys.argv or '--help' in sys.argv:
        print(DESC)
        sys.exit(0)

    if '-s' in sys.argv:
        print('\n'.join(list_supported()))
        sys.exit(0)

    assert len(sys.argv) == 2, f'you forgot an image, see {path.basename(__file__)} -h'
    assert path.isfile(sys.argv[1]), 'file does not exist'

    reader = QtGui.QImageReader(sys.argv[1])
    assert reader.canRead(), f'failed to read image - {reader.errorString()}'
    sp.Popen(['clpimg-daemon.py', sys.argv[1]])
