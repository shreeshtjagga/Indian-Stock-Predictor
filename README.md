# Indian Stock Market Predictor (NSE)

This project is an implementation of a **machine learning–based stock market prediction system** developed using Python and Streamlit. It provides an interactive web application where users can select NSE-listed stocks and obtain predictions for the **next trading day price direction (UP or DOWN)** along with an **estimated next-day price**.

The project demonstrates the application of **machine learning, feature engineering, and financial data analysis** using real-world stock market data.

---

## Overview

The project uses the **yfinance** library to fetch historical stock market data and applies the **XGBoost Classifier** to predict short-term price movement. Technical indicators such as **Simple Moving Average (SMA)**, **Exponential Moving Average (EMA)**, and **daily returns** are used to enhance the prediction process.

---

## Why XGBoost is Used

XGBoost (Extreme Gradient Boosting) is used in this project because it is highly effective for **structured and tabular data** such as stock market prices. It can capture **non-linear relationships** between technical indicators and price movement, which are common in financial markets.

Additionally, XGBoost provides:
- High prediction accuracy with relatively small datasets  
- Fast training and inference performance  
- Built-in regularization to reduce overfitting  
- Probabilistic confidence scores for classification  

These properties make XGBoost suitable for **short-term directional stock prediction**.

---

## Features

- Predicts next NSE trading day price direction (UP / DOWN)  
- Estimates next-day stock price based on recent volatility  
- Displays prediction confidence score  
- Uses Indian Standard Time (IST) for market logic  
- Automatically handles weekends  
- Deployed as an interactive web application using Streamlit  

---

## Technologies Used

- **Language:** Python  
- **Libraries:** pandas, numpy, scikit-learn, xgboost, yfinance  
- **Framework:** Streamlit  
- **Machine Learning Algorithm:** XGBoost Classifier  
- **Type:** Web-based Machine Learning Application  

---

## How It Works

1. The user selects one or more NSE-listed stocks from the interface.  
2. Historical stock data is fetched using Yahoo Finance.  
3. Technical indicators are computed through feature engineering.  
4. An XGBoost model is trained on historical price movement data.  
5. The model predicts the next-day price direction and confidence score.  
6. An estimated next-day price is calculated using recent volatility.  

---

# Disclaimer
- This project is for **Educational purposes** only and **does not provide financial or investment advice**. 
- Sole puropse of the porject is to explain the XGBoost Framework to which provides both the **Regression Model (XGBRegressor)** and **Classification Model (XGBClassifer)**

---

```bash
git clone https://github.com/rayfin774/indian-stock-predictor.git
cd indian-stock-predictor

