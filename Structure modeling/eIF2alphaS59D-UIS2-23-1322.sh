#!/bin/bash

#SBATCH --partition=gpu_quad
#SBATCH --gres=gpu:a100:1,vram:80G
#SBATCH -c 12
#SBATCH --time=120:00:00
#SBATCH --mem=80G
#SBATCH --mail-type=ALL
#SBATCH --mail-user=su_wu@hms.harvard.edu

###

module load alphafold/2.3.1 gcc/9.2.0 cuda/11.7

alphafold.py \
--fasta_paths=/n/scratch/users/s/sw34/malaria/eIF2alphaS59D-UIS2-23-1322.fasta \
--model_preset=multimer \
--use_gpu \
--max_template_date=2022-01-01 \
--db_preset=full_dbs \
--output_dir=/n/scratch/users/s/sw34/malaria/ \
--data_dir=/n/shared_db/alphafold-2.3/
