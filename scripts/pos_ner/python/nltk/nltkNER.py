# import general libraries
import pandas as pd
import ssl
import os
import json
import re

# give nltk permission to download data in python
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# download language models in nltk
import nltk
from nltk.tokenize import word_tokenize

# Read in a directory of txt files as the corpus using the os library.

user = os.getenv('USER')
corpusdir = '/scratch/users/{}/corpus/'.format(user)
corpus = []
for infile in os.listdir(corpusdir):
    with open(corpusdir+infile, errors='ignore') as fin:
        corpus.append(fin.read())

# convert corpus to string instead of list as required by nltk tokenizer
sorpus = str(corpus)

# this particular corpus has a multitude of "\n's" due to its original encoding. This removes them; code can be modified to remove other text artifacts before tokenizing.
sorpus = re.sub(r'(\\n[ \t]*)+', '', sorpus)

# tokenize into words
words = word_tokenize(sorpus)

# pos tag sentences
pos = nltk.pos_tag(words)

# Do named entity tagging of POS text
ne = nltk.ne_chunk(pos)

# can convert pos to df and write out as csv
df = pd.DataFrame(pos)
df.to_csv('/scratch/users/{}/outputs/pos.csv'.format(user))

# because of uneven data structure, better to export ne as json
with open('/scratch/users/{}/outputs/data.json'.format(user), 'w', encoding='utf-8') as f:
    json.dump(ne, f, ensure_ascii=False, indent=4)

