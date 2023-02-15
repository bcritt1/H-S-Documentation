# Read in a directory of txt files as the corpus using the os library.

import os
corpusdir = '/Users/bcritt/Documents/StanfordProjects/Corpora/Emerson/emerson/'
corpus = []
for infile in os.listdir(corpusdir):
    with open(corpusdir+infile, errors='ignore') as fin:
        corpus.append(fin.read())

# This may or may not be necessary for you. Gives python permission to access the internet so we can download libraries.

import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

!pip3 install nltk
import nltk
nltk.download()

# could also split into words (or paragraphs, etc.)
from nltk.tokenize import word_tokenize
words = word_tokenize(corpus[0])

# convert to lower case
words = [w.lower() for w in words]

# remove punctuation from each word
import string
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in words]
# remove remaining tokens that are not alphabetic
words = [word for word in stripped if word.isalpha()]

# filter out stop words
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
words = [w for w in words if not w in stop_words]

# stemming of words, some of these variables may change depending on whether you've done 
#from nltk.stem.porter import PorterStemmer
#porter = PorterStemmer()
#stemmed = [porter.stem(word) for word in words]

# lemmatizing words
wl = nltk.WordNetLemmatizer()
words = [wl.lemmatize(word) for word in words]