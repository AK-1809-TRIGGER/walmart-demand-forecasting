# Walmart Sales Forecasting & Inventory Risk Intelligence System

## Overview

This project is an end-to-end retail demand forecasting and inventory risk intelligence system built using Walmart’s historical sales dataset. The objective of the project is to analyze large-scale retail sales data, identify seasonal demand patterns, forecast future sales, and detect departments with high stockout risk using time-series forecasting techniques and business analytics.

The project combines Exploratory Data Analysis (EDA), statistical forecasting, and business intelligence techniques to generate actionable retail insights for inventory planning and sales optimization.

---

# Problem Statement

Retail chains such as Walmart face major challenges in accurately forecasting weekly sales and maintaining optimal inventory levels across multiple stores and departments. Incorrect demand forecasting may lead to:

* Stockouts during peak demand periods
* Overstocking and increased storage costs
* Revenue loss during holiday seasons
* Inefficient supply chain planning

The goal of this project is to build a forecasting and risk analysis pipeline capable of:

* Understanding historical sales behavior
* Identifying seasonal and holiday demand spikes
* Forecasting future weekly sales
* Detecting departments at inventory risk
* Supporting business decision-making using analytical insights

---

# Dataset Information

The project uses Walmart’s historical retail dataset containing weekly sales records.

## Dataset Statistics

* Total Records: 241,338
* Total Features: 20
* Stores: 25
* Departments: 80
* Time Period: February 2010 – October 2012

## Files Used

### train.csv

Contains weekly sales data for each store and department.

### stores.csv

Contains store metadata such as store type and size.

### features.csv

Contains external factors affecting sales:

* Temperature
* Fuel Price
* CPI
* Unemployment
* MarkDown values
* Holiday information

---

# Technologies Used

## Programming Language

* Python

## Libraries & Frameworks

* Pandas
* NumPy
* Matplotlib
* Seaborn
* Statsmodels
* Facebook Prophet
* Scikit-learn

## Development Environment

* Jupyter Notebook
* VS Code

---

# Project Workflow

## 1. Data Collection & Integration

The following datasets were merged:

* train.csv
* stores.csv
* features.csv

Data merging was performed using:

* Store
* Date

The final merged dataset was saved as:

```text
merged_data.csv
```

---

# 2. Data Preprocessing

The preprocessing stage included:

* Date conversion to datetime format
* Handling missing values
* Feature extraction:

  * Year
  * Month
  * Week
* Duplicate checks
* Dataset validation

---

# 3. Exploratory Data Analysis (EDA)

Extensive EDA was performed to understand sales behavior and demand patterns.

## Analysis Performed

### Weekly Sales Trend Analysis

Analyzed overall sales movement over time.

### Holiday Sales Analysis

Compared holiday vs non-holiday sales performance.

### Top Performing Stores

Identified stores generating the highest revenue.

### Seasonal Demand Analysis

Detected monthly and yearly seasonality patterns.

### Department-Wise Sales Analysis

Compared sales distribution across departments.

### Volatility Analysis

Measured sales fluctuations using standard deviation and average sales.

---

# Data Visualizations

The following visualizations were generated:

* Weekly Sales Trend
* Holiday vs Non-Holiday Sales
* Top Stores by Revenue
* Seasonal Heatmap
* Forecast Comparison Graphs
* Stockout Risk Visualization
* Model Performance Comparison

---

# Forecasting Models Used

The project compares multiple forecasting approaches for weekly sales prediction.

---

## 1. Naive Baseline Model

A simple baseline model was created using previous sales values as forecasts.

### Purpose

* Establish a benchmark performance
* Compare advanced forecasting models against a simple approach

---

## 2. ARIMA Model

ARIMA (AutoRegressive Integrated Moving Average) was used for statistical time-series forecasting.

### ARIMA Configuration

```text
order = (1,1,1)
seasonal_order = (1,1,0,52)
```

### Why ARIMA?

ARIMA is effective for:

* Trend analysis
* Sequential time-series forecasting
* Stationary data modeling

### Features

* Captures temporal dependencies
* Handles seasonality
* Uses lag-based forecasting

---

## 3. Facebook Prophet Model

Facebook Prophet was implemented for advanced forecasting with seasonality handling.

### Prophet Features

* Automatic trend detection
* Weekly seasonality
* Yearly seasonality
* Holiday-aware forecasting
* Robust handling of missing data

### Why Prophet?

Prophet performs well on business time-series data with:

* Seasonal demand spikes
* Holiday effects
* Non-linear trends

### Forecasting Capability

* 12-week future sales forecasting
* Trend decomposition
* Seasonal pattern analysis

---

# Model Evaluation Metrics

The models were evaluated using:

## RMSE

Root Mean Squared Error

Measures prediction error magnitude.

## MAE

Mean Absolute Error

Measures average forecasting error.

---

# Inventory Risk Detection

A stockout risk detection module was implemented to identify high-risk departments.

## Method Used

Volatility Score:

```text
Volatility = Standard Deviation / Average Sales
```

Departments with high volatility were flagged as:

```text
At Risk
```

## Business Use Case

This helps retailers:

* Prepare inventory before peak demand
* Reduce stockout probability
* Improve supply chain planning

---

# Key Insights

## Business Insights Generated

* Holiday weeks significantly increase weekly sales
* Certain stores consistently outperform others
* Q4 months show major seasonal spikes
* High volatility departments are more prone to stockouts
* Prophet performed better than baseline forecasting methods

---

# Repository Structure

```text
walmart-demand-forecasting/
│
├── data/
├── notebooks/
├── src/
├── charts/
├── outputs/
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Future Improvements

Possible future enhancements include:

* LSTM-based deep learning forecasting
* Real-time forecasting API
* Streamlit dashboard deployment
* Automated retraining pipeline
* Store-wise model optimization
* Inventory recommendation engine

---

# Conclusion

This project demonstrates the application of machine learning, statistical forecasting, and business analytics in solving real-world retail forecasting problems. By combining ARIMA, Facebook Prophet, EDA, and inventory risk analysis, the system provides valuable insights for demand forecasting and operational planning.

The project highlights practical skills in:

* Time-series forecasting
* Data analytics
* Statistical modeling
* Business intelligence
* Retail demand analysis
* Machine learning workflows
