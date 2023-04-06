# PDF to Text Conversion

This repo provides a shell script for the conversion of pdf files to plain-text for the purposes of higher-level text processing. This implementation utilizes the job array functionality of slurm to process all files in parallel. 
Parallelization may not be necessary for small corpora. 

## File Overview

[parallel_pdf_convert.sh](/scripts/ocr/parallel_pdf_convert.sh) utilizes imagemagick, tesseract, and ghostscript to OCR pdf files. Should also work on tiffs with light tweaking.

[parallel_pdf.sbatch](/scripts/ocr/parallel_pdf.sbatch) invokes the shell script and runs as a slurm array. 

## Usage Instructions

### Connecting to Sherlock

To connect to Sherlock
```
ssh yourSUNetID@sherlock.stanford.edu
```
in your terminal program of choice. 

### Downloading the Scripts

Once you are logged in, you'll want to have access to the files in this repo, which you can get with a couple simple commands. First, we need to install a program called subversion:
```
module load system subversion/1.12.2
```
and use that program to download the files:
```
svn export https://github.com/bcritt1/H-S-Documentation/trunk/scripts/ocr/ ocr
```
This will create a directory in your home space on Sherlock called "ocr" with all the files in this repository.

Next, we need to give the computer permission to run our shell script:
```
cd ocr/
chmod +x parallel_pdf_convert.sh
```
If you ```ls``` now, you should see that your parallel_pdf_convert.sh file has changed colors, meaning it is now executable.

### Tweaking your Files

Now we just need to tweak two variables in the shell script to reflect your environment. 
```
nano parallel_pdf_convert.sh
```
and change the FILES and DIR variables to reflect the location of your PDFs on Sherlock. For more on transferring your data to Sherlock, see 
[https://www.sherlock.stanford.edu/docs/storage/data-transfer/](https://www.sherlock.stanford.edu/docs/storage/data-transfer/).

Another tweak in the .sbatch file and we will be good to go. 
```
nano pdf_convert.sbatch
```
Here you need to make one of the following changes depending on whether you want to run in parallel:If you don't want to run in parallel, you can simply remove the array line in the slurm instructions. If running as an array, the range 
in this line should be adjusted to 1-n, where n is the number of files in your input directory. 

I've configured the jobs for 16GB memory which worked for my small test corpus: this process should be
relatively steady in memory usage, but if you're getting a memory error, this can be increased. Wall time is set at the default of 2 hours, but a line with eg. #SBATCH time=04:00:00 for 4 hours could be added to change this. For 
reference, two pdfs of about 15 pages each only took about 1.5 minutes total.

Finally, you'll need to change places with <USERNAME> to your username on Sherlock. 

### Running the Script

We should be ready.
```
sbatch pdf_convert.sbatch
```
to run the shell script. The script will take your pdfs, convert them to .tiff files, then convert those .tiff files to plain text. It will create /tiff and /ocr directories inside the directory with your pdfs and send the .tiff and 
.txt files there respectively. You may or may not need the .tiff files, but the .txt files can be used as inputs for just about any of the text processing sub-repos you find here. 
