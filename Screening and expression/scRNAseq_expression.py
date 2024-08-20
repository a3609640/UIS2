#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Single-cell RNA-seq expression analysis in Plasmodium
Author: Su Wu
"""

import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from adjustText import adjust_text
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import matplotlib as mpl

# Configure matplotlib for consistent font rendering in publications
plt.rcParams["pdf.fonttype"] = 42
plt.rcParams["ps.fonttype"] = 42
plt.rcParams['figure.figsize'] = (15, 15)
pd.options.mode.chained_assignment = None  # Disable SettingWithCopyWarning

# Define directories
data_file_directory = "/home/suwu/Documents/Bioinformatics_analysis/Malaria/Essential_genes"
output_directory = "/home/suwu/Documents/Bioinformatics_analysis/Malaria/Essential_genes"

# Load stage and expression data
stage = pd.read_csv(os.path.join(data_file_directory, "pb-ss2-set1-ss2-data.csv"))
expression = pd.read_csv(os.path.join(data_file_directory, "pb-ss2-set1-ss2-exp.csv"))

def plot_expression(gene_name, parameter):
    """Plot gene expression for a specific gene across different cell stages."""
    UIS2_expression = expression[expression['Unnamed: 0'].str.contains(gene_name)].T
    UIS2_expression.columns = UIS2_expression.iloc[0]
    UIS2_expression = UIS2_expression[1:].rename_axis('CELL_ID').reset_index()
    
    stage_UIS2_expression = pd.merge(stage, UIS2_expression, on='CELL_ID')
    stage_UIS2_expression = stage_UIS2_expression[stage_UIS2_expression[parameter] == 'mouse']
    
    plt.figure(figsize=(10, 10))
    ax = sns.scatterplot(data=stage_UIS2_expression, 
                         x="UMAP_1", 
                         y="UMAP_2", 
                         hue=gene_name,  
                         palette='OrRd', hue_norm=(0,14), 
                         alpha=0.9, s=25)
    
    ax.set(title=gene_name)
    ax.get_legend().remove()
    
    cbaxes = inset_axes(ax, width="20%", height="2%", loc=2) 
    ax.figure.colorbar(plt.cm.ScalarMappable(cmap="OrRd", norm=mpl.colors.Normalize(vmin=0, vmax=14)),
                       cax=cbaxes, orientation='horizontal', label="RNAseq count")
    
    output_path = os.path.join(output_directory, "output", f"{gene_name}_{parameter}_plot.pdf")
    plt.savefig(output_path, dpi=300, edgecolor='w', bbox_inches='tight')
    plt.show()

# Example: Plotting gene expression for specific genes
plot_expression('PBANKA_0212100', 'HOST')  # eIF2alpha
plot_expression('PBANKA_0412800', 'HOST')  # eIF4E
plot_expression('PBANKA_1411300', 'HOST')  # eIF4G
plot_expression('PBANKA_1331900', 'HOST')  # eIF4A
plot_expression('PBANKA_1206100', 'HOST')  # eIF3D

# Plot cell division control genes
plot_expression('PBANKA_0602000', 'HOST')  # ORC1
plot_expression('PBANKA_1137900', 'HOST')  # Proliferating cell nuclear antigen 1, putative

# Plot late schizont stage genes from atlas publication
plot_expression('PBANKA_1351500', 'HOST')  # CDPK5 (Calcium-dependent protein kinase 5)
plot_expression('PBANKA_0931200', 'HOST')  # HSP101


def plot_stage(parameter):
    """Plot UMAP of cell stages colored by a specific parameter."""
    plt.figure(figsize=(10, 10))
    ax = sns.scatterplot(data=stage, x="UMAP_1", y="UMAP_2", 
                         hue=parameter, palette='Dark2', alpha=0.9, s=25)
    
    plt.legend(loc='upper left')
    output_path = os.path.join(output_directory, "output", f"{parameter}_plot.pdf")
    plt.savefig(output_path, dpi=300, edgecolor='w', bbox_inches='tight')
    plt.show()

# Generate stage plots for different parameters
plot_stage('STAGE_LR')
plot_stage('HOST')

# Extract and plot UIS2 expression across stages
uis_genes = ['PBANKA_1328000', 'PBANKA_0212100', 'PBANKA_1126900', 
             'PBANKA_0205800', 'PBANKA_0719200']

UIS_expression = expression[expression['Unnamed: 0'].str.contains('|'.join(uis_genes), na=False)].T
UIS_expression.columns = UIS_expression.iloc[0]
UIS_expression = UIS_expression[1:].rename_axis('CELL_ID').reset_index()

stage_UIS_expression = pd.merge(stage, UIS_expression, on='CELL_ID')

# (Add plotting or further analysis of `stage_UIS_expression` as needed)
