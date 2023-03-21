#!/usr/bin/bash
#SBATCH --job-name=test_job
#SBATCH --output=/home/users/bcritt/out/test_job.%j.out
#SBATCH --error=/home/users/bcritt/err/test_job.%j.err
#SBATCH -p owners
#SBATCH -c 1
#SBATCH --mem=32GB
module load R/4.2.0
Rscript word2vec.R