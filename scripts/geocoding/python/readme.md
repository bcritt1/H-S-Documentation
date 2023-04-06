# Python Geocoding Workflow

This repo contains four simple files that execute spaCy's [NER](https://spacy.io/api/entityrecognizer/) functionality on a group of files and use that output as an input for geocoding in 
[Nominatim](https://nominatim.org/)[^1].

## File Overview

The files consist of:

1. [packages.sh](/scripts/geocoding/python/packages.sh): A shell script that sets up your environment, loading the correct version of python, some dependencies, and installing the python packages in requirements.txt.
2. [requirements.txt](/scripts/geocoding/python/requirements.txt): You shouldn't need to touch this. Simply tells python which packages it needs to install to run geocoding.py.
3. [geocoding.py](/scripts/geocoding/python/geocoding.py): Runs spaCy and Nominatum, outputing a .csv file with all the places (geopolitical entities) in your corpus and their lat/long coordinates.
4. [geocoding.sbatch](/scripts/geocoding/python/geocoding.sbatch): Creates a batch job for geocoding.py.

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
svn export https://github.com/bcritt1/H-S-Documentation/trunk/scripts/geocoding/python/
```
This will create a directory in your home space on Sherlock called "geocoding" with all the files in this repository.
![Repo Pull](/images/repoPull.png)

3. Once you have the files, you'll use packages.sh to set up your environment. First, we need to give the computer permission to run our shell script:
```
cd geocoding/
chmod +x packages.sh
```
If you ```ls``` now, you should see that your packages.sh file has changed colors, meaning it is now executable.
![chmod](/images/chmod.png)

4. Now run it:
```
./packages.sh
```
You should see some dialog from the computer as it installs different things:
![shell script](/images/bashScript.png)

5. With our environment set up, we just need to make one small tweak to our main script:
```
nano geocoding.py
```
and change the line "corpus dir = /scratch/users/bcritt/corpus/" to the location of your corpus[^2]. For info on transferring data to Sherlock, see: [https://www.sherlock.stanford.edu/docs/storage/data-transfer/](https://www.sherlock.stanford.edu/docs/storage/data-transfer/). For the purposes of efficiency, it is best that you locate your corpus in scratch like me, but it can be anywhere so long as you point the script to it.

6. At this point, we're just about ready to run our main script. However, you'll want to make a few tweaks to geocode.sbatch first. I've tuned most parameters for this process, but you'll need to change 
the path for your *.out and *.err files, which give you feedback on what went wrong should your script fail. I route them to /out and /err directories in my home: you can do the same by changing my user 
name to yours in the script. I tested the script on a list of ~4500 place names (<len(places)> in python) and it took 1.5 hours and consumed a little over 13 gb of memory at most. Therefore the sbatch file 
asks for 2 hours and 16 gb memory. Because of API limits, you can estimate 1-2 seconds per query and adjust the -t line accordingly. The memory usage should stay pretty constant, but because we're cutting 
it pretty close, you may want to adjust this up.

 ```
nano geocode.sbatch
```
to make any of these changes.

Then you should be able to run with: 
```
sbatch geocode.sbatch
```
When it finishes running, you should see your output as a file called places.csv in the geocoding directory[^3].

### Notes

[^1]: Google's geocoding API may offer better accuracy, but it can also rack up charges fast on large datasets. Nominatum is free and open-source.
[^2]: Scratch systems offer very fast read/write speeds, so they're good for things like I/O. However, data on scratch is deleted every 60 days if not modified, so if you use scratch, you'll want to transfer results back to your home directory.
[^3]: There are a few likely culprits for failure here, just because everyone's data is different. First, spaCy places a limit on the length of inputs by default. I have upped this limit with the line in geocoding.py "nlp.max_length = 5000000". You can get a rough idea of the length of your input by running ```wc``` in your "corpus" directory. Something a little bigger than that number should be safe. Also depending on the size of your data, you may get a memory error, which can be adjusted in the "-mem" line of the geocode.sbatch file. There are some more notes on things you might want to tweak in the geocode.py file itself. As always, if you don't see your places.csv file once the process finishes, check the .out and .err files for your job. You can contact [me](mailto:bcritt@stanford.edu) if you can't debug from there.
