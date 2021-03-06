#!/usr/bin/env bash

sudo apt-get install -qq libpulse-dev

# Install PyQt5 for Python 3
sudo apt-get install -qq python3-pyqt5 python3-pyqt5.qtopengl

echo 'QtWidgets'
python3 -c 'from PyQt5 import QtWidgets'

echo 'QtCore'
python3 -c 'from PyQt5 import QtCore'

echo 'QtTest'
python3 -c 'from PyQt5 import QtTest'

echo 'QtGui'
python3 -c 'from PyQt5 import QtGui'

echo 'Qt'
python3 -c 'from PyQt5 import Qt'

echo 'QtSvg'
python3 -c 'from PyQt5 import QtSvg'

echo 'QtMultimedia'
python3 -c 'from PyQt5 import QtMultimedia'

echo 'Ended'