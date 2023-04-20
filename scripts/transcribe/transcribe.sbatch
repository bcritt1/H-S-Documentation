#!/usr/bin/bash
#SBATCH --job-name=transcribe
#SBATCH --output=/home/users/bcritt/out/transcribe.%j.out
#SBATCH --error=/home/users/bcritt/err/transcribe.%j.err
#SBATCH --time=00:10:00
#SBATCH -p hns
#SBATCH -c 1
#SBATCH --mem=8GB
module load python/3.9.0
python3 transcribeCorpus.py
