import nltk
import ssl
import re
import os
import pandas as pd
from nltk.tokenize import sent_tokenize
nltk.download('punkt')


# This may or may not be necessary for you. Gives python permission to access the internet so we can download 
libraries.
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# Read in a directory of txt files as the corpus using the os library.
corpusdir = '/scratch/users/bcritt/corpus/'
corpus = []
for infile in os.listdir(corpusdir):
    with open(corpusdir+infile, errors='ignore') as fin:
        corpus.append(fin.read())

# convert corpus to string instead of list
sorpus = str(corpus)

# this particular corpus has a multitude of "\n's" due to its original encoding. This removes them; code can be 
modified to remove other text artifacts before tokenizing.

sorpus = re.sub(r'(\\n[ \t]*)+', '', sorpus)

# could also split into words (or paragraphs, etc.)
#words = word_tokenize(sorpus)

# Call the function
sentences = sent_tokenize(sorpus)

df = pd.DataFrame(sentences)
df.to_csv('/scratch/users/bcritt/outputs/sentences.csv')
