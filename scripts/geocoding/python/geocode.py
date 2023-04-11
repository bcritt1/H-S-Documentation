# Import libraries
import ssl
import urllib
import requests
import pandas as pd
import os
import spacy
import time

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# Read in corpus from scratch
user = os.getenv('USER')
corpusdir = '/scratch/users/{}/corpus/.format(user)'
corpus = []
for infile in os.listdir(corpusdir):
    with open(corpusdir+infile, errors='ignore') as fin:
        corpus.append(fin.read())

# Load language model from spacy. This can be changed to other languages. See https://spacy.io/usage/models/
nlp = spacy.load("en_core_web_sm")
# May need to increase length for large corpora. len(corpus) in python to find length.
nlp.max_length = 5000000
# Convert corpus to string to make spacy happy
sorpus = str(corpus)
# Perform nlp on sorpus
doc = nlp(sorpus)
# Label entities types in doc
ner_output = []
for token in doc:
    ner_output.append(token.text + token.ent_type_)
# Convert to dataframe to clean
df = pd.DataFrame(ner_output)
# Retain only entities labeled as geopolitical entities. Can change string to retain people or other types.
places = df.loc[df[0].str.contains("GPE")]
places[0] = places[0].str.replace('GPE','')
#places = places.replace('GPE','')

# Perform the geocode with Nominatum. Function adapted from https://www.natasshaselvaraj.com/a-step-by-step-guide-on-geocoding-in-python/

def geocode(locality):
    url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(locality) +'?format=json'
    response = requests.get(url).json()
    time.sleep(1)
    if(len(response)!=0):
        return(response[0]['lat'], response[0]['lon'])
    else:
        return('-1')

places['geocoded'] = places[0].apply(geocode)

places.to_csv('/scratch/users/{}/outputs/places.csv'.format(user))
