#!/bin/bash
#SBATCH --job-name=pdf
#SBATCH --output=/home/users/%u/out/pdf.%j.out
#SBATCH --error=/home/users/%u/err/pdf.%j.err
#SBATCH -p hns
#SBATCH --ntasks=1 # Run a single task 
#SBATCH --mem-per-cpu=8gb # Memory per processor 
#SBATCH --array=1-2

ml load system imagemagick/7.0.7-2
ml load system tesseract/5.1.0
ml load system ghostscript/9.53.2
file=$(ls /home/users/bcritt/pdfs/*.pdf | sed -n ${SLURM_ARRAY_TASK_ID}p)
./parallel_pdf_convert.sh -in $file

