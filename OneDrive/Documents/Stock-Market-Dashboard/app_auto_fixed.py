# app_auto_fixed.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

st.set_page_config(page_title="Stock Market Dashboard", layout="wide")
st.title("📈 Stock Market Dashboard (Auto-Fix Bundle)")

st.markdown("Upload a CSV with **Date**, **Ticker**, and **Close** (or **Adj Close**) columns, or place `stocks.csv` in the same folder as this script.")

uploaded = st.file_uploader("Upload your stock CSV (optional)", type=["csv"])

if uploaded is not None:
    df = pd.read_csv(uploaded)
    st.success("File uploaded successfully!")
else:
    try:
        df = pd.read_csv("stocks.csv")
        st.info("Loaded bundled stocks.csv (from current folder)")
    except FileNotFoundError:
        st.warning("No CSV uploaded and no stocks.csv found in the folder. Upload a CSV to continue.")
        st.stop()

# Normalize column names to title case and strip spaces
df.columns = [c.strip().title() for c in df.columns]

# Find price column (Close/Adj Close)
close_cols = [c for c in df.columns if "Close" in c]
if not close_cols:
    st.error("Your CSV must contain a Close or Adj Close column.")
    st.stop()
price_col = close_cols[0]

# Ensure Date column exists; add Ticker if missing
if "Date" not in df.columns:
    st.error("Your CSV must contain a Date column.")
    st.stop()
if "Ticker" not in df.columns:
    df["Ticker"] = "SINGLE"
    st.info("No Ticker column found — added default Ticker='SINGLE' for single-stock CSVs.")

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df = df.dropna(subset=["Date"]).sort_values(["Ticker", "Date"]).reset_index(drop=True)

# Sidebar controls
tickers = sorted(df["Ticker"].unique())
sel = st.sidebar.selectbox("Select ticker", tickers)
min_date = df["Date"].min().date()
max_date = df["Date"].max().date()
date_range = st.sidebar.date_input("Date range", [min_date, max_date], min_value=min_date, max_value=max_date)

mask = (df["Ticker"] == sel) & (df["Date"] >= pd.to_datetime(date_range[0])) & (df["Date"] <= pd.to_datetime(date_range[1]))
view = df.loc[mask].sort_values("Date")

st.subheader(f"Price history — {sel}")
if view.empty:
    st.info("No data for selected ticker/date range.")
else:
    st.line_chart(view.set_index("Date")[price_col])

# Moving average overlay
st.subheader("Moving averages")
window = st.sidebar.slider("MA window (days)", 5, 60, 20)
if not view.empty:
    view["MA"] = view[price_col].rolling(window=window, min_periods=1).mean()
    st.line_chart(view.set_index("Date")[[price_col, "MA"]])

# Return distribution and rolling volatility
if not view.empty:
    view["Return"] = view[price_col].pct_change()
    view["LogReturn"] = np.log(view[price_col] / view[price_col].shift(1))
    st.subheader("Return distribution (selected range)")
    fig, ax = plt.subplots(figsize=(8,3))
    sns.histplot(view["Return"].dropna(), bins=50, kde=True, ax=ax)
    st.pyplot(fig)

    st.subheader("Rolling volatility (21-day, annualized)")
    view["Vol21"] = view["LogReturn"].rolling(window=21, min_periods=1).std() * np.sqrt(252)
    st.line_chart(view.set_index("Date")["Vol21"])

# Correlation heatmap across tickers
st.subheader("Correlation heatmap (returns across tickers)")
try:
    pivot = df.pivot(index="Date", columns="Ticker", values=price_col)
    corr = pivot.pct_change().dropna().corr()
    if corr.shape[0] >= 2:
        fig2, ax2 = plt.subplots(figsize=(6,4))
        sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", ax=ax2)
        st.pyplot(fig2)
    else:
        st.write("Need at least 2 tickers to show correlation.")
except Exception as e:
    st.write("Correlation heatmap error:", e)

st.info("Bundle app by ChatGPT — edit to extend features (modeling, download, etc.).")
