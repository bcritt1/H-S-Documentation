#!/usr/bin/bash
#SBATCH --job-name=test_job
#SBATCH --output=test_job.%j.out
#SBATCH --error=test_job.%j.err
#SBATCH -p hns
#SBATCH -c 1
#SBATCH --mem=32GB
module load python/3.9.0
python3 spacy_tokenize_ner.py
