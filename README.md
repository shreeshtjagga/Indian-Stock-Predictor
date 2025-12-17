# 📈 Indian Stock Market Predictor (NSE)

🔗 Live App: https://indian-stock-predictor.streamlit.app/

## 📌 Project Description
The Indian Stock Market Predictor is a machine learning–based web application developed using Python and Streamlit. The project focuses on predicting the next NSE trading day price movement (UP or DOWN) and providing an estimated next-day price for selected Indian stocks.

The application fetches real-time and historical stock market data using the Yahoo Finance API and processes this data through feature engineering techniques such as moving averages and return calculations. A supervised machine learning model is then trained on historical data to identify patterns in price movements.

This project demonstrates how artificial intelligence and machine learning can be applied to financial markets for decision-support systems. It highlights concepts such as data preprocessing, feature engineering, classification algorithms, and performance optimization in a real-world financial domain.

The goal of this project is educational—to understand how stock data can be analyzed programmatically and how predictive models can assist in market analysis, not to provide trading or investment advice.

## 🧠 Machine Learning Used
- Algorithm: XGBoost Classifier  
- Learning Type: Supervised Machine Learning  
- Problem Type: Binary Classification (Price UP / DOWN)  
- Features Used: Open, High, Low, Close, Volume, SMA, EMA, Daily Returns  
- Data Source: Yahoo Finance (yfinance)

## 🚀 Features
- Predicts next trading day stock direction  
- Estimates next-day stock price  
- Displays prediction confidence  
- Uses Indian Standard Time (IST)  
- Automatically handles weekends  
- Optimized using Streamlit caching  
- Deployed as an interactive web application  

## 🧰 Technologies
- Python  
- Streamlit  
- XGBoost  
- scikit-learn  
- Pandas, NumPy  
- yfinance  

## 📂 Project Structure
- app.py → Main Streamlit application  
- requirements.txt → Python dependencies  
- README.md → Project documentation  

## ⚠️ Disclaimer
This project is created strictly for educational and learning purposes. It does not provide financial, trading, or investment advice.

##  To Clone this Resposiory
git clone https://github.com/YOUR_USERNAME/indian-stock-predictor.git
cd indian-stock-predictor


