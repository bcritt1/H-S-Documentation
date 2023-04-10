# Tokenizer Workflow

This repo contains two simple files that execute scikitlearn's TF-IDF functionality on a directory of txt files.

## File Overview

The files consist of:

1. [tokenize.py](/scripts/tfidf/tokenize.py): Runs nltk tokenizer on a corpus of txt files. Can be run for 
sentences, words, paragraphs, etc. Outputs as .csv.
3. [tokenizePy.sbatch](/scripts/tfidf/scikit_tfidf.sbatch): Creates a batch job for tokenize.py.

## Usage instructions

1. ssh into sherlock with the syntax: 
```
ssh yourSUNetID@sherlock.stanford.edu
```

2. Once you are logged in, you'll want to have access to these files, which you can get with a couple simple commands. First, we need to install a program called subversion:
```
module load system subversion/1.12.2
```
and use that program to download the files:
```
svn export https://github.com/bcritt1/H-S-Documentation/trunk/scripts/tokenizers/python/ tokenizers
```
![nltkdir](/images/tokenizersdir.png)
This will create a directory in your home space on Sherlock called "tfidf" with all the files in this 
repository. You'll want to
```
ml purge
```
after this as subversion tends to interfere with python dependencies.

3. Once you have the files, you'll use packages.sh to set up your environment. First, let's move into our new directory::
```
cd tokenizers/
```

4. We just need to make one small tweak to our main script:
```
nano tokenize.py
```
and change the line "corpus dir = /scratch/users/bcritt/corpus/" to the location of your corpus[^1]. For info on 
transferring data to Sherlock, see: [https://www.sherlock.stanford.edu/docs/storage/data-transfer/](https://www.sherlock.stanford.edu/docs/storage/data-transfer/). For the purposes of efficiency, it is best that you locate your corpus in 
scratch like me, but it can be anywhere so long as you point the script to it. There is a .csv output line at the 
end of this file that can be added after any intermediate step, though you'll need to do some output control to 
prevent each .csv from overwriting the next.

6. At this point, we're just about ready to run our main script. However, you'll want to make a few tweaks to 
tokenize.sbatch first. I've tuned most parameters for this process, but you'll need to change 
the path for your *.out and *.err files, which give you feedback on what went wrong should your script fail. I route them to /out and /err directories in my home: you can do the same by changing my user 
name to yours in the script. You may need to increase mem or time depending on the size of your corpus, but the 
values given here are a pretty good starting place.

 ```
nano tokenize.sbatch
```
to make any of these changes.

Then you should be able to run with: 
```
sbatch tokenize.sbatch
```
When it finishes running, you should see your output as a .csv file in outputs/ in scratch. This data 
can then be 
used as an input for some other process.

### Notes

[^1]: Scratch systems offer very fast read/write speeds, so they're good for things like I/O. However, data on 
scratch is deleted every 60 days if not modified, so if you use scratch, you'll want to transfer results back to your home directory.
