#!/usr/bin/bash                     # tells the computer this is a bash script and how to run it
#SBATCH --job-name=test_job         # gives the job a name. if you run a long program, you can type "squeue" into the terminal and check on your job's progress by this name.
#SBATCH --output=test_job.%j.out    # gives a name to your output file. You can direct this elsewhere by giving it a file path: ../../home/bcritt/testjob.out.
#SBATCH --error=test_job.%j.err     # a file that outputs any errors your script encounters. Good if something goes wrong.
#SBATCH --time=10:00                # sets a time limit for your job. Format is DD:HH:MM:SS. Currently, this is set to 10 minutes.
#SBATCH -p normal                   # tells Sherlock which partition to use. "Normal" is the default partition for free users, but as an H&S member, you will likely have access to a special partition called "hns" that will likely be faster to schedule. You can check which partitions you can use with the terminal command sh_part and change "normal" to "hns" if desired.
#SBATCH -c 1                        # number of cores to use.
#SBATCH --mem=8GB                   # amount of RAM to use.
python3 ./mycode.py                 # Invoke the desired script just as you would in the Terminal.
