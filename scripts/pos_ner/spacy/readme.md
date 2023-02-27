# Overview

The files in this repo will allow you to perform tokenization and NER of a corpus with spaCy. 

How to use:

1. Transfer all files to your home directory on Sherlock, including your corpus files. See [here](https://www.sherlock.stanford.edu/docs/storage/data-transfer/#ssh-based-protocols) for more on files transfer.
2. Change corpusdir in [sherlock_spacy_tokenize_pos_ner.py](/scripts/pos_ner/spacy/sherlock_spacy_tokenize_pos_ner.py) to the path to your text files
3. Input the lines from [packages.txt](/scripts/pos_ner/spacy/packages.txt) in the terminal
4. Run [spacy.sh](/scripts/pos_ner/spacy/spacy.sh) with ```sbatch spacy.sh```.
5. The script will output two .csv files: pos and ner. The first will be an output of the parts of speech of your corpus tokens and the second will be just the named entities. The ner function builds on the pos function, so it can be turned off if ner is not desired.
