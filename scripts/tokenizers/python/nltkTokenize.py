import nltk
import ssl
import os
import pandas as pd
from nltk.tokenize import sent_tokenize
from nltk.tokenize.treebank import TreebankWordTokenizer
nltk.download('punkt')


# This may or may not be necessary for you. Gives python permission to access the internet so we can download libraries.
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

# Function to tokenize the corpus into sentences and then into words, maintaining sentence-level information. This format is required for gensim word embedding downstream
def make_sentences(list_txt):
    all_txt = []
    for txt in list_txt:
        lower_txt = txt.lower()
        sentences = sent_tokenize(lower_txt)
        sentences = [tokenizer.tokenize(sent) for sent in sentences]
        all_txt += sentences
        print(len(sentences))  
    return all_txt

# Call the function
sentences = make_sentences(corpus)

df = pd.DataFrame(sentences)
df.to_csv('/scratch/users/bcritt/outputs/sentences.csv')
