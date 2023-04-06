#!/bin/bash

DIR=/home/users/bcritt/pdfs/
FILES=/home/users/bcritt/pdfs/*.pdf
for f in $FILES;
do
  	tiff=${f%.*}.tiff
        convert -density 400 $f -depth 8 -strip -background white -alpha off $tiff
        ocr=${f%.*}_ocr
        tesseract $tiff $ocr
done

mkdir $DIR"/ocr"
mkdir $DIR"/tiff"
mv $DIR/*_ocr.txt $DIR/ocr
mv $DIR/*.tiff $DIR/tiff