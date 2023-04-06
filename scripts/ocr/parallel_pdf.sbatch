#!/bin/bash
#SBATCH --job-name=myarrayjob
#SBATCH --output=test_job.%j.out
#SBATCH --error=test_job.%j.err
#SBATCH -p hns
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --array=1-2
ml load system imagemagick/7.0.7-2
ml load system tesseract/5.1.0
ml load system ghostscript/9.53.2
file=$(ls /home/users/bcritt/pdfs/*.pdf | sed -n ${SLURM_ARRAY_TASK_ID}p)
./pdf_convert.sh -in $file

