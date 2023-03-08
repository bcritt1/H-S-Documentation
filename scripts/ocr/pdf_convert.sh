#!/bin/bash

#brew install imagemagick
#brew install ghostscript
#brew install tesseract

FILES=/Users/bcritt/Documents/pdfs/*.pdf
for f in $FILES;
do
	tiff=${f%.*}.tiff
	convert -density 400 $f -depth 8 -strip -background white -alpha off $tiff
	ocr=${f%.*}_ocr
	tesseract $tiff $ocr
done

mkdir /Users/bcritt/Documents/pdfs/"ocr"
mkdir /Users/bcritt/Documents/pdfs/"tiff"
mv /Users/bcritt/Documents/pdfs/*_ocr.txt /Users/bcritt/Documents/pdfs/ocr
mv /Users/bcritt/Documents/pdfs/*.tiff /Users/bcritt/Documents/pdfs/tiff