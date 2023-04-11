#!/usr/bin/bash
#SBATCH --job-name=cleaning
#SBATCH --output=/home/users/%u/out/cleaning.%j.out
#SBATCH --error=/home/users/%u/err/cleaning.%j.err
#SBATCH -p hns
#SBATCH -c 1
#SBATCH --mem=32GB
module load python/3.9.0
pip3 install nltk
pip install --upgrade certifi
python3 -m nltk.downloader all
python3 text_cleaning_pipeline.py
