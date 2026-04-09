# Netflix Content Classifier

An end-to-end data science project for analyzing Netflix's catalog, engineering reusable features, persisting curated datasets, and training machine learning models to classify titles as either **Movie** or **TV Show**.

## Executive Summary

This project turns the public Netflix titles dataset into a reproducible analytics and machine learning pipeline. It covers the full workflow from raw ingestion through cleaning, feature engineering, exploratory analysis, database persistence, and model training.

The repository is notebook-first, but the artifacts are organized so the outputs are reusable outside the notebooks as well. Cleaned data, feature-engineered data, evaluation plots, and serialized models are all committed for review and downstream use.

## What This Project Demonstrates

- Data inspection and quality assessment on a real-world catalog dataset.
- Non-destructive cleaning and standardization of text, date, and categorical fields.
- Feature engineering for both analysis and prediction tasks.
- Exploratory data analysis with trend, distribution, and category-level views.
- SQLite integration for relational querying and persistence.
- Model comparison across multiple classifier families.
- Artifact export for reproducibility and portfolio presentation.

## Dataset

The raw dataset contains Netflix titles with metadata such as release year, date added, rating, duration, country, cast, director, and description.

The project is organized into a bronze-silver-gold data flow:

- Bronze: `data/bronze/netflix_titles.csv`
- Silver: `data/silver/Silver_Cleaned_Netflix_Data.csv`
- Gold: `data/gold/Netflix_Featured_Scaled_Data.csv`

The processed dataset is also stored in `database/netflix.db` for SQL-based analysis.

## Methodology

### 1. Data Inspection and Cleaning

The first notebook standardizes column names, checks duplicates, inspects missing values, and converts date fields into analysis-friendly types. Cleaning is designed to preserve rows rather than discard records unnecessarily.

### 2. Feature Engineering

The second notebook creates modeling and analysis features, including temporal fields, content duration measures, primary country and genre extraction, and derived indicators for movie versus TV-show structure. Numerical features are also scaled for modeling.

### 3. Exploratory Data Analysis

The third notebook explores catalog composition and content trends through visual analysis of:

- title type distribution
- release and addition trends
- country distribution
- rating patterns
- duration patterns
- genre composition
- actor frequency

### 4. SQLite Persistence

The fourth notebook writes the curated dataset to SQLite so it can be queried with SQL and used as a structured analytical asset.

### 5. Machine Learning

The fifth notebook trains and compares three classifier families:

- Logistic Regression
- Random Forest
- XGBoost

Each model is evaluated in baseline and tuned form. The best-performing tuned XGBoost result produces a perfect confusion matrix on the evaluated split, with 548 true negatives and 1,214 true positives.

## Repository Structure

```text
Netflix-Content-Classifier/
├── data/
│   ├── bronze/   # Raw source data
│   ├── silver/   # Cleaned dataset
│   └── gold/     # Feature-engineered dataset
├── database/     # SQLite database
├── model_images/ # Saved evaluation plots
├── models/       # Serialized model artifacts
├── notebook/     # Project notebooks
├── requirements.txt
├── setup.py
└── README.md
```

## Notebook Breakdown

- `01_Data_Inspection_&_Cleaning.ipynb` - initial inspection, missing value handling, type normalization, and clean export.
- `02_Feature_Engineering.ipynb` - feature extraction, scaling, and model-ready dataset preparation.
- `03_EDA.ipynb` - distribution analysis, trend analysis, and visualization.
- `04_sqlite3.ipynb` - loading the processed data into SQLite and validating the persisted output.
- `05_ML.ipynb` - model training, tuning, evaluation, and artifact export.

## Deliverables

The repository includes the following generated outputs:

- Cleaned CSV in the silver layer.
- Feature-engineered and scaled CSV in the gold layer.
- SQLite database for relational analysis.
- Serialized logistic regression, random forest, and XGBoost models.
- Confusion matrix and ROC curve plots for baseline and tuned models.
- Feature importance visualization for XGBoost.

## Technology Stack

- Python
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- xgboost
- sqlite3
- Jupyter Notebook

## Installation

```bash
pip install -r requirements.txt
```

For editable local development:

```bash
pip install -e .
```

## How to Run

1. Open the notebooks in the `notebook/` folder.
2. Execute them in order, beginning with data inspection and cleaning.
3. Review the generated artifacts in `data/silver/`, `data/gold/`, `database/`, `models/`, and `model_images/`.

## Reproducibility Notes

- The repository is designed to be run notebook-by-notebook.
- Generated artifacts are already present in the repository for convenience.
- `requirements.txt` is intentionally minimal and aligned with the notebook workflow.
- `setup.py` supports editable installation for local experimentation.

## Author

Vaibhav Mangla
