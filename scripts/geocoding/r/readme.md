# R Geocoding Workflow

This repo uses an R wrapper for [spaCy](https://cran.r-project.org/web/packages/spacyr/vignettes/using_spacyr.html) to identify places in a directory of txt files, then uses 
[tmaptools](https://cran.r-project.org/web/packages/tmaptools/tmaptools.pdf) to geocode those places with lat/long data.

## File Overview

1. [sherlockGeocode.R](/scripts/geocoding/python/sherlockGeocode.R) is the main script that performs NER and geocoding on a text corpus.

2. [sherlockGeocodeR.sbatch](/scripts/geocoding/python/sherlockGeocodeR.sbatch) is the slurm script that runs the job on Sherlock.

## Usage Instructions

### Connect to Sherlock

 First you must connect to Sherlock using
```
ssh SUNetID@sherlock.stanford.edu
```
in your terminal program.

### Download Files

Next, we're going to pull the files from this repo onto Sherlock using
```  
svn export https://github.com/bcritt1/H-S-Documentation/trunk/scripts/geocoding/python/ geocoding
```
this will create a new directory in your home called "geocoding". Let's ```cd geocoding``` there.

### Tweaking Files

There are a couple pieces of information I can't supply for you, so you'll have to make a few changes in these files. The .sbatch file should be configured for most jobs, but if you're running out of memory 
or time because your corpus is bigger than the one I was using, you may need to tweak the mem or time parameters. The .R file, however, will require at least one change to point the "input_loc" variable to 
your corpus location on Sherlock. For more on getting your corpus onto Sherlock, see: 
[https://www.sherlock.stanford.edu/docs/storage/data-transfer/](https://www.sherlock.stanford.edu/docs/storage/data-transfer/).

### Running the script

At this point, you should be ready to run. To do this, make sure you're in the geocoding directory and type
```
sbatch sherlockGeocodeR.sbatch
```
This will run sherlockGeocode.R, and output a file called "places.csv" to the directory. If you have any issues, contact [srcc-support@stanford.edu](srcc-support@stanford.edu) and your question will be 
routed to me.
