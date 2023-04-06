#!/usr/bin/bash
#SBATCH --job-name=huggingface
#SBATCH --output=/home/users/$USER/out/huggingface.%j.out
#SBATCH --error=/home/users/$USER/err.huggingface.%j.err
#SBATCH -p hns
#SBATCH -c 1
#SBATCH --mem=32GB
module load python/3.9.0
python3 huggingface.py
