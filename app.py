
# Install these once only :
# pip install streamlit yfinance pandas numpy scikit-learn xgboost pytz

import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
from xgboost import XGBClassifier
from datetime import datetime, timedelta
import pytz
import logging

logging.getLogger("yfinance").setLevel(logging.CRITICAL)
st.set_page_config(page_title="Indian Stock Predictor", layout="wide")
st.title("Indian Stock Market Predictor ")
st.write("Predicts **next NSE trading day direction & estimated price**")

ist = pytz.timezone("Asia/Kolkata")
now = datetime.now(ist)

market_open = now.replace(hour=9, minute=15, second=0, microsecond=0)

def next_trading_day(d):
    d = d + timedelta(days=1)
    while d.weekday() >= 5:
        d += timedelta(days=1)
    return d

prediction_day = now.date() if now < market_open else next_trading_day(now.date())
st.info(f"Prediction for: **{prediction_day}** (IST)")


stocks = [
    "INFY.NS", "TCS.NS", "RELIANCE.NS", "HDFCBANK.NS", "ICICIBANK.NS",
    "SBIN.NS", "ITC.NS", "LT.NS", "AXISBANK.NS", "KOTAKBANK.NS",
    "HCLTECH.NS", "WIPRO.NS", "BHARTIARTL.NS", "MARUTI.NS",
    "ASIANPAINT.NS", "ULTRACEMCO.NS", "SUNPHARMA.NS", "TITAN.NS",
    "BAJFINANCE.NS", "BAJAJFINSV.NS", "NESTLEIND.NS", "POWERGRID.NS",
    "ONGC.NS", "NTPC.NS", "COALINDIA.NS", "TATAMOTORS.NS",
    "DRREDDY.NS", "HEROMOTOCO.NS", "GRASIM.NS", "ADANIPORTS.NS",
    "JSWSTEEL.NS"
]

selected_stocks = st.sidebar.multiselect("Select NSE Stocks", options=stocks, placeholder="Choose stocks"
)

def add_features(df):
    df["SMA"] = df["Close"].rolling(10).mean()
    df["EMA"] = df["Close"].ewm(span=10).mean()
    df["Return"] = df["Close"].pct_change()
    df.dropna(inplace=True)
    return df

@st.cache_data(ttl=300)
def download_data(stock):
    df = yf.download(
        stock,
        period="1y",
        interval="1d",
        progress=False,
        threads=False
    )
    df.dropna(axis=1, how="all", inplace=True)
    return df
def train_model(X, y, split):
    model = XGBClassifier(
        n_estimators=25,
        max_depth=3,
        learning_rate=0.1,
        eval_metric="logloss",
        verbosity=0
    )
    model.fit(X[:split], y[:split])
    return model

if st.button(" Predict NSE Stocks", type="primary"):

    if not selected_stocks:
        st.warning("Please select at least one stock")
    else:
        results = []

        for stock in selected_stocks:
            df = download_data(stock)

            if df.empty or len(df) < 60:
                continue

            df = df[["Open", "High", "Low", "Close", "Volume"]]
            df = add_features(df)

            df["Target"] = (df["Close"].shift(-1) > df["Close"]).astype(int)
            df.dropna(inplace=True)

            X = df.drop("Target", axis=1)
            y = df["Target"]

            split = int(len(df) * 0.8)

            model = train_model(X, y, split)

            latest = X.iloc[-1:]
            pred = int(model.predict(latest)[0])
            conf = float(model.predict_proba(latest)[0][pred])

       
            conf = max(conf, 0.55)

            today_price = round(float(df["Close"].iloc[-1]), 2)
            volume = int(df["Volume"].iloc[-1])

            avg_move = float(df["Return"].tail(20).abs().mean() * 100)

            if pred == 1:
                direction = "UP "
                next_price = today_price * (1 + avg_move / 100)
            else:
                direction = "DOWN"
                next_price = today_price * (1 - avg_move / 100)

            next_price = round(float(next_price), 2)

            results.append({
                "Stock": stock.replace(".NS", ""),
                "Today Price (₹)": today_price,
                "Estimated Next Price (₹)": next_price,
                "Direction": direction,
                "Volume": f"{volume:,}",
                "Confidence (%)": f"{conf * 100:.1f}"
            })

        if results:
            st.subheader(" NSE Stock Comparison")
            st.dataframe(
                pd.DataFrame(results),
                use_container_width=True,
                hide_index=True
            )
        else:
            st.warning("No valid predictions available")
st.caption("**Educational project only. Not financial advice.**")
st.caption(" ALL RIGHTS RESERVED TO **SHREESHT** 2025-2027")



