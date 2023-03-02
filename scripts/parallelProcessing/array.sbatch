#!/bin/bash
#SBATCH --job-name=myarrayjob
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --array=1-129


sleep 60
file=$(ls ./corpus/*.txt | sed -n ${SLURM_ARRAY_TASK_ID}p)
myscript -in $file
module load python/3.9.0
python3 fileLoad.py
