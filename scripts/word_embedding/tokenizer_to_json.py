#HOW IS FIRST BIT INTEGRATED?

#Download necessary libraries collected in a txt file and added here piecemeal as needed. 
#It would be cleaner to have everything in the text file.
!pip3 install -r requirements1.txt #done in shell
!pip install --upgrade certifi 
!python -m nltk.downloader all

#all this in script?
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
corpusdir = '/Users/brad/Documents/GitHub/Emerson/works_split_datamunging/'
corpus = []
for infile in os.listdir(corpusdir):
    with open(corpusdir+infile, errors='ignore') as fin:
        corpus.append(fin.read())

#define the tokenizer NLTK (Natural Language Toolkit) will use
tokenizer = TreebankWordTokenizer()

#Create a variable "sentences", defined as the output of the sent_tokenize function being run on the corpus list.
#See that the sentence is now a list of lists, with each item a sentence in the corpus.
sentences = sent_tokenize(corpus[0])

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
