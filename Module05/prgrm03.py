# use subplots to demonstrate various aspects of stock market
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

# download stock data
stock = "AAPL"
data = yf.download(stock, start="2020-01-01", end="2020-12-31")  # get 1 year data

# prepare data for subplots
price_data = data["Close"]
volume_data = data["Volume"]
short_moving_averages = price_data.rolling(window=20).mean()
long_moving_averages = price_data.rolling(window=50).mean()

# create subplots
_, axes = plt.subplots(nrows=3, figsize=(12, 12), sharex=True)

# plot price trends
axes[0].plot(price_data.index, price_data, label=stock)
axes[0].set_title("Price Trends")
axes[0].set_ylabel("Price")
axes[0].legend()

# plot volume trends
axes[1].bar(volume_data.index, volume_data, label="Volume")
axes[1].set_title("Volume Trends")
axes[1].set_ylabel("Volume")
axes[1].legend()

# plot moving averages
axes[2].plot(
    short_moving_averages.index, short_moving_averages, label="Short Moving Averages"
)
axes[2].plot(
    long_moving_averages.index, long_moving_averages, label="Long Moving Averages"
)
axes[2].set_title("Moving Averages")
axes[2].set_xlabel("Data")
axes[2].set_ylabel("Price")
axes[2].legend()

# save the plots
plt.tight_layout()
plt.show()
