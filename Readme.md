
# Netflix Movies & TV Shows – End-to-End Data Analysis Project

## 📋 Project Overview

This project follows a complete data science pipeline for analyzing the Netflix Titles dataset. It starts from raw data inspection and progresses through data cleaning, feature engineering, exploratory data analysis (EDA), machine learning, database integration, and data export for dashboard creation.

The primary goal is to demonstrate comprehensive data analysis skills, from data wrangling to predictive modeling, using Python and popular data science libraries.

## 📚 Table of Contents

- [Installation](#installation)
- [Dataset](#dataset)
- [Project Steps](#project-steps)
  - [Step 1: Install Required Libraries](#step-1-install-required-libraries)
  - [Step 2: Import Required Libraries](#step-2-import-required-libraries)
  - [Step 3: Load Dataset](#step-3-load-dataset)
  - [Step 4: Data Inspection](#step-4-data-inspection)
  - [Step 5: Data Cleaning](#step-5-data-cleaning)
  - [Step 6: Feature Engineering](#step-6-feature-engineering)
  - [Step 7: Exploratory Data Analysis (EDA)](#step-7-exploratory-data-analysis-eda)
  - [Step 8: Save Cleaned Data to Excel](#step-8-save-cleaned-data-to-excel)
  - [Step 9: Working with SQLite3](#step-9-working-with-sqlite3)
  - [Step 10: Machine Learning – Predicting Content Type](#step-10-machine-learning--predicting-content-type)
- [Key Insights](#key-insights)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [How to Run](#how-to-run)
- [Skills Demonstrated](#skills-demonstrated)
- [Future Improvements](#future-improvements)
- [Author](#author)

## 🛠 Installation

1. Ensure you have Python installed (version 3.7 or higher recommended).
2. Clone this repository or download the project files.
3. Navigate to the project directory.
4. Install the required libraries using pip:

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

## 📊 Dataset

- **Source**: Netflix Movies & TV Shows dataset (netflix_titles.csv)
- **Size**: 8,807 rows and 12 columns
- **Key Columns**:
  - `show_id`: Unique identifier
  - `type`: Movie or TV Show
  - `title`: Content title
  - `director`: Director name(s)
  - `cast`: Cast members
  - `country`: Country of origin
  - `date_added`: Date added to Netflix
  - `release_year`: Original release year
  - `rating`: Content rating
  - `duration`: Duration (minutes for movies, seasons for TV shows)
  - `listed_in`: Genres/categories
  - `description`: Content description

## 🚀 Project Steps

### Step 1: Install Required Libraries

Upgrade pip and install dependencies from requirements.txt.

### Step 2: Import Required Libraries

Import necessary libraries for data handling (pandas, numpy) and visualization (matplotlib, seaborn).

### Step 3: Load Dataset

Load the Netflix dataset from the CSV file into a pandas DataFrame.

### Step 4: Data Inspection

- Examine the first and last few rows
- Check dataset size and shape
- Review column names and data types
- Analyze missing values and duplicates
- Generate descriptive statistics

**Key Findings**:
- 8,807 rows, 12 columns
- No duplicates
- Missing values in director, cast, country, date_added, rating, duration
- Most columns are categorical; release_year is numeric
- Date columns stored as strings

### Step 5: Data Cleaning

- Standardize column names (lowercase, underscores)
- Handle missing values by filling with appropriate defaults
- Convert date_added to datetime format
- Extract year_added and month_added features
- Verify no nulls remain in critical columns

**Approach**:
- Avoid dropping rows to prevent data loss
- Use 'Unknown' for missing categorical data
- Preserve date_added nulls to avoid artificial data

### Step 6: Feature Engineering

Create new features for enhanced analysis:
- `is_movie`: Binary indicator (1 for Movie, 0 for TV Show)
- `primary_country`: First country from country list
- `primary_genre`: First genre from listed_in
- `content_age`: Years between release and addition to Netflix
- `duration_num`: Numeric duration value
- `movie_duration_min`: Duration for movies
- `tv_seasons`: Number of seasons for TV shows
- `release_decade`: Decade of release (e.g., 2010)

### Step 7: Exploratory Data Analysis (EDA)

Perform comprehensive analysis with visualizations:

1. **Content Type Distribution**: Movies vs TV Shows count
2. **Growth Over Years**: Trend of content additions
3. **Movies vs TV Shows Growth**: Comparative yearly trends
4. **Top Countries**: Content production by country (top 15)
5. **Movie Duration Distribution**: Histogram of movie lengths
6. **TV Show Seasons**: Distribution of season counts
7. **Content Ratings**: Frequency of different ratings
8. **Top Genres**: Most common content categories
9. **Top Actors**: Most frequent cast members
10. **Stand-Up Comedy**: Analysis of comedy content

**Key Insights**:
- Movies dominate the library
- Rapid growth post-2015
- Few countries produce most content
- Most movies: 80-120 minutes
- Most TV shows: 1-3 seasons
- Popular genres: Drama, Comedy, International
- Stand-up comedy primarily as movies

### Step 8: Save Cleaned Data to Excel

Export the cleaned and engineered DataFrame to an Excel file (netflix_cleaned_data.xlsx) for reporting and dashboard creation.

### Step 9: Working with SQLite3

- Create and connect to a SQLite database (netflix_analysis.db)
- Store the DataFrame as a table
- Run sample queries for verification and analysis

### Step 10: Machine Learning – Predicting Content Type

- Prepare data by selecting relevant features
- Encode categorical variables
- Train a Logistic Regression model to predict Movie vs TV Show
- Evaluate model performance
- Analyze feature importance

## 🔍 Key Insights

- **Content Composition**: ~70% Movies, ~30% TV Shows
- **Growth Pattern**: Exponential increase in content additions since 2015
- **Geographic Distribution**: United States dominates, followed by India and UK
- **Duration Trends**: Movies average ~100 minutes; TV shows mostly 1-2 seasons
- **Genre Preferences**: Drama, Comedy, and International content most prevalent
- **Rating Distribution**: TV-MA and TV-14 most common ratings
- **Model Performance**: Logistic Regression achieves 99.6% accuracy in content type prediction

## 🛠 Technologies Used

- **Python**: Core programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Matplotlib**: Data visualization
- **Seaborn**: Statistical data visualization
- **Scikit-learn**: Machine learning (Logistic Regression)
- **SQLite3**: Database operations
- **Jupyter Notebook**: Interactive development environment

## 📁 Project Structure

```
Project of Data Analyst/
│
├── data/
│   └── netflix_titles.csv      # Raw dataset
├── main.ipynb                  # Main analysis notebook
├── netflix_cleaned_data.xlsx   # Cleaned data export
├── netflix_analysis.db         # SQLite database
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── project_report.md           # Detailed project report
├── .gitignore                  # Git ignore rules
└── LICENSE                     # MIT License
```

## ▶️ How to Run

1. Ensure all dependencies are installed (see Installation)
2. Open `main.ipynb` in Jupyter Notebook or JupyterLab
3. Run cells sequentially from top to bottom
4. The notebook will generate visualizations, export files, and train the ML model

## 🎯 Skills Demonstrated

- Data Cleaning and Preprocessing
- Feature Engineering
- Exploratory Data Analysis
- Data Visualization
- Machine Learning (Classification)
- Database Operations (SQLite)
- Data Export (Excel)
- Problem-Solving with Real-World Data
- Python Programming Best Practices

## 🔮 Future Improvements

- Build interactive dashboards (Power BI, Tableau, or Streamlit)
- Implement more advanced ML models (Random Forest, XGBoost)
- Add time series forecasting for content growth
- Create a web application for data exploration
- Incorporate additional datasets for richer analysis

## 👨‍💻 Author

**Vaibhav Mangla**  
Aspiring Data Analyst  
Passionate about data-driven insights and storytelling

---

⭐ If you found this project helpful, feel free to star the repository!
