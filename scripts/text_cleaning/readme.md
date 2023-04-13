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

### text_cleaning_pipeline.py 

This file performs standard forms of preprocessing for text files including tokenization, lowercasing, punctuation removal, stop word filtering, and lemmatization. The output/input variable (words) remains 
the same throughout the script, so you should be able to comment out any processes you don't desire and still run the script.

###  text_cleaning.sbatch 

Pretty standard sbatch file. Depending on the size of the corpus, "time" and "mem" may need to be tweaked if you are getting "wall time" or "out of memory" errors respectively.

```bash
#!/usr/bin/bash
#SBATCH --job-name=cleaning					# gives the job a descriptive name that slurm will use
#SBATCH --output=/home/users/%u/out/cleaning.%j.out		# the filepath slurm will use for output files. I've configured this so it automatically inserts variables for your username (%u) and the job name (%j) above.
#SBATCH --error=/home/users/%u/err/cleaning.%j.err		# the filepath slurm will use for error files. I've configured this so it automatically inserts variables for your username (%u) and the job name (%j) above.
#SBATCH -p hns							# the partition slurm will use for the job. Here it is hns (humanities and sciences), but you can use other partions (sh_part to see which you can access)
#SBATCH -c 1							# number of cores to use. This should be 1 unless you've rewritten the code to run in parallel
#SBATCH --mem=32GB						# memory to use. 32GB should be plenty, but if you're getting a memory error, you can increase
module load python/3.9.0					# load the most recent version of python on Sherlock
pip3 install nltk						# download nltk
pip install --upgrade certifi					# allow nltk to download files
python3 -m nltk.downloader all					# download nltk files
python3 text_cleaning_pipeline.py				# run the python script
```

#### Notes

[^1]: Scratch systems offer very fast read/write speeds, so they're good for things like I/O. However, data on 
scratch is deleted every 60 days if not modified, so if you use scratch, you'll want to transfer results back to your home directory.
