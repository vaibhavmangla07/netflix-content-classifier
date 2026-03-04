# Netflix Movies & TV Shows – End-to-End Data Science Project

## 📊 Project Overview

This is a **comprehensive end-to-end data science project** that demonstrates a complete data science pipeline. The project analyzes Netflix's content library to extract actionable insights about content distribution, production trends, and builds a predictive machine learning model for content classification.

**Goal:** Demonstrate professional data science skills from raw data to production-ready models.

---

## 🎯 Project Objectives

✅ Perform thorough data inspection and quality assessment  
✅ Implement robust data cleaning and preprocessing  
✅ Engineer meaningful features for enhanced analysis  
✅ Conduct exploratory data analysis (EDA) with visualizations  
✅ Build an ML model for content type prediction  
✅ Integrate data with database systems  
✅ Export clean data for dashboard creation  

---

## 📁 Project Structure

```
Netflix Data Science Project/
├── main.ipynb                    # Complete analysis notebook (92 cells)
├── data/
│   ├── netflix_titles.csv        # Raw dataset (8,807 records)
│   └── netflix_cleaned_data.xlsx # Processed data export (2.3 MB)
├── database/
│   └── netflix_analysis.db       # SQLite database (3.9 MB)
├── README.md                     # Project overview
├── project_report.md             # Detailed analysis report
└── requirements.txt              # Python dependencies
```

---

## 🚀 10-Step Data Science Pipeline

### 1️⃣ **Install & Import Libraries**
- Upgrade pip and install dependencies
- Import pandas, numpy, matplotlib, seaborn, scikit-learn

### 2️⃣ **Load Dataset**
- Load Netflix titles CSV: **8,807 rows × 12 columns**
- Data types: Primarily categorical with numeric release_year

### 3️⃣ **Data Inspection**
- Head/tail analysis
- Shape and size verification
- Missing value detection: **31,427 nulls identified**
- Duplicate check: **0 duplicates**
- Statistical summary

### 4️⃣ **Data Cleaning** ✨
- Standardize column names (lowercase, underscores)
- Strategic missing value handling (non-destructive):
  - Categorical → 'Unknown'
  - Numeric → 'Not Rated' / '0'
- Convert date_added to datetime format
- Extract year_added & month_added
- **Result:** 0 nulls, 100% data retention

### 5️⃣ **Feature Engineering**
Created **9 meaningful features**:
- `is_movie` – Binary indicator (Movie=1, TV Show=0)
- `primary_country` – First country from list
- `primary_genre` – First genre from list
- `content_age` – Years between release and Netflix addition
- `duration_num` – Numeric duration value
- `movie_duration_min` – Duration in minutes (movies)
- `tv_seasons` – Number of seasons (TV shows)
- `release_decade` – Decade categorization
- `year_added`, `month_added` – Temporal features

**Total Features:** 12 → **21 (75% increase)**

### 6️⃣ **Exploratory Data Analysis**
**10 Comprehensive Analyses:**
1. Content type distribution (Movies vs TV Shows)
2. Growth trends over years
3. Comparative growth (Movies vs TV Shows)
4. Top 15 countries by content
5. Movie duration distribution
6. TV show seasons distribution
7. Content ratings frequency
8. Top genres/categories
9. Prolific actors
10. Comedy content analysis

### 7️⃣ **Data Export**
- Excel export: `netflix_cleaned_data.xlsx` (2.3 MB)
- All 21 engineered features preserved
- Ready for business intelligence tools

### 8️⃣ **Database Integration**
- Create SQLite database: `netflix_analysis.db`
- Store processed data in relational format
- Execute sample queries for verification
- Enable SQL-based analysis

### 9️⃣ **Machine Learning** ⭐
**Content Type Prediction Model (Movie vs TV Show)**

**Enhancements Applied:**
- ✅ Advanced encoder with mapping dictionaries
- ✅ StandardScaler for feature scaling
- ✅ Optimized Logistic Regression parameters
- ✅ Balanced class weighting

**Performance:**
```
Accuracy:  99.48% ✅
Precision: 99.49%
Recall:    99.48%
F1-Score:  99.48%
AUC:       99.97%
```

---

## 📊 Key Findings

### Content Distribution
- **Movies:** 6,131 (69.6%) 🎬
- **TV Shows:** 2,676 (30.4%) 📺
- **Ratio:** 2.3:1 in favor of movies

### Growth Trends
- **Pre-2015:** Slow, steady growth
- **2015-2019:** Exponential growth (spike in 2019)
- **2020-2021:** Continued growth, slight moderation

### Geographic Insights
| Country | Count | % |
|---------|-------|---|
| United States | 3,211 | 36.5% |
| India | 1,010 | 11.5% |
| United Kingdom | 419 | 4.8% |
| Canada | 383 | 4.3% |
| Japan | 246 | 2.8% |

