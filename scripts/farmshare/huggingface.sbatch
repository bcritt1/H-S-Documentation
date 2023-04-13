#!/usr/bin/bash
#SBATCH --job-name=huggingface
#SBATCH --output=/home/users/%u/out/huggingface.%j.out
#SBATCH --error=/home/users/%u/err/huggingface.%j.err
#SBATCH -p hns
#SBATCH -c 1
#SBATCH --mem=32GB
module load anaconda3
conda install --channel "pytorch-nightly" pytorch torchvision torchaudio
conda install -c huggingface transformers
anaconda3 huggingface.py
