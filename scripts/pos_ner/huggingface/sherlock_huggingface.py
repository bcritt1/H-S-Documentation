# Import corpus
import os
corpusdir = '/home/users/bcritt/corpus/'
corpus = []
for infile in os.listdir(corpusdir):
    with open(corpusdir+infile, errors='ignore') as fin:
        corpus.append(fin.read())

# Import language models and pipeline elements
from transformers import AutoTokenizer, AutoModelForTokenClassification
tokenizer = AutoTokenizer.from_pretrained("Jean-Baptiste/roberta-large-ner-english")
model = AutoModelForTokenClassification.from_pretrained("Jean-Baptiste/roberta-large-ner-english")


# Process text sample (from wikipedia)
from transformers import pipeline
nlp = pipeline('ner', model=model, tokenizer=tokenizer, aggregation_strategy="simple")
entities = nlp(corpus)

import json
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(str(entities), f, ensure_ascii=False, indent=4)