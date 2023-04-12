# import libraries
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize.treebank import TreebankWordTokenizer
nltk.download('punkt')


# This may or may not be necessary for you. Gives python permission to access the internet so we can download libraries.
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# Read in a directory of txt files as the corpus using the os library.
import os
user = os.getenv('USER')
corpusdir = '/scratch/users/{}/corpus/'.format(user)
corpus = []
for infile in os.listdir(corpusdir):
    with open(corpusdir+infile, errors='ignore') as fin:
        corpus.append(fin.read())

#define the tokenizer NLTK (Natural Language Toolkit) will use
tokenizer = TreebankWordTokenizer()

# Function to tokenize the corpus into sentences and then into words, maintaining sentence-level information. This format is required for gensim word vectors downstream
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

# Optional exit point, export to json
#import json
#with open('data.json', 'w', encoding='utf-8') as f:
#    json.dump(sentences, f, ensure_ascii=False, indent=4)

#Reimport with:
#with open("data.json", "r") as read_file:
#    data = json.load(read_file)

import gensim

"""The syntax of the next statement is as follows:

model =: Assigning our model to the variable "model" via Python syntax.
gensim.models.Word2Vec: Calling the gensim function Word2Vec to tell it which word embedding algorithm to use. Others include FastText, Doc2Vec, and Stanford's GLoVe.
sentences: Telling the function what dataset to run on. Remember "sentences" is a sentence tokenized Python list of our corpus.
min_count: An option telling gensim the minimum times a word should occur in the corpus to be incorporated in the model. We want it to include all words so we set this to 0. If you have a concern that unique words will skew your model, you can set this higher to include only words that appear more frequently.
vector_size=100: The number of coordinates gensim will use to describe each word vector. The model will be more accurate the higher this number is, but it will also take more time to compute.
sg=1: Sets the method for the embedding. 1 is skip-gram, 0 is CBOW. Skip-gram is thought to be more accurate on smaller corpora, so we will use that."""

#Create model according to paramaters above. "sentences" is the output of the tokenizer.py script, reimported from json as below:
model = gensim.models.Word2Vec(sentences, min_count=0, vector_size=100, sg = 1)

#Save the model locally so we don't need to retrain it every time. 
model.save('/scratch/users/{}/outputs/my_model'.format(user))

#If you save your model, in the future you can start at this line, loading in the model from disk. There are lots of ways to explore the embedding: 
#https://radimrehurek.com/gensim/auto_examples/tutorials/run_word2vec.html#sphx-glr-auto-examples-tutorials-run-word2vec-py. This is probably done best with a Sherlock [interactive 
#session](https://www.sherlock.stanford.edu/docs/user-guide/running-jobs/#interactive-jobs) or [OnDemand](https://login.sherlock.stanford.edu/)
 #my_model = gensim.models.Word2Vec.load('/scratch/users/{}/outputs/my_model'.format(user)) 
