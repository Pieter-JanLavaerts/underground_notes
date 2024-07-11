#!/bin/sh
pdftk Basic\ Mathematics\ \(Serge\ Lang\)\ \(Z-Library\).pdf cat $(($1 + $3)) output $1.pdf
pdftoppm -png $1.pdf > pages/$1.png
page=$(printf "%03d" $1)
cp pages/$1.png "named/$page $2.png"

