#!/bin/bash
#SBATCH --job-name=myarrayjob
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --array=1-129

module load python/3.6.1
file=$(ls /home/users/bcritt/corpus/*.txt | sed -n ${SLURM_ARRAY_TASK_ID}p)
python3 /home/users/bcritt/fileLoad.py -in $file