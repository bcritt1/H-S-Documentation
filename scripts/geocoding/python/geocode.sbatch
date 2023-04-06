#! /usr/bin/bash
#SBATCH --job-name=test_job
#SBATCH --output=/home/users/bcritt/out/test_job.%j.out
#SBATCH --error=/home/users/bcritt/err/test_job.%j.err
#SBATCH --time=03:00:00
#SBATCH -p hns
#SBATCH -c 1
#SBATCH --mem=32GB
module load python/3.9.0
python3 geocode.py
