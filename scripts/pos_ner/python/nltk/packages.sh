#!/bin/bash

ml load python/3.9.0
pip3 install nltk
pip install --upgrade certifi
python3 -m nltk.downloader all
