# HPC Introduction on Farmshare

Farmshare is an open high powered computing (HPC) learning environment where anyone with a SUNet ID can sign on, without registering, and learn HPC. 

## Overview

In this workshop, we'll be running a named entity recognizer on Ralph Waldo Emerson's ouevre. We'll be using a machine learning platform called huggingface, through which we will leverage a large language 
model called "RoBERTa", which is based on "BERT" 
(Bidirectional Encoder Representations from Transformers). RoBERTa is a cutting edge model that rivals GPT in analytical tasks (though it can't generate responses like GPT). Our output will be a .json file 
with all of the named entities 
(important people, places, things) in this text corpus. Having the computer encode and return certain types of information from large text corpora is an important retrieval task for doing higher level things like social network analysis, 
knowledge graphing, mapping references, etc. 

## [Farmshare](https://web.stanford.edu/group/farmshare/cgi-bin/wiki/index.php/Main_Page) vs [Sherlock](https://www.sherlock.stanford.edu/docs/)

If you are interested in doing this process on your own data, this workshop is adapted from a [tutorial](https://github.com/bcritt1/H-S-Documentation/tree/main/scripts/pos_ner/python/huggingface) for Sherlock, the research HPC cluster at 
Stanford. This is part of a larger script [library](https://github.com/bcritt1/H-S-Documentation/tree/main/scripts) with easy to implement scripts for common computational text analysis processes.

While you can jump onto Farmshare without even registering, it is a relatively small cluster that isn't meant for heavy-duty research. To get on Sherlock, you need to be approved by a PI, but this can be provided by your advisor or potentially CESTA given your affiliation.

If you go through today and decide this command line interface (CLI) is too much for you, Sherlock also has a really neat service called [Open 
OnDemand](https://login.sherlock.stanford.edu/pun/sys/dashboard) where you can work in a graphical user interface (GUI) like RStudio or jupyter 
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
and you will see something like ```/home/yourUsername/```. ```pwd``` stands for "print working directory" and it tells you "where you are located" in your computer. On a graphical system, this would be like 
the file you have open in 
File Explorer. Our directory is empty right now, so let's create some directories (or folders):
```bash
mkdir out/ err/ outputs/
```
which reads as "make directory" and then the directories you want to make. 
Now type:
```bash
ls
```
which stands for "list", and you should now see our "out", "err", and "outputs" directories. If you type ```cd out``` then the ```Tab``` button, the shell will complete your command to ```cd outputs```. 
Because ```cd``` means "change 
directory", when you press ```Enter```, you will move into the "outputs" directory. You can```pwd``` to confirm you're in ```home/Username/outputs/``` now, a place that didn't exist until you made it a 
second ago! We made this and the other directories because we're going to be directing the outputs of our script to them in a second. 

## Exploring and Running Code
To get to our scripts, which I've set up already for the purposes of 
time, we need to: 

```bash
cd /farmshare/home/groups/srcc/cesta_workshop/
```
to move there, If you ```ls``` you'll a few directories: "corpus", "huggingface", and "conda". 

![cestadir](/images/cestadir.png)

The first contains a sample corpus representing the collected works of Ralph Waldo Emerson. These are our inputs, the material we are feeding into our script: I had this corpus on hand, but it could be 
any collection of texts you want to investigate. "conda" contains an environment that I created that holds the different libraries we'll need to execute our script: normally, you may be doing some of this 
work, but for time, I did it. That said, my script library should make a lot of this labor "plug & play", so the technical barrier should be relatively low regardless. Finally, the "huggingface" directory 
holds our scripts. Let's ```cd``` there.

```bash
cat huggingface.sbatch
```
to see our sbatch file. The sbatch file is the way we communicate with Slurm, the job scheduler on our clusters. Because HPC systems are shared and people often need the same resources at the same time, a 
scheduler schedules job times for people based on the requests they make in their sbatch file (smaller jobs get scheduled faster). Our sbatch file looks like this:
```bash
#!/bin/bash						# tells the computer what type of program this is. This will appear at the start of all sbatch (and bash) scripts
#SBATCH --job-name=huggingface				# gives a name to our job. This can be anything, but like most things in programming, it's good to be descriptive
#SBATCH --output=/home/%u/out/huggingface.%j		# slurm automatically produces two types of outputs from jobs. These can help you debug if things go wrong. Here I'm routing them to the directories we created earlier.
#SBATCH --error=/home/%u/err/huggingface.%j		# the err file is usually more helpful, as it outputs any error messages your code produces. Because you're submitting your job and not running interactively, you don't get to see these errors as they happen
#SBATCH -c 1						# tells slurm to run the job on 1 core. Unless you've parallelized your code so it can run separate processes on separate hardware, this will usually be 1
#SBATCH --mem=32GB					# tells slurm how much memory to use. For many users, this is the primary benefit of hpc. My pretty beefy machine at home has 32 GB of RAM, and that's probably 2-4x what most people have. However, I couldn't use all those 32GB for a job, because the computer itself needs memory to run. On an hpc system, you can devote more memory (and exactly the amount) you need for a job. If jobs are failing on your personal machines, you may ***need*** hpc to do your research.
							# Everything below here (the lines without #s) are shell commands and not communicating with slurm. 
source /farmshare/home/groups/srcc/cesta_workshop/miniconda3/bin/activate		# activates the anaconda environment I set up, which basically contains the python libraries we invoke in our py 
script
python3 /farmshare/home/groups/srcc/cesta_workshop/huggingface/huggingface.py		# runs our py script with python3
```
Now
```bash
cat huggingface.py
```
to see our python code. It too is relatively straightforward. We import a couple packages at the top which give us functionality beyond base python (here to read our filesystem and create jsons). We then tell it where our corpus is and read it in. After that, we import language models from huggingface. We tell huggingface what we want it to do with our corpus and then perform the process. And finally we export all of that data to json, which we can check out in a bit.

```python
# Import packages
import os
import json

# Read in corpus
user = os.getenv('USER')
corpusdir = '/farmshare/home/groups/srcc/cesta_workshop/corpus/'
#corpusdir = '/scratch/users/{}/corpus/'.format(user)
corpus = []
for infile in os.listdir(corpusdir):
    with open(corpusdir+infile, errors='ignore') as fin:
        corpus.append(fin.read())

# Import language models and pipeline elements
from transformers import AutoTokenizer, AutoModelForTokenClassification
tokenizer = AutoTokenizer.from_pretrained("Jean-Baptiste/roberta-large-ner-english")
model = AutoModelForTokenClassification.from_pretrained("Jean-Baptiste/roberta-large-ner-english")


# Process corpus
from transformers import pipeline
nlp = pipeline('ner', model=model, tokenizer=tokenizer, aggregation_strategy="simple")
entities = nlp(corpus)

# Export data to json
with open('/home/{}/outputs/data.json'.format(user), 'w', encoding='utf-8') as f:
    json.dump(str(entities), f, ensure_ascii=False, indent=4)
```

Now that we know what they do, the scripts are ready to run. We submit the .sbatch file to Slurm with the sbatch command. The sbatch, in turn, give Slurm directions and tells it to run our .py file.
```bash
sbatch huggingface.sbatch
```
to run the script and:
```bash
watch squeue -u $USER
```
to watch the queue while it completes. 

## Outputs

Because of the file paths we supplied in the .sbatch and .py files, our *.out and *.err files will be routed to home/userName/out and */err, and our outputs will go to home/userName/outputs. The script is 
going to take 10 or more minutes to complete, but we can ```cd``` to that location to check out our output when it's done. Or you can even check it out from here by giving it a filepath:
```bash
head /home/userName/outputs/data.json
```
![outputs](/images/outputs.png)
What we see is all Named Entities (proper nouns, more or less) in our inputs categorized as a type of entity, and a confidence score of how likely the computer things it is that they actually are that type 
of entity. This type of output can be the basis for interesting analyses in its own right (What things interest this writer? Are they more interested in people or political entities?) or as the basis for 
secondary analyses (extracting everything labelled as a place and mapping them). 

## Wrap-Up
This process took about 15 minutes on 32 GB of RAM, working on a relatively small (130 works) corpus. Compute time will 
often expand exponentially with inputs, so anyone looking to do serious digital research of this type may *need* to use HPC resources. I'm hoping this workshop gave you an idea of what HPC is, how it works, 
and how you can take advantage of it here at Stanford with a relatively low barrier to entry. Remember, on Sherlock Open OnDemand offers an even more user-friendly experience, and I'm always here to help 
regardless of how you engage with our resources. 

My git [repo](https://github.com/bcritt1/H-S-Documentation/blob/main/scripts/farmshare/readme.md) contains scripts and documentation for many processes, tailored for use on Sherlock. Sherlock itself has a lot of good [documentation](https://www.sherlock.stanford.edu/docs/). Finally, Quinn Dombrowski has been working on a lot of good information for Humanists in HPC [here](https://dh-stanford.github.io/hpcforhumanists/intro.html).

[bcritt@stanford.edu](mailto:bcritt@stanford.edu) with questions.
