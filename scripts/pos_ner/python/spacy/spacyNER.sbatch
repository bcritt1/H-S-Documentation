#!/usr/bin/bash
#SBATCH --job-name=spacy
#SBATCH --output=/home/users/%u/out/spacy.%j.out
#SBATCH --error=/home/users/%u/err/spacy.%j.err
#SBATCH -p hns
#SBATCH -c 1
#SBATCH --mem=32GB
module load python/3.9.0
pip3 install spacy
python3 -m spacy download en_core_web_sm
python3 spacyNER.py
