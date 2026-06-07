# UIS2 Computational Analysis

This repository contains data files, reference scripts, structure-modeling inputs,
and molecular-docking configuration files associated with the study
["Mechanistic Insights into Plasmodium eIF2alpha Dephosphorylation by UIS2 via Computational Methods"](https://pmc.ncbi.nlm.nih.gov/articles/PMC12132543/).

The materials here document the computational analyses of UIS2 essentiality and
expression, AlphaFold-based protein-structure modeling, and docking of
salubrinal against the UIS2 model. The scripts are provided as methodological
references and are not intended to be run directly without adaptation to the
original computing environment and file paths.

## Repository Structure

```text
UIS2/
├── Knockout screen and scRNAseq/
│   ├── essential_gene.py
│   ├── scRNAseq_expression.py
│   ├── essentialgenelist.xlsx
│   ├── pb-ss2-set1-ss2-data.csv
│   └── pb-ss2-set1-ss2-exp.csv
├── Structure modeling/
│   ├── *.fasta
│   └── *.sh
├── Molecular Docking/
│   ├── config_UIS2_ZINC000001910965_active.txt
│   ├── UIS2_ranked_0.pdbqt
│   └── ZINC000001910965.pdbqt
└── README.md
```

## Contents

### Knockout Screen and scRNA-seq

The `Knockout screen and scRNAseq/` directory includes source data and Python
reference scripts illustrating:

- analyzing PlasmoGEM phenotype-screening data to evaluate UIS2 and related
  translation-initiation factors;
- visualizing single-cell RNA-seq expression patterns from the Malaria Cell
  Atlas; and
- generating publication-style scatter plots and UMAP visualizations.

### Structure Modeling

The `Structure modeling/` directory contains FASTA inputs and Slurm submission
script examples used for AlphaFold 2.3.1 modeling of UIS2, eIF2alpha, UIS2
fragments, and UIS2-eIF2alpha complexes.

These scripts were prepared for a specific HPC environment and include
cluster-specific module names, scratch paths, resource requests, and email
settings.

### Molecular Docking

The `Molecular Docking/` directory contains AutoDock Vina input files for
docking salubrinal against the UIS2 structural model, including receptor and
ligand PDBQT files and an example Vina configuration file.

## Citation

If you use this repository, please cite the associated publication:

Su Wu et al. "Mechanistic Insights into Plasmodium eIF2alpha Dephosphorylation
by UIS2 via Computational Methods."

Publication link:
<https://pmc.ncbi.nlm.nih.gov/articles/PMC12132543/>

## Contact

For questions or additional information, please contact:

Su Wu  
su_wu@hms.harvard.edu
