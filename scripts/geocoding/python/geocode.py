# This may or may not be necessary for you. Gives python permission to access the internet so we can download libraries.

import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

#import relevant nltk data, functions

import nltk
import pandas as pd
from nltk import word_tokenize,pos_tag
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

# Read in a directory of txt files as the corpus using the os library. It's most efficient to locate this in scratch. My scratch path is below: you will need to adjust to reflect your path.

import os
corpusdir = '/scratch/users/bcritt/corpus/'
corpus = []
for infile in os.listdir(corpusdir):
    with open(corpusdir+infile, errors='ignore') as fin:
        corpus.append(fin.read())

# NLTK implementation of tokenize, pos tag, and ner tag corpus. Not used in current workflow.

#ne_tree = nltk.ne_chunk(pos_tag(word_tokenize(corpus[0])))
#print(ne_tree)

#optional tree illustration of NER

#!pip3 install svgling
#ne_tree

#spacy implementation of NER
!pip3 install spacy && python3 -m spacy download en_core_web_sm
import spacy 
nlp = spacy.load("en_core_web_sm")

doc = nlp(corpus[0])
# Perform NER on docs, outputing the tokens and entity types
ner_output = []
for token in doc:
    ner_output.append(token.text + token.ent_type_)

# Filter NER data to only include things labeled as "GPE" (geopolitical entities)
df = pd.DataFrame(ner_output)
places = df.loc[df[0].str.contains("GPE")]
places[0] = places[0].str.replace('GPE','')
"""

# Geocode GPE Data with Nominatum

!pip3 install urllib
!pip3 install requests
import urllib
import requests

def geocode2(locality):
    url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(locality) +'?format=json'
    response = requests.get(url).json()
    if(len(response)!=0):
        return(response[0]['lat'], response[0]['lon'])
    else:
        return('-1')

places['geocoded'] = places[0].apply(geocode2)

# Write out data to csv in scratch for efficiency.
places.to_csv('/scratch/users/bcritt/output/places.csv')
