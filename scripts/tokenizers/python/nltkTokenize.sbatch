#!/usr/bin/bash
#SBATCH --job-name=tokenize
#SBATCH --output=/home/users/bcritt/out/tokenize.%j.out
#SBATCH --error=/home/users/bcritt/err/tokenize.%j.err
#SBATCH --time=02:00:00
#SBATCH -p hns
#SBATCH -c 1
#SBATCH --mem=32GB
module load python/3.9.0
python3 nltkTokenize.py
