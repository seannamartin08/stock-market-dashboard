#📊 Stock Market Dashboard
Interactive Data Analysis using Python & Streamlit

This project provides a complete workflow for analyzing stock market data and visualizing insights through an interactive Streamlit dashboard.
It includes data cleaning, exploratory data analysis (EDA), feature engineering, visualizations, and a fully functional automated dashboard.

⭐ Project Highlights
✅ 1. End-to-End Stock Market Analysis

Data loading & cleaning

Handling missing values

Automatic column mapping (Date, Close, Ticker, etc.)

Feature engineering: returns, log returns, moving averages

✅ 2. Visual Insights

Time-series charts

Moving average plots

Volatility curves

Correlation heatmaps

Pairplots

Return distributions

Volume analysis

✅ 3. Streamlit Interactive Dashboard

Upload any CSV and auto-detect key columns

Visualize stock trends instantly

Choose tickers for analysis

View correlations & summary statistics

Prepared for predictive model integration

🗂 Project Structure
Stock-Market-Dashboard/
│── app_auto_fixed.py          # Streamlit web app
│── stocks_analysis.py         # Full EDA + feature engineering script
│── requirements.txt           # Project dependencies
│── README.md                  # Project documentation
│── data/
│     └── stocks.csv           # Sample dataset (optional)
│── images/
│     ├── heatmap.png          # Correlation heatmap
│     └── pairplot.png         # Pairplot visualization
│── models/
      └── rf_model.joblib      # (Optional) trained ML model

🚀 How to Run the Project
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Run the Streamlit Dashboard
streamlit run app_auto_fixed.py

3️⃣ Output

Once the app launches, you can:

Upload your own CSV

Explore stock trends

Visualize technical indicators

View summary statistics

Analyze correlations

🔍 Key Features Implemented
📌 Data Preprocessing

Auto column mapping (Date, Ticker, Close, etc.)

Handles file inconsistencies

Converts date formats

Sorts and groups by ticker

📌 Feature Engineering

Daily returns

Log returns

Rolling moving averages (7, 21, 50 days)

Rolling volatility

📌 EDA Visualizations

Time-series charts

Heatmaps

Pairplots

Volume charts

Return distributions

🧠 Future Enhancements

Add machine learning forecasting (LSTM, ARIMA, Prophet)

Add technical indicators (RSI, MACD, Bollinger Bands)

Deploy Streamlit app online

Add portfolio analytics

Add real-time stock data integration

🎯 Overall Experience

Developing this stock market dashboard provided hands-on experience with financial data analysis, interactive visualization, and dashboard design. This project strengthened practical skills in Python, data cleaning, EDA, and Streamlit app development while offering insights into real-world stock behavior. The final dashboard bridges both analytical depth and user-friendly interactivity, making it a strong foundation for future enhancements like forecasting and portfolio management.

👤 Author

Seanna Martin
Data Analyst & Streamlit Developer
