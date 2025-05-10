# hourly-stock-forecasting
Predicting hourly stock prices using sentiment analysis from Twitter and news headlines with deep learning (LSTM).
# Hourly Stock Price Prediction Using Sentiment Analysis

This project uses deep learning (LSTM) and real-time sentiment analysis from Twitter and financial news to predict hourly stock prices.

## 🔍 Objective
To explore how public sentiment affects short-term stock price movements and whether combining sentiment data with historical stock prices can improve forecasting accuracy.

## 🧠 Model
- LSTM neural network trained on:
  - Hourly stock OHLCV data
  - Aggregated sentiment scores from Twitter and news
- Sentiment tools: VADER, TextBlob, FinBERT

## 📊 Data Sources
- [Yahoo Finance](https://finance.yahoo.com/)
- Twitter API
- [FinViz](https://finviz.com/)

## 📂 Project Structure
hourly-stock-forecasting/
├── data/ # Stock and sentiment data
├── models/ # Saved LSTM model
├── notebooks/ # Jupyter notebook
├── outputs/ # Predictions, plots, metrics
├── requirements.txt # Python dependencies
├── README.md # This file
├── Project Report/


## 🚀 How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt

jupyter notebook notebooks/hourly-stock-forecasting.ipynb
📈 Results
R²: 0.89

MAE: 1.23

Trading Strategy Outperformed Buy-and-Hold by 16%

👨‍💻 Author
Muhammad Yousuf Rehan 
