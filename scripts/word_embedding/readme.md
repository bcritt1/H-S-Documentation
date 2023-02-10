# Word Embeddings

This directory contains segmented and full workflows for generating a word embedding on Sherlock. Files are as follows:

## [packages.txt](/scripts/word_embedding/packages.txt)

Several lines of shell code to load various modules needed for this process. You will need to copy and past each line separately into your terminal window on Sherlock.

## [requirements.txt](/scripts/word_embedding/requirements.txt)

A small text file loaded used to load necessary packages in python; referenced by the various scripts in this directory. You likely won't need to open this file, but it needs to be in your working directory when you run the python files.

## [tokenizer_to_json.py](/scripts/word_embedding/tokenizer_to_json.py)

A script that tokenizes a directory and converts that python data into a json so it can be used later. Mostly necessary if you are tokenizing a very large corpus and want to separate this step out. Also could be useful if you want the token data for use elsewhere.

## [embedding.py](/scripts/word_embedding/embedding.py)

The second part of the workflow. For use with tokenizer_to_json.py: loads the json from that script back into python and creates a word embedding from it.

## [full_embedding_workflow.py](/scripts/word_embedding/full_embedding_workflow.py)

[tokenizer_to_json.py](/scripts/word_embedding/tokenizer_to_json.py) and [embedding.py](/scripts/word_embedding/embedding.py) combined and streamlined. For those who want to run everything in one fell swoop and don't care about saving intermediary data structures for outside use. Will save the word embedding model after creation.
