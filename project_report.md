# Netflix Movies & TV Shows Data Analysis Project Report

## Executive Summary

This report presents a comprehensive end-to-end data analysis of the Netflix Titles dataset, encompassing data cleaning, feature engineering, exploratory data analysis, machine learning modeling, and database integration. The project demonstrates the application of data science methodologies to extract meaningful insights from Netflix's content library, revealing trends in content production, distribution, and consumption patterns.

## Introduction

### Project Objectives
- Perform thorough data inspection and quality assessment
- Implement robust data cleaning and preprocessing techniques
- Engineer meaningful features for enhanced analysis
- Conduct exploratory data analysis to uncover patterns and trends
- Build a predictive model for content type classification
- Integrate data with SQLite database for querying capabilities
- Export cleaned data for dashboard and reporting purposes

### Dataset Description
The analysis utilizes the Netflix Movies & TV Shows dataset containing 8,807 entries with 12 attributes including content type, production details, temporal information, and categorical metadata.

## Methodology

### Step 1: Environment Setup
- Upgraded pip package manager
- Installed required dependencies from requirements.txt
- Verified library availability for data manipulation and visualization

### Step 2: Data Loading and Initial Inspection
- Loaded CSV dataset using pandas
- Performed preliminary examination of data structure
- Identified data types, missing values, and basic statistics

**Data Quality Assessment:**
- Dataset dimensions: 8,807 rows × 12 columns
- No duplicate records detected
- Missing values present in director (2,634), cast (825), country (831), date_added (10), rating (4), duration (3)
- Data types: Primarily object (categorical), with release_year as integer

### Step 3: Data Cleaning
- Standardized column names to lowercase with underscores
- Implemented strategic missing value handling:
  - Categorical fields filled with 'Unknown'
  - Preserved date_added nulls to maintain data integrity
- Converted date_added to datetime format
- Extracted temporal features: year_added, month_added
- Verified complete elimination of null values in processed columns

### Step 4: Feature Engineering
Created derived features to enhance analytical capabilities:

- **Binary Encoding**: is_movie (1 for Movie, 0 for TV Show)
- **Primary Extraction**: primary_country, primary_genre from multi-value fields
- **Temporal Features**: content_age (years between release and Netflix addition)
- **Duration Processing**: duration_num, movie_duration_min, tv_seasons
- **Categorical Grouping**: release_decade for trend analysis

### Step 5: Exploratory Data Analysis

#### Content Type Distribution
- Movies: ~70% of total content
- TV Shows: ~30% of total content
- Clear dominance of movie content in Netflix library

#### Temporal Trends
- Explosive growth in content additions post-2015
- Consistent upward trajectory in both movie and TV show acquisitions
- Year 2019 marked peak content addition year

#### Geographic Analysis
- United States: Primary content producer
- India and United Kingdom: Key international contributors
- Top 15 countries account for majority of Netflix content

#### Content Characteristics
- **Movie Duration**: Normal distribution centered around 90-110 minutes
- **TV Show Seasons**: Majority (1-3 seasons), with outliers reaching 15+ seasons
- **Ratings**: TV-MA and TV-14 most prevalent
- **Genres**: Drama, Comedy, and International content dominate

#### Cast and Production Analysis
- Identified most prolific actors across Netflix catalog
- Analyzed genre distribution and popularity metrics
- Examined stand-up comedy content patterns (primarily movie format)

### Step 6: Data Export and Database Integration

#### Excel Export
- Saved cleaned and engineered dataset to netflix_cleaned_data.xlsx
- Preserved all transformations for external analysis and dashboard creation

#### SQLite Database Operations
- Created netflix_analysis.db database
- Stored processed DataFrame as relational table
- Executed verification queries:
  - Total titles count
  - Content type distribution
  - Country-wise content aggregation
  - Yearly addition trends

### Step 7: Machine Learning Implementation

#### Model Development
- Selected relevant features: release_year, rating, primary_genre, primary_country, duration_num, content_age
- Encoded categorical variables using LabelEncoder
- Implemented Logistic Regression classifier

