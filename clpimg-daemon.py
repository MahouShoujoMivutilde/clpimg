#!/usr/bin/env python3

from PyQt5 import QtGui
import sys

if __name__ == '__main__':
    app = QtGui.QGuiApplication(sys.argv)

    reader = QtGui.QImageReader(sys.argv[1])
    image = reader.read()

    clipboard = app.clipboard()
    clipboard.setImage(image)

    # important. let it wait for new clips (text & etc)
    # and only THEN die. otherwise on-the-fly conversion
    # to compatible TARGET will not work
    clipboard.dataChanged.connect(app.exit)

    app.exec()
