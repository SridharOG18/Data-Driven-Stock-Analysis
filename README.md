# Data-Driven Stock Analysis: Organizing, Cleaning, and Visualizing Market Trends

## Skills Utilized
- Pandas, Python, SQL
- Power BI, Streamlit
- Data Cleaning & Transformation
- Statistical Analysis
- Data Visualization

## Domain
Finance / Data Analytics

## Project Overview
The Stock Performance Dashboard provides a comprehensive visualization and analysis of Nifty 50 stocks' performance over the past year. The project processes daily stock data, extracts key performance metrics, and visualizes top-performing stocks in terms of price changes and average stock metrics. The dashboard is interactive and built using Streamlit and Power BI, aiding investors, analysts, and enthusiasts in making informed decisions.

## Business Use Cases
1. **Stock Performance Ranking**: Identify the top 10 best and worst-performing stocks.
2. **Market Overview**: Summary of average stock performance and percentage of gainers vs losers.
3. **Investment Insights**: Identify consistently growing or declining stocks.
4. **Decision Support**: Insights on price trends, volatility, and market behavior.

## Approach
### Data Extraction & Transformation
- Extracted stock data from YAML files.
- Transformed it into CSV format, organizing by stock symbols.
- Loaded data into an SQL database for analysis.

### Data Analysis & Visualization
1. **Volatility Analysis**
   - Calculated daily returns.
   - Computed standard deviation of returns to measure volatility.
   - Visualized top 10 most volatile stocks using bar charts.

2. **Cumulative Return Over Time**
   - Calculated cumulative returns for each stock.
   - Plotted a line chart of cumulative returns for the top 5 performing stocks.

3. **Sector-wise Performance**
   - Classified stocks by sector.
   - Analyzed average yearly returns per sector.
   - Visualized sector performance using bar charts.

4. **Stock Price Correlation**
   - Computed correlation between stock prices.
   - Created a heatmap to visualize correlations.

5. **Top 5 Gainers and Losers (Monthly)**
   - Identified monthly top gainers and losers.
   - Created bar charts for each month showing top 5 gainers and losers.

## Dataset
- Contains daily stock price data for Nifty 50 stocks.
- Includes columns: `Ticker, Close, High, Low, Open, Volume, Stock Date, Daily Return, Yearly Return, Cumulative Return, Sector`.

## Results
- Interactive Power BI and Streamlit dashboards visualizing stock trends.
- Insights into stock market trends, volatility, and sector performance.
- A structured SQL database for efficient querying and analysis.

## Technologies Used
- **Languages**: Python, SQL
- **Database**: MySQL/PostgreSQL
- **Visualization Tools**: Power BI, Streamlit
- **Libraries**: Pandas, Matplotlib, SQLAlchemy

## Project Deliverables
- **SQL Database**: Clean and structured stock data.
- **Python Scripts**: Data processing and analysis.
- **Power BI Dashboard**: Visual stock performance insights.
- **Streamlit Application**: Interactive data exploration tool.

## Guidelines Followed
- Efficient and optimized SQL queries.
- Modular and well-structured Python scripts.
- Clear and interactive visualizations.
- Comprehensive documentation.