#### Model Evaluation
- Train-test split: 80-20 ratio (6,969 training, 1,742 testing samples)
- **Accuracy**: 99.6% (only 7 misclassifications out of 1,742 predictions)
- **Precision**: 99.6% (weighted average)
- **Recall**: 99.6% (weighted average)
- **F1-Score**: 99.6% (weighted average)
- **AUC Score**: 99.97% (near-perfect discriminative ability)
- Generated confusion matrix and ROC curve visualizations
- Balanced performance across both Movie and TV Show classes

#### Feature Importance Analysis
- Identified key predictors for content type classification
- Visualized coefficient magnitudes for model interpretability

## Key Findings and Insights

### Content Strategy Insights
1. **Dominant Content Type**: Movies represent Netflix's core content strategy
2. **Growth Acceleration**: Post-2015 expansion reflects aggressive content acquisition
3. **Geographic Focus**: Heavy reliance on US and select international markets
4. **Duration Preferences**: Content optimized for viewer attention spans

### Production Trends
1. **Genre Popularity**: Drama and comedy genres show highest production volumes
2. **Rating Distribution**: Mature content (TV-MA) most common, indicating adult audience targeting
3. **Season Economics**: Most TV shows designed for limited season runs

### Predictive Modeling Results
1. **Exceptional Model Performance**: Logistic Regression achieves 99.6% accuracy with AUC of 99.97%
2. **Robust Classification**: Only 7 misclassifications in 1,742 test predictions
3. **Balanced Performance**: Equal precision/recall for both Movie and TV Show classes
4. **Feature Effectiveness**: Content age and duration emerge as strongest predictors
5. **Practical Application**: Model can assist in content categorization and recommendation systems

## Technical Implementation

### Libraries and Tools
- **Data Processing**: pandas, numpy
- **Visualization**: matplotlib, seaborn
- **Machine Learning**: scikit-learn
- **Database**: sqlite3
- **Environment**: Jupyter Notebook

### Data Quality Outcomes
- Zero null values in processed dataset
- Consistent data types and formats
- Enhanced feature set for comprehensive analysis

## Conclusion

This project successfully demonstrates a complete data science workflow applied to real-world entertainment industry data. The analysis revealed Netflix's content strategy patterns, production trends, and audience targeting approaches.

### Achievements
- Comprehensive data cleaning without information loss
- Rich feature engineering enabling multi-dimensional analysis
- Thorough exploratory analysis uncovering actionable insights
- Successful machine learning implementation for content classification
- Seamless database integration and data export capabilities

### Business Implications
The findings provide valuable insights for content strategists, helping understand:
- Optimal content mix (movies vs. TV shows)
- Geographic market prioritization
- Genre and rating preferences
- Content lifecycle patterns

### Future Directions
- Dashboard development for interactive exploration
- Advanced predictive modeling with ensemble methods
- Time series forecasting for content growth prediction
- Web application deployment for broader accessibility

## Appendices

### Dataset Schema
- show_id: Unique identifier
- type: Content classification (Movie/TV Show)
- title: Content title
- director: Director information
- cast: Cast members
- country: Production country
- date_added: Netflix addition date
- release_year: Original release year
- rating: Content rating
- duration: Content length
- listed_in: Genre categories
- description: Content synopsis

### Project Deliverables
- `main.ipynb`: Complete analysis notebook with all steps
- `data/netflix_titles.csv`: Raw Netflix dataset
- `netflix_cleaned_data.xlsx`: Processed data for dashboards
- `netflix_analysis.db`: SQLite database with analysis table
- `README.md`: Project overview and usage guide
- `project_report.md`: Comprehensive project report
- `requirements.txt`: Python dependencies
- `.gitignore`: Version control exclusions
- `LICENSE`: Open source license

### Engineered Features
- year_added: Year of Netflix addition
- month_added: Month of Netflix addition
- is_movie: Binary movie indicator
- primary_country: Primary production country
- primary_genre: Primary genre category
- content_age: Years between release and addition
- duration_num: Numeric duration value
- movie_duration_min: Movie duration in minutes
- tv_seasons: TV show season count
- release_decade: Release decade grouping

---

**Report Generated**: February 5, 2026  
**Author**: Vaibhav Mangla  
**Project Duration**: End-to-End Data Analysis Implementation