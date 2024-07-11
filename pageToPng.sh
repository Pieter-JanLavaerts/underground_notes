#!/bin/bash
mkdir -p pdfpages
mkdir -p pngpages
mkdir -p namedpngs
echo generate page png $1 $2 $3 $4
pdftk $1 cat $(($2 + $4)) output pdfpages/$2.pdf
pdftoppm -png pdfpages/$2.pdf > pngpages/$2.png
page=$(printf "%03d" $2)
cp pngpages/$2.png "namedpngs/$page $3.png"

