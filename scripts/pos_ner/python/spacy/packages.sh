# shell script to install spaCy language model. Model can be changed depending on user's need

ml load python/3.9.0
pip3 install spacy
python3 -m spacy download en_core_web_sm
