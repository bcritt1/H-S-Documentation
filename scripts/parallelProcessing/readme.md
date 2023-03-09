# Intro to Parallel Processing

People may gravitate toward high-performance computing because they have jobs that would take a really long time to run on a home or office computer. The sheer performance of the hardware in high-performance clusters can help to "brute force" jobs. However, the most efficient way to use HPC resources is to run jobs in [parallel](https://en.wikipedia.org/wiki/Parallel_computing), which means that parts of your job are being done simultaneously on different pieces of hardware. 

Imagine, for instance, you have 100 (or 1,000 or 1,000,000) high-quality videos you need to read into a computer to analyze them. Being high-quality means that they're also really big, and it takes a computer a long time to "read" them: 10-20 minutes each. While throwing more power at them in a serial computing configuration could make the process go slightly faster, what if you could read in all 100 videos at the same time? Even if each video takes 20 minutes, if they're all being scanned in at the same time, all 100 will be done in 20 minutes, not 100 x 20 (33 hours) it would take to read them serially.

# Script Description

[largeTaskArray.sbatch](/scripts/parallelProcessing/largeTaskArray.sbatch) is an sbatch script using the Slurm job array functionality to perform parallel processing of jobs that may take a little while to run individually. It calls [fileLoad.py](/scripts/parallelProcessing/fileLoad.py), which loads x files into memory in python. The number of files will be the range in the ```#SBATCH --array=``` in the .sbatch file. Other than that, primary changes include the input directory and the location of the .py file. It should be noted that for loading small files, you'd likely want to use the [smallTaskArray.sbatch(/scripts/parallelProcessing/smallTaskArray.sbatch) workflow as it will minimize strain on the scheduler. For very large files (videos, say), this should work fine, or you can adapt the script to do something other than loading files.

The pair of pdf.sbatch and pdf_convert.sh perform a similar function, creating a job array for the ingestion and conversion of pdf text files to OCR'ed plaintext. Very useful if you create or obtain a large corpus in pdf form. pdf_convert.sh can be adapted to run as a standalone shell script or as a non-array sbatch job for smaller corpora.

There are other methods of parallel processing (openMP, MPI), but Slurm job arrays are generally easier/cleaner.
