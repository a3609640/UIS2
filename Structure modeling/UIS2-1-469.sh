#!/bin/bash

#SBATCH --partition=gpu_quad
#SBATCH --gres=gpu:rtx8000:1
#SBATCH -c 12
#SBATCH --time=120:00:00
#SBATCH --mem=80G
#SBATCH --mail-type=ALL
#SBATCH --mail-user=su_wu@hms.harvard.edu

###

module load alphafold/2.3.1 gcc/9.2.0 cuda/11.7

alphafold.py \
--fasta_paths=/n/scratch/users/s/sw34/malaria/UIS2-1-469.fasta \
--model_preset=monomer \
--use_gpu \
--max_template_date=2022-01-01 \
--db_preset=full_dbs \
--output_dir=/n/scratch/users/s/sw34/malaria/ \
--data_dir=/n/shared_db/alphafold-2.3/
