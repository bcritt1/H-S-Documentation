#!/usr/bin/bash
#SBATCH --job-name=cleaning
#SBATCH --output=/home/users/bcritt/out/cleaning.%j.out
#SBATCH --error=/home/users/bcritt/err/cleaning.%j.err
#SBATCH -p hns
#SBATCH -c 1
#SBATCH --mem=32GB
module load python/3.9.0
python3 text_cleaning_pipeline.py
