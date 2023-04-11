#!/usr/bin/bash
#SBATCH --job-name=nltk
#SBATCH --output=/home/users/%u/out/nltk.%j.out
#SBATCH --error=/home/users/%u/err/nltk.%j.err
#SBATCH -p hns
#SBATCH -c 1
#SBATCH --mem=32GB
module load python/3.9.0
pip3 install nltk
pip3 install --upgrade certifi
python3 -m nltk.downloader all
python3 nltkNER.py
