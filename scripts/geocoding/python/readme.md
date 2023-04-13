# Python Geocoding Workflow

This repo contains four simple files that execute spaCy's [NER](https://spacy.io/api/entityrecognizer/) functionality on a group of files and use that output as an input for geocoding in 
[Nominatim](https://nominatim.org/)[^1].

## File Overview

The files consist of:

1. [requirements.txt](/scripts/geocoding/python/requirements.txt): You shouldn't need to touch this. Simply tells python which packages it needs to install to run geocoding.py.
2. [geocode.py](/scripts/geocoding/python/geocoding.py): Runs spaCy and Nominatum, outputing a .csv file with all the places (geopolitical entities) in your corpus and their lat/long coordinates.
3. [geocode.sbatch](/scripts/geocoding/python/geocoding.sbatch): Creates a batch job for geocoding.py.

## Usage instructions

1. ssh into sherlock with the syntax: 
```bash
ssh yourSUNetID@sherlock.stanford.edu
```

2. Once you are logged in, you'll want to have access to these files, which you can get with a couple simple commands. First, we need to install a program called subversion:
```bash
ml subversion
```
and use that program to download the files:
```
svn export https://github.com/bcritt1/H-S-Documentation/trunk/scripts/geocoding/python/ geocoding
```
This will create a directory in your home space on Sherlock called "geocoding" with all the files in this repository.
![Repo Pull](/images/repoPull.png)
```bash
cd geocoding
```
into your new directory.

3. At this point, you should be able to run everything:
```bash
sbatch geocode.sbatch
```

I tested the script on a list of ~4500 place names (<len(places)> in python) and it took 1.5 hours and consumed a little over 13 gb of memory at most. Therefore the sbatch file 
asks for 2 hours and 16 gb memory. Because of API limits, you can estimate 1-2 seconds per query and adjust the -t line accordingly. The memory usage should stay pretty constant, but because we're cutting 
it pretty close, you may want to adjust this up.

```
nano geocode.sbatch
```
to make any of these changes.

When it finishes running, you should see your output as a file called places.csv in your outputs directory at /scratch/users/$USERNAME/outputs/[^3].

## Code Overview

### geocode.py

Fairly detailed in-line notes in the script itself, so check that out for more detail. Generally, the code reads in your corpus, tokenizes the corpus, and performs named entity recognition. One of the outputs of the last process is the 
labeling of places as Geopolitical Entities (GPEs). We then filter the data to retain only GPEs and feed those place names into Nominatim, which returns lat/long coordinates for those places.

### geocode.sbatch

```bash
#!/usr/bin/bash
#SBATCH --job-name=geocode					# gives the job a descriptive name that slurm will use
#SBATCH --output=/home/users/%u/out/geocode.%j.out		# the filepath slurm will use for output files. I've configured this so it automatically inserts variables for your username (%u) and the job name (%j) above.
#SBATCH --error=/home/users/%u/err/geocode.%j.err		# the filepath slurm will use for error files. I've configured this so it automatically inserts variables for your username (%u) and the job name (%j) above.
#SBATCH -p hns							# the partition slurm will use for the job. Here it is hns (humanities and sciences), but you can use other partions (sh_part to see which you can access)
#SBATCH -c 1							# number of cores to use. This should be 1 unless you've rewritten the code to run in parallel
#SBATCH --mem=32GB						# memory to use. 32GB should be plenty, but if you're getting a memory error, you can increase
module load python/3.9.0					# load the most recent version of python on Sherlock
pip3 install nltk						# download nltk
pip install --upgrade certifi					# allow nltk to download files
python3 -m nltk.downloader all					# download nltk files
python3 geocode.py						# run the python script
```

#### Notes

[^1]: Google's geocoding API may offer better accuracy, but it can also rack up charges fast on large datasets. Nominatum is free and open-source.
[^2]: Scratch systems offer very fast read/write speeds, so they're good for things like I/O. However, data on scratch is deleted every 60 days if not modified, so if you use scratch, you'll want to transfer results back to your home directory.
[^3]: There are a few likely culprits for failure here, just because everyone's data is different. First, spaCy places a limit on the length of inputs by default. I have upped this limit with the line in geocoding.py "nlp.max_length = 5000000". You can get a rough idea of the length of your input by running ```wc``` in your "corpus" directory. Something a little bigger than that number should be safe. Also depending on the size of your data, you may get a memory error, which can be adjusted in the "-mem" line of the geocode.sbatch file. There are some more notes on things you might want to tweak in the geocode.py file itself. As always, if you don't see your places.csv file once the process finishes, check the .out and .err files for your job. You can contact [me](mailto:bcritt@stanford.edu) if you can't debug from there.
