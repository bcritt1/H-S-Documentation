# HPC Introduction on Farmshare

Farmshare is an open high powered computing (HPC) learning environment where anyone with a SUNet ID can sign on, without registering, and learn HPC. 

## Overview

In this workshop, we'll be running a named entity recognizer on Ralph Waldo Emerson's ouevre. We'll be using a machine learning platform called huggingface, through which we will leverage a large language model called "BERT" 
(Bidirectional Encoder Representations from Transformers). BERT is a cutting edge model that rivals GPT in analytical tasks (though it can't generate responses like GPT). Our output will be a .json file with all of the named entities 
(important people, places, things) in this text corpus. Having the computer encode and return certain types of information from large text corpora is an important retrieval task for doing higher level things like social network analysis, 
knowledge graphing, mapping references, etc. 

## Farmshare vs Sherlock

If you are interested in doing this process on your own data, this workshop is adapted from a [tutorial](https://github.com/bcritt1/H-S-Documentation/tree/main/scripts/pos_ner/python/huggingface) for Sherlock, the research HPC cluster at 
Stanford. This is part of a larger script [library](https://github.com/bcritt1/H-S-Documentation/tree/main/scripts) with easy to implement scripts for common computational text analysis processes.

If you go through today and decide this command line interface (CLI) is too much for you, Sherlock also has a really neat service called OpenOndemand where you can work in a graphical user interface (GUI) like RStudio or jupyter 
notebooks. This also has the benefit of being interactive, so instead of, say, outputting visualizations as jpegs in a batch script, you can produce interactive visualizations and iterate mid-script in OpenOndemand. It is, however, a 
really new paradigm for HPC, so you'll likely run into a few snafus along the way.

## Connecting

To connect to the HPC cluster, we need to use a program called ssh (secure shell protocol). This is easy on Mac and Linux, but Windows requires a little extra work. To install the OpenSSH Client on Windows 10 or Windows 11, open the 
Settings app, then navigate to Apps > Apps & Features > Optional Features.  Click “Add a Feature,” then scroll through the optional features until you locate “OpenSSH Client.” Tick the box, then click “Install.” At this point, Windows 
users can open up their "Powershell" application, and Mac/Linux users can open up "Terminal" and all of us can type
```bash
ssh SUNetID@rice.stanford.edu
```
You'll be prompted for your Stanford password, which you can copy and paste here (there will be no cursor marker, so it's easiest to just C + P). Press enter, complete the 2FA, and then you'll see some cool graphics.

![farmshare](/images/farmshare.png)

In this window, now, you are on a Linux machine somewhere else in the world. This is a log-in node, where you can work to set-up any jobs you want to run, and submit them to a compute node on the Farmshare cluster. If that sounds like 
nonsense, we'll be doing all of that stuff here shortly, so it'll make more sense in a bit.

## Moving and seeing in the shell

So you're probably feeling pretty lost right now. There are a couple basics to getting around in the shell, which is essentially the layer upon which graphical operating systems like MacOS and Windows run, and is essentially a more 
direct, non-graphical way of interacting with your computer. The architecture underneath, though, is the same. Type
```bash
pwd
```
and you will see something like ```/home/yourUsername/```. ```pwd``` stand for "print working directory" and it tells you "where you are located" in your computer. On a graphical system, this would be like the file you have open in 
File Explorer. Our directory is empty right now, so let's grab some files with a program called subversion, which will go to the github repo we are at, download what's there, and throw the content into a new directory:
```bash
svn export https://github.com/bcritt1/H-S-Documentation/trunk/scripts/pos_ner/python/huggingface/ huggingface
``` 
![hugpull](/images/hugpull.png)
You'll see a list of things the program downloaded once the program runs.

Now type
```bash
ls
```
which stands for "list", and you should see a new directory called "huggingface". If you type ```cd hug``` then the ```Tab``` button, the shell will complete your command to ```cd huggingface```. Because ```cd``` means "change 
directory", when you press ```Enter```, you will move into the huggingface directory. You can pwd to confirm you're in ```home/Username/huggingface/``` now, and/or ```ls``` to see what's in this new directory. 

![huggingface](/images/huggingface.png)
```bash
cat huggingface.sbatch
```
to see our sbatch file. EXPLANATION

Now
```bash
cat huggingface.py
```
to see our python code. EXPLANATION

Now that we know what they do, these are all set up to run:
```bash
sbatch huggingface.sbatch
```
```bash
watch squeue -u $USER
```
