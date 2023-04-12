#!/usr/bin/bash
#SBATCH --job-name=embedding
#SBATCH --output=/home/users/%u/out/embedding.%j.out
#SBATCH --error=/home/users/%u/err/embedding.%j.err
#SBATCH -p hns
#SBATCH -c 1
#SBATCH --mem=32GB
module load python/3.9.0
module load gensim
pip3 install --user --upgrade certifi
pip3 install nltk
python3 -m nltk.downloader all
python3 embedding.py
