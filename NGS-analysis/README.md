
# R Next-Generation Sequencing (NGS) Analysis Portfolio

This repository contains a collection of R-based analyses demonstrating
experience with next-generation sequencing (NGS) data analysis, with a focus
on bulk RNA-seq, single-cell RNA-seq, functional enrichment, and integrative
cancer genomics workflows. The projects use real biological datasets and
widely adopted Bioconductor and Seurat-based methods.

## Projects Included

### Differential Expression Analysis (Bulk RNA-seq)
Performs differential gene expression analysis comparing tumor and normal
samples using the edgeR package. The workflow includes gene ID mapping,
filtering of duplicated and low-quality genes, TMM normalization, exploratory
analysis (MDS and BCV plots), exact testing, and generalized linear modeling
with patient as a blocking factor.

### Sample Relationships and Quality Control
Exploratory analysis of RNA-seq samples using DESeq2 to assess sample
relationships and data quality. Includes filtering of low-count genes,
rlog transformation, sample distance heatmaps, PCA, and clustering based on
highly variable genes.

### Enrichment Analysis
Functional enrichment analysis of differentially expressed genes using Gene
Ontology Biological Process (GO:BP). The analysis uses enrichGO to identify
overrepresented pathways and includes visualization with bar plots, dot plots,
gene–concept network plots, and heatmaps to support biological interpretation.

### Single-Cell RNA-seq Analysis
Analysis of single-cell RNA-seq data using the Seurat framework. The workflow
includes quality control filtering, normalization, identification of highly
variable genes, scaling, PCA, neighborhood graph construction, clustering,
UMAP visualization, differential expression between clusters, and cell-type
annotation using known marker genes and ScType-based scoring.

### Cancer Multi-Omics Analysis (TCGA GBM vs LGG)
Integrative analysis of TCGA glioblastoma (GBM) and lower-grade glioma (LGG)
samples combining DNA methylation and gene expression data. The workflow uses
GDC data retrieval, MultiAssayExperiment, and the ELMER framework to identify
differentially methylated probes, enhancer–gene relationships, enriched
transcription factor binding motifs, and candidate regulatory drivers
associated with tumor subtype differences.

### Integrative Final Project
A capstone analysis that combines multiple NGS techniques, including
differential expression analysis, enrichment analysis, and exploratory data
analysis, to demonstrate an end-to-end RNA-seq analysis workflow.

## Tools and Technologies
- R
- Bioconductor
- edgeR
- DESeq2
- Seurat
- ELMER
- clusterProfiler
- org.*.eg.db annotation packages
- ggplot2, pheatmap, and related visualization tools


