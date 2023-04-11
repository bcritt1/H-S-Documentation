# NLTK NER Workflow

This repo contains two simple files that execute [nltk's](https://www.nltk.org/index.html) parts of speech and named entity taggers on a directory of .txt files.

## File Overview

The files consist of:

1. [nltkNER.py](/scripts/pos_ner/python/nltk/nltkNER.py): Runs ntlk on a corpus, outputing a .csv file with 
POS and .json file with NER for all the words in your corpus.
2. [nltkNER.sbatch](/scripts/pos_ner/python/nltk/nltkNER.sbatch): Creates a batch job for nltkNER.py.

## Usage instructions

### Setting up and Connecting to Sherlock

1. Before we log onto Sherlock, let's make sure we're going to have everything we need there and move inputs/corpus onto Sherlock. For info on transferring data to Sherlock, see:
[https://www.sherlock.stanford.edu/docs/storage/data-transfer/](https://www.sherlock.stanford.edu/docs/storage/data-transfer/). [rsync](https://www.sherlock.stanford.edu/docs/storage/data-transfer/#rsync) is probably the best program for
this, but if you prefer another, go with that. For rsync, you'd use the command 
``` 
rsync -a ~/path/to/local/data yourSUNetid@login.sherlock.stanford.edu:/scratch/users/$USER/corpus/
```
You'll need to tweak the local path because I don't know where your files are located, but the remote path (after the ":") should work fine to get your corpus into scratch, a fast storage system where it's best to do file 
reading/writing.

2. Now we can log onto Sherlock using ssh in the Terminal program on Mac[^1]. with the syntax: 
```
ssh yourSUNetID@sherlock.stanford.edu
```
### File Management

3. Once you are logged in, you'll want to have access to these files, which you can get with a couple simple commands. First, we need to install a program called subversion:
```
ml system subversion
```
and use that program to download the files:
```
svn export https://github.com/bcritt1/H-S-Documentation/trunk/scripts/pos_ner/python/nltk/ nltk
```
This will create a directory in your home space on Sherlock called "nltk" with all the files in this repository.

Once you have the directory--you can ```ls``` to verify it's there--
```
ml purge
```
to remove subversion from your environment. 

3. Let's also make three directories for the outputs of our process:
```
mkdir out err /scratch/users/$USER/outputs
```
### Running Code

4. Now, let's move into our new directory
```
cd nltk
```
and submit our sbatch file to slurm, Sherlock's job scheduler: 
```
sbatch nltkNER.sbatch
```
You can watch your program run with
```
watch squeue -u $USER
```
When it finishes running, you should see your outputs as .csv and .json files in the outputs/ 
directory on scratch. This data can then be used as an input for other processes, or analyzed on its own.

#### Notes

[^1]: The syntax would be the same if you use Terminal on Linux or Windows Subsystem for Linux [(WSL)](https://learn.microsoft.com/en-us/windows/wsl/install). Using other programs is possible, but documenting them here would be 
impossible. 
