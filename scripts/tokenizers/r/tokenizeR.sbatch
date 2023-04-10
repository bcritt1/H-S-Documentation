#!/usr/bin/bash
#SBATCH --job-name=tokenize
#SBATCH --output=/home/users/bcritt/out/tokenize.%j.out
#SBATCH --error=/home/users/bcritt/err/tokenize.%j.err
#SBATCH --time=02:00:00
#SBATCH -p hns
#SBATCH -c 1
#SBATCH --mem=32GB
module load R/4.2.0
Rscript tokenize.r
