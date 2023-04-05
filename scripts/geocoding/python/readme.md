# Python Geocoding Workflow

Below are three simple files that execute spaCy's [NER](https://spacy.io/api/entityrecognizer/) functionality on a group of files and use that output as an input for geocoding in [Nominatum](https://nominatim.org/).[^1] 

# File Overview

The files consist of:

1. [packages.sh](/scripts/geocoding/python/packages.sh): A shell script that sets up your environment, loading the correct version of python, some dependencies, and installing the python packages in requirements.txt.
2. [requirements.txt](/scripts/geocoding/python/requirements.txt): You shouldn't need to touch this. Simply tells python which packages it needs to install to run geocoding.py.
3. [geocoding.py](/scripts/geocoding/python/geocoding.py): Runs spaCy and Nominatum, outputing a .csv file with all the places (geopolitical entities) in your corpus and their lat/long coordinates.

# Usage instructions

1. ssh into sherlock with the syntax 
'''
ssh yourSUNetID@sherlock.stanford.edu
'''
2. Once you are logged in, you'll want to have access to these files, which you can get by using the command
'''
git clone
'''

[^1] Google's geocoding API may offer better accuracy, but it can also rack up charges fast on large datasets. Nominatum is free and open-source.
