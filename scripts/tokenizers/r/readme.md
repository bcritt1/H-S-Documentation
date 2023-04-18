# Tokenizer Workflow

This repo contains two simple files that execute scikitlearn's TF-IDF functionality on a directory of txt files.

## File Overview

The files consist of:

1. [tokenize.py](/scripts/tokenizers/r/tokenize.r): Runs R's tokenizer libraryon a corpus of txt files. Can be run for 
sentences, words, paragraphs, etc. Outputs as .csv and .json, or either.
2. [tokenizePy.sbatch](/scripts/tokenizers/r/tokenizeR.sbatch): Creates a batch job for tokenize.r.

## Usage instructions

1. 1. Before we log onto Sherlock, let's make sure we're going to have everything we need there and move inputs/corpus onto Sherlock. For info on transferring data to Sherlock, see:
[https://www.sherlock.stanford.edu/docs/storage/data-transfer/](https://www.sherlock.stanford.edu/docs/storage/data-transfer/). [rsync](https://www.sherlock.stanford.edu/docs/storage/data-transfer/#rsync) is probably the best program for
this, but if you prefer another, go with that. For rsync, you'd use the command 
``` 
rsync -a ~/path/to/local/data yourSUNetid@login.sherlock.stanford.edu:/scratch/users/$USER/corpus/
```
You'll need to tweak the local path because I don't know where your files are located, but the remote path (after the ":") should work fine to get your corpus into scratch, a fast storage system where it's best to do file 
reading/writing.

2. ssh into sherlock with the syntax. ```ssh``` stands for "secure shell protocol" and is a program that lets you connect to another computer, in this case the one located at "sherlock.stanford.edu": 
```
ssh yourSUNetID@sherlock.stanford.edu
```

3. Once you are logged in, you'll want to have access to these files, which you can get with a couple simple commands. First, we need to install a program called subversion:
```bash
ml system subversion
```
This essentially reads as "module load" from the "system" sub-library the module "subversion". This is a syntax you will you any time you want to load a built-in module from the Sherlock environment. See 
[here](https://www.sherlock.stanford.edu/docs/software/modules/) for more.

Once it's loaded, let's  use subversion to download the files:
```bash
svn export https://github.com/bcritt1/H-S-Documentation/trunk/scripts/tokenizers/r/ tokenizers
```
This will create a directory in your home space on Sherlock called "tokenizers" with all the files in this 
repository. You'll want to
```bash
ml purge
```
after this as subversion can interfere with some dependencies.

4. While we're creating directories, let's make a few where our script will be routing data:
```bash
mkdir out err /scratch/users/$USER/outputs
``` 
The syntax for this is "make directories" and then the list of directories I want to make. The last one I gave a file path because I wanted to create it in a different location than where I am currently located on Sherlock.

5. Then, let's move into our new directory:
```bash
cd tokenizers/
```
which means "change directory" to the tokenizers directory we created with subversion. Once there, we should be ready to run with: 
```bash
sbatch tokenizeR.sbatch
```
which uses a command called sbatch to submit our tokenizeR.sbatch script to slurm, the job scheduler on Sherlock. You can watch your program run by combining the "watch" command with another slurm command:
```bash
watch squeue -u $USER
```
which translates to "watch the output of squeue for my user variable".

When it finishes running, you should see your output as a .csv file in outputs/ in scratch. This data 
can then be used as an input for pretty much all the processes in this library.

### Notes

[^1]: Scratch systems offer very fast read/write speeds, so they're good for things like I/O. However, data on 
scratch is deleted every 60 days if not modified, so if you use scratch, you'll want to transfer results back to your home directory.
