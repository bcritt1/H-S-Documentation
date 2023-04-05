#! /usr/bin/bash

ml system subversion/1.12.2
svn export https://github.com/bcritt1/H-S-Documentation/trunk/scripts/geocoding/python/ geocoding
ml python/3.9.0
pip3 install --user -r ./geocoding/requirements.txt
python3 -m spacy download en_core_web_sm
