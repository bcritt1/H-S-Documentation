#!/usr/bin/bash
#SBATCH --job-name=nltk
#SBATCH --output=/home/users/bcritt/out/nltk.%j.out
#SBATCH --error=/home/users/bcritt/err/nltk.%j.err
#SBATCH -p hns
#SBATCH -c 1
#SBATCH --mem=32GB
module load python/3.9.0
python3 nltkNER.py
