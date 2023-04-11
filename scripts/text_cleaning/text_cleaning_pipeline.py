import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import ssl
import re
import string
import pandas as pd

# Read in a directory of txt files as the corpus using the os library.
user = os.getenv('USER')
corpusdir = '/scratch/{}/bcritt/corpus/'.format(user)
corpus = []
for infile in os.listdir(corpusdir):
    with open(corpusdir+infile, errors='ignore') as fin:
        corpus.append(fin.read())

# This may or may not be necessary for you. Gives python permission to access the internet so we can download libraries.

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# convert corpus to string instead of list
sorpus = str(corpus)

# this particular corpus has a multitude of "\n's" due to its original encoding. This removes them; code can be modified to remove other text artifacts before tokenizing.

sorpus = re.sub(r'(\\n[ \t]*)+', '', sorpus)
sorpus

# could also split into words (or paragraphs, etc.)
words = word_tokenize(sorpus)

# convert to lower case
words = [w.lower() for w in words]

# remove punctuation from each word
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in words]
# remove remaining tokens that are not alphabetic
words = [word for word in stripped if word.isalpha()]

# filter out stop words
stop_words = set(stopwords.words('english'))
words = [w for w in words if not w in stop_words]

# stemming of words, some of these variables may change depending on whether you've done 
#from nltk.stem.porter import PorterStemmer
#porter = PorterStemmer()
#stemmed = [porter.stem(word) for word in words]

# lemmatizing words
wl = nltk.WordNetLemmatizer()
words = [wl.lemmatize(word) for word in words]

# can convert pos to df and write out as csv
df = pd.DataFrame(words)
df.to_csv('/scratch/users/{}/outputs/stems.csv'.format(user))
