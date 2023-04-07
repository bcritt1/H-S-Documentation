#!/usr/bin/bash
#SBATCH --job-name=spacy
#SBATCH --output=/home/users/bcritt/out/spacy.%j.out
#SBATCH --error=/home/users/bcritt/err/spacy.%j.err
#SBATCH -p hns
#SBATCH -c 1
#SBATCH --mem=32GB
module load python/3.9.0
python3 spacy.py
