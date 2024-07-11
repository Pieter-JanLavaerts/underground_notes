#!/bin/bash
echo generate page png $1 $2 $3 $4
pdftk $1 cat $(($2 + $4)) output $2.pdf
pdftoppm -png $2.pdf > pages/$2.png
page=$(printf "%03d" $2)
mkdir -p pages
mkdir -p named
cp pages/$2.png "named/$page $3.png"

