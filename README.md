# Automotive Market Intelligence & Price Prediction System

An end-to-end Machine Learning and Business Intelligence solution designed to analyze automotive auction data, extract strategic market insights, and deploy a real-time price prediction system.

---

## Overview

This project provides a data-driven framework to evaluate vehicle market values, identify pricing inefficiencies, and predict final sale prices based on key vehicle attributes. The solution covers the entire data lifecycle:

1. **Data Cleaning & Analysis:** Processing 500,000+ automotive auction records to handle missing values, correct data types, and eliminate outliers.
2. **Exploratory Data Analysis (EDA):** Identifying linear and non-linear relationships between variables such as Manheim Market Report (MMR) values, vehicle condition scores, odometer readings, and final selling prices.
3. **Feature Engineering:** Creating domain-specific indicators to highlight market dynamics and price deviations.
4. **Predictive Modeling:** Developing and optimizing machine learning pipelines using Scikit-Learn and XGBoost.
5. **Business Intelligence:** Building an interactive Power BI dashboard for executive reporting, performance monitoring, and market trend analysis.
6. **Web Deployment:** Exposing the best-performing model via a Streamlit web application for real-time inference.

---

## Features

### Feature Engineering

* **Vehicle Age:** Calculated from the model year and transaction year.
* **PriceVsMMR:** Absolute difference between the selling price and the estimated wholesale market value (MMR).
* **MarketSignal:** Categorical classification labeling vehicles as "Undervalued", "Overpriced", or "Fair Value" to assist auction buyers in discovering profit opportunities.

### Machine Learning Pipeline

* Preprocessing via `ColumnTransformer` (StandardScaler for numerical data, OneHotEncoder for categorical data).
* Outlier removal using the Interquartile Range (IQR) method.
* Model evaluation comparing baseline algorithms (Ridge Regression) against advanced ensemble techniques (XGBoost Regressor).
* Model serialization using `joblib` for rapid inference.

### Power BI Dashboard Architecture & Analytics

* **Executive KPI Panel:** Displays top-level metrics including Total Revenue, Average Vehicle Selling Price, Total Units Sold, and Overall Market Deviation relative to MMR.
* **Market Inefficiency & Arbitrage Matrix:** Visualizes the "Market Signal" distribution, allowing users to slice data by vehicle make, body type, and state to instantly isolate undervalued inventory with high profit margins.
* **Pricing Drivers & Correlation Analysis:** Features cross-filtering visuals that analyze the non-linear relationship between Odometer (Mileage), Condition Scores, and Sale Price across different model years.
* **Brand Equity & Depreciation Trends:** Compares price retention rates and average selling prices across major automotive manufacturers over time.
* **Advanced DAX Calculations:** Utilizes custom DAX measures for dynamic time-intelligence calculations, moving averages, conditional formatting triggers, and price-difference ratios (`[PriceVsMMR]` and `[MarketBeatRate]`).

### Streamlit Web Application

* Interactive user interface allowing parameter inputs (Make, Model, Year, Condition, Mileage, MMR).
* Instant price estimation powered by the trained machine learning backend.

---

## Technology Stack

* **Language:** Python
* **Data Processing & EDA:** Pandas, NumPy, Matplotlib, Seaborn
* **Machine Learning:** Scikit-Learn, XGBoost, Joblib
* **Business Intelligence:** Power BI, DAX
* **Deployment:** Streamlit
* **Environment:** Jupyter Notebook, Git

---

## Business Impact

* **Inventory Optimization:** Enables dealerships and auction buyers to instantly spot undervalued cars based on historical market trends.
* **Risk Mitigation:** Minimizes overpayment risks by evaluating condition-adjusted price expectations against market baseline indicators.
* **Automated Valuation:** Reduces manual appraisal time by leveraging an automated machine learning pipeline.
