# Text Cleaning Workflow

This repo contains two simple files that executes many forms of NLTK's text cleaning functionality on a directory of txt files.

## File Overview

The files consist of:

1. [text_cleaning_pipeline.py](/scripts/tfidf/text_cleaning_pipeline.py): Runs tfidf on a corpus, exporting a .csv organized by input files.
2. [text_cleaning.sbatch](/scripts/tfidf/text_cleaning.sbatch): Creates a batch job for text_cleaning_pipeline.py.

## Usage instructions

1. ssh into sherlock with the syntax: 
```
ssh yourSUNetID@sherlock.stanford.edu
```

2. Once you are logged in, you'll want to have access to these files, which you can get with a couple simple commands. First, we need to install a program called subversion:
```
ml system subversion
```
and use that program to download the files:
```
svn export https://github.com/bcritt1/H-S-Documentation/trunk/scripts/text_cleaning/ text_cleaning
```
This will create a directory in your home space on Sherlock called "text_cleaning" with all the files in this 
repository. You'll want to
```
ml purge
```
after this as subversion tends to interfere with python dependencies.

3. Once you have the files, you'll use packages.sh to set up your environment. First, let's move into our new directory::
```
cd text_cleaning/
```

4. At this point, you're basically ready to run the script.
```
sbatch text_cleaning_pipeline.sbatch
```
When it finishes running, you should see your output as a .csv file in outputs/text_cleaning in scratch. This data 
can then be 
used as an input for some other process.

## Code Explanation

1. text_cleaning_pipeline.py: This file performs standard forms of preprocessing for text files including tokenization, lowercasing, punctuation removal, stop word filtering, and lemmatization. The output/input variable (words) remains 
the same throughout the script, so you should be able to comment out any processes you don't desire and still run the script.
2. text_cleaning.sbatch: Pretty standard sbatch file. Depending on the size of the corpus, "time" and "mem" may need to be tweaked if you are getting "wall time" or "out of memory" errors respectively.

### Notes

[^1]: Scratch systems offer very fast read/write speeds, so they're good for things like I/O. However, data on 
scratch is deleted every 60 days if not modified, so if you use scratch, you'll want to transfer results back to your home directory.
