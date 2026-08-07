#!/bin/bash

# OpenDMX Studio macOS App Builder

python3 -m pip install pyinstaller

pyinstaller \
 --windowed \
 --name OpenDMXStudio \
 --icon icon.icns \
 main.py

mkdir -p release
cp -r dist/OpenDMXStudio.app release/

echo "OpenDMXStudio.app created in release folder"
