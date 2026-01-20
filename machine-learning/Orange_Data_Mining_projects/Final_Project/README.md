# Final Project – Machine Learning Analysis

This final project integrates both **unsupervised and supervised machine learning techniques** using **Orange Data Mining**.  
The project explores data structure, clustering behavior, dimensionality reduction, and classification performance across multiple models.

All analyses are contained in:
- An **Orange workflow (`.ows`)** defining the full analytical pipeline
- An **HTML report** documenting results, visualizations, and interpretations

---

## Topics and Methods Covered

### Unsupervised Learning
- **K-Means Clustering**
  - Cluster formation and visualization
- **Hierarchical Clustering**
  - Ward linkage
  - Dendrogram-based cluster comparison
- **Cluster Visualization**
  - Scatter plots for cluster separation
- **Silhouette Analysis**
  - Evaluation of clustering quality

---

### Dimensionality Reduction
- **Principal Component Analysis (PCA)**
  - Scatter plots of principal components
  - Identification of important contributing features
- **t-SNE**
  - Nonlinear dimensionality reduction
  - Visualization of class and cluster structure

---

### Supervised Learning and Model Comparison
The following classification models were evaluated using confusion matrices and test metrics:

- **Logistic Regression**
- **Support Vector Machine (SVM)**
- **Naive Bayes**
- **Random Forest**

Performance comparisons were conducted across models using:
- Confusion matrices
- Test and score metrics

---

### Logistic Regression Feature Analysis
- Examination of **important features** under different regularization strengths:
  - C = 1
  - C = 0.030
- Comparison of:
  - Feature importance rankings
  - Model performance metrics at different C values

---

## Tools Used
- **Orange Data Mining**
- Visualization and evaluation widgets for:
  - Clustering
  - Classification
  - Feature selection
  - Model assessment

---

## Files in This Folder
- `final_project_workflow.ows` – Complete Orange Data Mining workflow
- `final_project_report.html` – Detailed report with figures, confusion matrices, and explanations

