#!/bin/sh

rm -Rf ./build/*
rm -Rf ./dist/*

/usr/bin/env python setup.py py2app

mkdir -p Launcher_v000
rm -Rf ./Launcher_v000/Launcher.app

cp -p ./LICENSE ./Launcher_v000/
cp -p ./README.md ./Launcher_v000/

mv ./dist/Launcher.app ./Launcher_v000/

# markdown README.md >README.html
markdown_py -o html5 -f README.html README.md
cp README.html  ./Launcher_v000/


# finally re-create the development version

rm -Rf ./build/*
rm -Rf ./dist/*

/usr/bin/env python setup.py py2app -A


