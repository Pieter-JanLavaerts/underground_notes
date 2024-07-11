#!/bin/bash
book="Basic Mathematics (Serge Lang).pdf"
pdftk $book cat $(($1 + $3)) output $1.pdf
pdftoppm -png $1.pdf > pages/$1.png
page=$(printf "%03d" $1)
mkdir pages
cp pages/$1.png "named/$page $2.png"

