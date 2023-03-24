#!/bin/bash

# before running, <ml load imagemagick/7.0.7-2 ghostscript/9.53.2 tesseract/5.1.0
# easily compatible with jobArray scripts

DIR=/Users/bcritt/Documents/pdfs
FILES=/Users/bcritt/Documents/pdfs/*.pdf
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
