#! /usr/bin/bash
#SBATCH --job-name=test_job
#SBATCH --output=/home/users/%u/out/test_job.%j.out
#SBATCH --error=/home/users/%u/err/test_job.%j.err
#SBATCH --time=02:00:00
#SBATCH -p hns
#SBATCH -c 1
#SBATCH --mem=16GB
module load python/3.9.0
pip3 install --user -r requirements.txt
python3 -m spacy download en_core_web_sm
python3 geocode.py
