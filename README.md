📈 yfinance – Yahoo Finance Data with Python

yfinance is a Python library that makes it simple to access Yahoo Finance market data. It allows you to download historical stock prices, financial statements, and other market information directly into pandas DataFrames for analysis, visualization, and trading strategies.

🚀 Features

Fetch historical stock price data (Open, High, Low, Close, Volume).

Download dividends, splits, and corporate actions.

Access real-time market data and financials.

Integrates seamlessly with pandas for analysis.

Lightweight and easy to use.

📦 Installation
pip install yfinance

🔧 Usage
import yfinance as yf

# Download historical data
data = yf.download("AAPL", start="2023-01-01", end="2023-12-31")

print(data.head())

📊 Example Output
                  Open        High         Low       Close   Adj Close   Volume
Date
2023-01-03  129.889999  130.259995  125.080002  125.070000  124.499153  112117500
2023-01-04  126.889999  128.660004  125.080002  127.989998  127.410301  89113600
...

🔍 Use Cases

Stock market research & analysis.

Backtesting trading strategies.

Building dashboards & financial apps.

Educational projects in finance and data science.

📚 Resources

yfinance PyPI

Official GitHub Repo

📜 License

This project is licensed under the MIT License.
