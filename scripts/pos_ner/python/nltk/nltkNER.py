# import general libraries
import pandas as pd
import ssl
import os
import json

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
from nltk.tokenize.treebank import TreebankWordTokenizer
nltk.download('punkt')

# Read in a directory of txt files as the corpus using the os library.

user = os.getenv('USER')
corpusdir = '/scratch/users/{}/corpus/'.format(user)
corpus = []
for infile in os.listdir(corpusdir):
    with open(corpusdir+infile, errors='ignore') as fin:
        corpus.append(fin.read())

#define the tokenizer NLTK (Natural Language Toolkit) will use
tokenizer = TreebankWordTokenizer()

# function to word tokenize corpus
def make_sentences(list_txt):
    all_txt = []
    for txt in list_txt:
        lower_txt = txt.lower()
        sentences = word_tokenize(lower_txt)
        #sentences = [tokenizer.tokenize(sent) for sent in sentences]
        all_txt += sentences
        print(len(sentences))  
    return all_txt

# call function
sentences = make_sentences(corpus)

# pos tag sentences
pos = nltk.pos_tag(sentences)

# Do named entity tagging of POS text
ne = nltk.ne_chunk(pos)

# can convert pos to df and write out as csv
df = pd.DataFrame(pos)
df.to_csv('/scratch/users/{}/outputs/pos.csv'.format(user))

# because of uneven data structure, better to export ne as json
with open('/scratch/users/{}/outputs/data.json'.format(user), 'w', encoding='utf-8') as f:
    json.dump(ne, f, ensure_ascii=False, indent=4)

