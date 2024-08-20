#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 16:35:51 2023

Bioinformatics analysis and visualization of essential genes in Plasmodium
Author: Su Wu
"""

import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from adjustText import adjust_text

# Configure matplotlib for consistent font rendering in publications
plt.rcParams["pdf.fonttype"] = 42
plt.rcParams["ps.fonttype"] = 42
plt.rcParams['figure.figsize'] = (15, 15)
pd.options.mode.chained_assignment = None  # Disable SettingWithCopyWarning

# Define directories
data_file_directory = "/home/suwu/Documents/Bioinformatics_analysis/Malaria/Essential_genes"
output_directory = "/home/suwu/Documents/Bioinformatics_analysis/Malaria/Essential_genes"

# Load and filter essential genes data
essential = pd.read_excel(os.path.join(data_file_directory, "essentialgenelist.xlsx"))
filtered_essential = essential[essential['Product'].notnull()]

# Filter genes involved in translation or serine/threonine protein phosphatases
translation_genes = filtered_essential[
    filtered_essential['Product'].str.contains('translation|serine/threonine protein phosphatase, putative', na=False) |
    filtered_essential['Name'].str.contains('IK2|IK1|EIF', na=False)
]

def plot_essential(adjust=False):
    """Plot essential genes, highlighting those involved in translation-related processes."""
    plt.figure(figsize=(10, 10))
    sns.scatterplot(data=essential, x="Relative growth rate", 
                    y="Confidence", hue="Phenotype", alpha=0.9, s=25)
    
    texts = [
        plt.text(x, y, s, size=12)
        for x, y, s in zip(translation_genes['Relative growth rate'], 
                           translation_genes['Confidence'], 
                           translation_genes['Name'])
    ]
    
    plt.xlabel('Relative Growth Rate')
    plt.ylabel('Confidence')
    
    if adjust:
        adjust_text(texts, arrowprops=dict(arrowstyle='fancy', color='k', lw=1))
    
    output_path = os.path.join(output_directory, "output", "essential_plot.pdf")
    plt.savefig(output_path, dpi=300, edgecolor='w')
    plt.show()

# Generate the essential gene plot
plot_essential(adjust=True)
