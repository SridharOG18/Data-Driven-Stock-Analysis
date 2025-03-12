import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime, timedelta
from sqlalchemy import create_engine
import seaborn as sns
import io
import matplotlib.pyplot as plt

#############################
## PART 1: Load Data  ##
#############################

@st.cache_data
def fetch_stock_data(tickers, start, end):
    data = {}
    for ticker in tickers:
        df = yf.download(ticker, start=start, end=end)
        if not df.empty:
            df['Ticker'] = ticker
            df['daily_return'] = df['Close'].pct_change()
            data[ticker] = df
    return pd.concat(data.values()) if data else pd.DataFrame()

#############################
## PART 2: UI Elements  ##
#############################

st.title('Stock Market Analysis Dashboard')
st.sidebar.header("User Inputs")

# Stock selection & date range
ticker_list = [
    'SBIN', 'BAJFINANCE', 'TITAN', 'ITC', 'TCS', 'LT', 'TATACONSUM', 'RELIANCE', 'HCLTECH', 'JSWSTEEL', 'ULTRACEMCO', 'POWERGRID', 'INFY', 'TRENT', 'BHARTIARTL', 'TATAMOTORS', 'WIPRO', 'TECHM', 'NTPC', 'HINDUNILVR', 'APOLLOHOSP', 'M&M', 'GRASIM', 'ICICIBANK', 'ADANIENT', 'ADANIPORTS', 'BEL', 'BAJAJFINSV', 'EICHERMOT', 'COALINDIA', 'MARUTI', 'INDUSINDBK', 'ASIANPAINT', 'TATASTEEL', 'HDFCLIFE', 'DRREDDY', 'SUNPHARMA', 'KOTAKBANK', 'SHRIRAMFIN', 'NESTLEIND', 'ONGC', 'CIPLA', 'BPCL', 'BRITANNIA', 'SBILIFE', 'HINDALCO', 'HEROMOTOCO', 'AXISBANK', 'HDFCBANK', 'BAJAJ-AUTO'
]
tickers = st.sidebar.multiselect("Select Stocks", ticker_list, default=['SBIN', 'BAJFINANCE'])
date_range = st.sidebar.date_input("Select Date Range", [datetime.today() - timedelta(days=365), datetime.today()])

#############################
## PART 3: Fetch & Process Data  ##
#############################

data = pd.read_csv("D:/Project_Stock/StockData_Updated.csv")
if data.empty:
    st.error("No stock data available. Try different selections.")
    st.stop()

data['stock_date'] = pd.to_datetime(data['stock_date'])  # Ensure datetime format
data['Cumulative Return'] = data.groupby('Ticker')['daily_return'].cumsum()
volatility = data.groupby('Ticker')['daily_return'].std().sort_values(ascending=False).head(10)

#############################
## PART 4: Charts & Analysis  ##
#############################

# Volatility Chart
st.subheader("Top 10 Most Volatile Stocks")
fig_vol = px.bar(volatility, x=volatility.index, y=volatility.values, title="Stock Volatility", labels={'x': 'Ticker', 'y': 'Volatility'})
st.plotly_chart(fig_vol)

# Cumulative Return Chart
st.subheader("Cumulative Returns of Top 5 Performing Stocks")
top_performers = data.groupby('Ticker')['Cumulative Return'].max().nlargest(5).index
data_top = data[data['Ticker'].isin(top_performers)]
fig_cum = px.line(data_top, x='stock_date', y='Cumulative Return', color='Ticker', title="Cumulative Returns of Top 5 Performing Stocks")
st.plotly_chart(fig_cum)

# Correlation Heatmap
st.subheader("Stock Price Correlation")
price_pivot = data.pivot(index='stock_date', columns='Ticker', values='close')
correlation_matrix = price_pivot.corr()
fig_corr = px.imshow(correlation_matrix, labels=dict(x="Ticker", y="Ticker", color="Correlation"), title="Stock Correlation Heatmap", color_continuous_scale='RdBu')
st.plotly_chart(fig_corr)

# Monthly Gainers/Losers
st.subheader("Monthly Top 5 Gainers & Losers")
data['Month'] = data['stock_date'].dt.strftime('%Y-%m')
monthly_returns = data.groupby(['Ticker', 'Month'])['daily_return'].sum().reset_index()

for month in monthly_returns['Month'].unique():
    with st.expander(f"Month: {month}"):
        df_month = monthly_returns[monthly_returns['Month'] == month]
        top_gainers = df_month.nlargest(5, 'daily_return')
        top_losers = df_month.nsmallest(5, 'daily_return')
        fig_gainers = px.bar(top_gainers, x='Ticker', y='daily_return', title=f"Top 5 Gainers - {month}")
        fig_losers = px.bar(top_losers, x='Ticker', y='daily_return', title=f"Top 5 Losers - {month}")
        st.plotly_chart(fig_gainers)
        st.plotly_chart(fig_losers)

# Sector-wise Performance
st.subheader("Sector-wise Performance")
sector_performance = data.groupby('sector')['yearly_return'].mean().reset_index()
sector_performance = sector_performance.sort_values(by='yearly_return', ascending=True)
fig_sector = px.bar(
    sector_performance, 
    x='sector', 
    y='yearly_return', 
    title="Average Yearly Return by Sector", 
    labels={'sector': 'Sector', 'yearly_return': 'Average Yearly Return (%)'}, 
    color='yearly_return', 
    color_continuous_scale='Blues'
)
fig_sector.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig_sector)