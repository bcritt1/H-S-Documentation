# Sherlock Script Repository

This is a collection of scripts made to run on Stanford's [Sherlock](https://www.sherlock.stanford.edu/) cluster. In general, the scripts are implementations of humanities-focused computational 
methodologies. They primarily focus on text processing and analysis, but also extend to mapping and other processes. Further support is planned for visualization pipelines. If you'd like to request support 
for other methodologies, please contact [Brad Rittenhouse](mailto:bcritt@stanford.edu). You can find a quick gloss of the different sub-repos and their uses below:

## Geocoding

Geocoding describes the practice of assigning specific coordinates to places, often for the purpose of mapping. In the humanities, one must often first computationally process text to identify and extract 
places so they can then be geocoded. This repo contains a workflow that starts with plain-text documents and ends with a structured .csv of places and their coordinates.

## OCR

In order for computers to work on text, the text must be rendered in a format that is machine-readable. While we can look at a paper page or even a pdf and read the text, computers need text in a format 
known as plain-text. The scripts in this repo take an input of pdf files and renders them as plain-text .txt files so a computer can read and eventually process them. This process is known as Optical 
Character Recognition, or OCR. With some knowledge, this pipeline could be tweaked to deal with image files as well. There are additional scripts for the parallel processing of files as well, so large collections can be OCR'ed in an expedient manner.

## Parallel Processing

Parallel processing generally refers to running computational processes in parallel, at the same time, on different pieces of hardware, as opposed to in sequence on the same piece of hardware. As you can 
imagine, reading in 100 files on 100 computers all at the same time will go a lot faster than reading in 100 files, one after another, on just 1 computer. This repo contains simple bash and slurm scripts 
that parallelize file input and the OCR library above.

## POS and NER

Parts of Speech (POS) analysis and Named Entity Recognition (NER) are two common text analysis processes. The former reads in text and attempts to assign a part of speech to every word, while the latter 
identifies and categorizes named entities, which broadly overlaps with the linguistic concept of proper nouns. This type of metadata creation forms the foundation for higher-level analysis of natural 
language, bridging the gap, in some ways, between a computer's understanding of language and our own.

## Text Cleaning

This repo contains python scripts that run various common text cleaning techniques on plain-text documents. An understanding of your workflow is recommended before using this repo, as some other processes 
here (like the R tokenizer script) apply text cleaning techniques already.

## TF-IDF

Term Frequency, Inverse Document Frequency (TF-IDF) basically compares the frequency of a term's usage in one document versus the frequency of its use in a collection of documents. Basically, this gives a 
measure of how unique a term is to a specific document and can be used to infer what makes a document or set of documents unique. This repo includes a python implementation of TF-IDF. 

## Tokenizers

Another fundamental text processing technique. Tokenizing applies various heuristics to text in order to determine what a word, or token, is. Because computers don't understand this innately, we must give 
them parameters, through tokenizers, to do so and thus understand language in a more human manner, ie. as a collection of words. Tokens can also be understood as sentences, paragraphs, etc. (which in turn 
influence the unit of thought a study engages); options for doing those types of tokenization are provided as well.

## Word Embedding

Word embeddings describe words in a corpus as a vectors in n-dimensional space using neural net models. In a human sense, they give some sense of the syntactic usage of words in a given corpus. This repo 
includes word2vec implementations of word embeddings in R and python.