### Duration Patterns
- **Movies:** Average ~100 minutes (80-120 most common)
- **TV Shows:** Most have 1-3 seasons
- **Distribution:** Normal for movies, right-skewed for TV

### Popular Genres
1. Drama (2,416 titles)
2. International (1,500)
3. Comedy (1,243)
4. Action (939)
5. Thriller (853)

---

## 💻 Technical Stack

**Language & Libraries:**
- Python 3.7+
- **Data:** pandas, numpy
- **Visualization:** matplotlib, seaborn
- **Machine Learning:** scikit-learn
- **Database:** sqlite3
- **Environment:** Jupyter Notebook

**Tools & Techniques:**
- Data cleaning & preprocessing
- Feature engineering
- EDA with 10+ visualizations
- Categorical encoding
- Feature scaling (StandardScaler)
- Train-test split (80-20)
- Logistic Regression
- Model evaluation & metrics

---

## 📋 Installation & Usage

### Prerequisites
```bash
Python 3.7 or higher
pip package manager
```

### Installation
```bash
# Clone/download the project
cd "Project of Data Analyst"

# Install dependencies
pip install -r requirements.txt

# Open notebook
jupyter notebook main.ipynb
```

### Running the Analysis
1. Open `main.ipynb` in Jupyter
2. Run cells sequentially (Step 1-10)
3. View outputs and visualizations
4. Generated files appear in folder:
   - `netflix_cleaned_data.xlsx`
   - `netflix_analysis.db`

---

## 🎓 Skills Demonstrated

✅ **Data Engineering**
- Data cleaning (non-destructive approach)
- Missing value handling
- Data type conversion

✅ **Feature Engineering**
- Creating meaningful features (9 new)
- Domain knowledge application
- Feature extraction techniques

✅ **Exploratory Data Analysis**
- Statistical analysis
- Multiple perspectives
- Data visualization
- Insight extraction

✅ **Machine Learning**
- Model building
- Feature preprocessing
- Model evaluation
- Hyperparameter optimization

✅ **Database Management**
- SQLite integration
- Relational data modeling
- SQL queries

✅ **Data Visualization**
- matplotlib & seaborn
- Multiple plot types
- Professional styling

✅ **Professional Practices**
- Code organization
- Documentation
- Best practices
- Version control

---

## 📈 Performance Summary

### Data Quality
- **Records Retained:** 8,807/8,807 (100%)
- **Null Values Handled:** 31,427
- **Features Created:** 9 new features
- **Data Loss:** 0%

### Model Performance
- **Test Accuracy:** 99.48%
- **Training Accuracy:** 99.53%
- **Misclassifications:** 9 out of 1,742 (0.52%)
- **Balanced Performance:** Equal on both classes

### Deliverables
- ✅ Clean, documented notebook (92 cells)
- ✅ Processed Excel export (2.3 MB)
- ✅ SQLite database (3.9 MB)
- ✅ Comprehensive documentation

---

## 🔍 Files Description

| File | Size | Purpose |
|------|------|---------|
| **main.ipynb** | 540 KB | Complete analysis (92 cells) |
| **netflix_titles.csv** | 3.2 MB | Raw dataset |
| **netflix_cleaned_data.xlsx** | 2.3 MB | Processed data for BI tools |
| **netflix_analysis.db** | 3.9 MB | SQLite database |
| **README.md** | - | Project overview |
| **Project_Report.pdf** | - | Detailed technical report |
| **requirements.txt** | - | Python packages |

---

## 🎯 Use Cases

This project can be used for:
- **Portfolio Showcase** – Demonstrates complete data science skills
- **Learning Resource** – Step-by-step pipeline example
- **Production Blueprint** – Template for real-world projects
- **Business Intelligence** – Netflix content analysis insights

---

## 🚀 Next Steps

### Enhancement Ideas:
1. **Deploy as Dashboard** – Streamlit/Power BI visualization
2. **Advanced ML** – Random Forest, XGBoost comparison
3. **Cross-Validation** – k-fold validation for robustness
4. **API Service** – REST API for predictions
5. **Real-time Pipeline** – Automated data updates

---

##  Acknowledgments

- Netflix dataset from public data sources
- Python open-source community
- Jupyter Notebook platform

---

## 📝 Tips for Success

1. **Run sequentially:** Execute cells in order (don't skip steps)
2. **Check outputs:** Verify each step produces expected results
3. **Ask questions:** Understand why each step is important
4. **Experiment:** Modify parameters and see effects
5. **Document:** Take notes on key findings

---

**Happy Analyzing! 🎬📊**
