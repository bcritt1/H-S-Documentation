# Huggingface NER Workflow

This repo contains three simple files that execute an iteration of huggingface NER..

## File Overview

The files consist of:

1. [packages.sh](/scripts/pos_ner/python/huggingface/packages.sh): A shell script that sets up your environment, loading the correct version of python and some dependencies..
2. [huggingface.py](/scripts/pos_ner/python/hugginface/huggingface.py): Runs huggingface on a corpus, outputing a .json file with POS and NER for all the words in your corpus.
3. [geocoding.sbatch](/scripts/pos_ner/python/huggingface/huggingface.sbatch): Creates a batch job for huggingface.py.

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
svn export https://github.com/bcritt1/H-S-Documentation/trunk/scripts/pos_ner/python/huggingface/ huggingface
```
This will create a directory in your home space on Sherlock called "huggingface" with all the files in this repository.

3. Once you have the files, you'll use packages.sh to set up your environment. First, let's move into our new directory::
```
cd huggingface/
```

4. And run the shell script that sets up our environment::
```
./packages.sh
```
You should see some dialog from the computer as it installs different things:
![shell script](/images/hugpull.png)

5. With our environment set up, we just need to make one small tweak to our main script:
```
nano huggingface.py
```
and change the line "corpus dir = /scratch/users/bcritt/corpus/" to the location of your corpus[^1]. For info on 
transferring data to Sherlock, see: [https://www.sherlock.stanford.edu/docs/storage/data-transfer/](https://www.sherlock.stanford.edu/docs/storage/data-transfer/). For the purposes of efficiency, it is best that you locate your corpus in scratch like me, but it can be anywhere so long as you point the script to it.

6. At this point, we're just about ready to run our main script. However, you'll want to make a few tweaks to 
huggingface.sbatch first. I've tuned most parameters for this process, but you'll need to change 
the path for your *.out and *.err files, which give you feedback on what went wrong should your script fail. I route them to /out and /err directories in my home: you can do the same by changing my user 
name to yours in the script. You may need to increase mem or time depending on the size of your corpus, but the 
values given here are a pretty good starting place.

 ```
nano huggingface.sbatch
```
to make any of these changes.

Then you should be able to run with: 
```
sbatch huggingface.sbatch
```
When it finishes running, you should see your output as a file called data.json in the huggingface 
directory[^3]. This data can then be used as an input for some other process.

### Notes

[^1]: Scratch systems offer very fast read/write speeds, so they're good for things like I/O. However, data on 
scratch is deleted every 60 days if not modified, so if you use scratch, you'll want to transfer results back to your home directory.
