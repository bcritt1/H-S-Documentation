#!/bin/bash
#SBATCH --job-name=myarrayjob
#SBATCH --output=/home/users/%u/out/myarray.%j.out
#SBATCH --error=/home/users/%u/err/myarray.%j.err
#SBATCH -p owners
#SBATCH --ntasks=1 # Run a single task 
#SBATCH --mem-per-cpu=8gb # Memory per processor 
#SBATCH --array=1-2

# load python and set input location
ml python/3.9.0
python3 parallel_transcribe.py --file "/home/users/bcritt/audio/recording${SLURM_ARRAY_TASK_ID}.wav"
