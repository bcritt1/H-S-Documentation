#load model, increase max str length for large corpora. Can check length with len(corpus)

import spacy 
nlp = spacy.load("en_core_web_sm")
nlp.max_length = 5000000

import os
corpusdir = '/Users/bcritt/Documents/StanfordProjects/Corpora/Emerson/emerson/'
corpus = []
for infile in os.listdir(corpusdir):
    with open(corpusdir+infile, errors='ignore') as fin:
        corpus.append(fin.read())

# convert corpus to string for use with spacy
sorpus = str(corpus)

# tag text with POS info
doc = nlp(sorpus)
pos_output = []
for token in doc:
    pos_output.append(token.text + " " + token.tag_ + " " + token.pos_)

# convert to pd df for analysis
import pandas as pd

pos_df = pd.DataFrame(pos_output)
pos_df[['word','pos_tag', 'pos']] = pos_df[0].str.split(" ", 3, expand=True)
pos_df = pos_df.drop(pos_df.columns[0], axis=1)

#write out as csv for later use
pos_df.to_csv('pos.csv')

# tag sorpus with NER data
doc = nlp(sorpus)
ner_output = []
for token in doc:
    ner_output.append(token.text + " " + token.ent_type_)

# convert output to df for easier use
ner_df = pd.DataFrame(ner_output)
ner_df[['word','entity_type']] = ner_df[0].str.split(" ", 2, expand=True)
ner_df = ner_df.drop(ner_df.columns[0], axis=1)

# save only rows with entity info
import numpy as np

ner_df['entity_type'].replace('', np.nan, inplace=True)
ner_df.dropna(subset=['entity_type'], inplace=True)

#write out as csv for later use
ner_df.to_csv('ner.csv')