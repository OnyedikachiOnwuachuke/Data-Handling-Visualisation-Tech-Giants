# importting the libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# Load data
stock_google = pd.read_csv('GOOGLE.csv')
stock_samsung = pd.read_csv('SAMSUNG.csv')
stock_fb = pd.read_csv('FB.csv')
stock_apple = pd.read_csv('APPLE.csv')

# Convert 'Date' column to datetime format
stock_google['Date'] = pd.to_datetime(stock_google['Date'])
stock_samsung['Date'] = pd.to_datetime(stock_samsung['Date'])
stock_fb['Date'] = pd.to_datetime(stock_fb['Date'])
stock_apple['Date'] = pd.to_datetime(stock_apple['Date'])

# Create new column for months
stock_google['Month'] = stock_google['Date'].dt.strftime('%b')
stock_samsung['Month'] = stock_samsung['Date'].dt.strftime('%b')
stock_fb['Month'] = stock_fb['Date'].dt.strftime('%b')
stock_apple['Month'] = stock_apple['Date'].dt.strftime('%b')

# Calculate total sold
stock_google['Total sold'] = stock_google['Close'] * stock_google['Volume']
stock_samsung['Total sold'] = stock_samsung['Close'] * stock_samsung['Volume']
stock_fb['Total sold'] = stock_fb['Close'] * stock_fb['Volume']
stock_apple['Total sold'] = stock_apple['Close'] * stock_apple['Volume']


# Create the dashboard-infographics visualization
fig = plt.figure(figsize=(12, 6))
fig.patch.set_facecolor('grey')  # Set the figure background color

# Define the grid layout
gs = gridspec.GridSpec(2, 2, figure=fig)

# Plot 1: Line plot for stock prices
ax1 = fig.add_subplot(gs[0, 0])
ax1.plot(stock_google['Month'], stock_google['Close'], label='Google')
ax1.plot(stock_samsung['Month'], stock_samsung['Close'], label='Samsung')
ax1.plot(stock_fb['Month'], stock_fb['Close'], label='Facebook')
ax1.plot(stock_apple['Month'], stock_apple['Close'], label='Apple')
ax1.set_xlabel('Month')
ax1.set_ylabel('Stock Price')
ax1.set_title('Stock Prices')
ax1.legend()

# Plot 2: Pie chart for market share
ax2 = fig.add_subplot(gs[0, 1])
market_share = [30, 25, 20, 25]
labels = ['Google', 'Samsung', 'Facebook', 'Apple']
ax2.pie(market_share, labels=labels, autopct='%1.1f%%')
ax2.set_title('Market Share')

# Plot 3: Bar chart for total sold
ax3 = fig.add_subplot(gs[1, 0])
total_sold = [stock_google['Total sold'].sum(), stock_samsung['Total sold'].sum(
), stock_fb['Total sold'].sum(), stock_apple['Total sold'].sum()]
ax3.bar(labels, total_sold)
ax3.set_xlabel('Company')
ax3.set_ylabel('Total Sold')
ax3.set_title('Total Sold')

# Plot 4: Histogram for stock volume
ax4 = fig.add_subplot(gs[1, 1])
ax4.hist(stock_google['Volume'], bins=10, alpha=0.5, label='Google')
ax4.hist(stock_samsung['Volume'], bins=10, alpha=0.5, label='Samsung')
ax4.hist(stock_fb['Volume'], bins=10, alpha=0.5, label='Facebook')
ax4.hist(stock_apple['Volume'], bins=10, alpha=0.5, label='Apple')
ax4.set_xlabel('Volume')
ax4.set_ylabel('Frequency')
ax4.set_title('Stock Volume')
ax4.legend()

# Overall Title and Explanation
fig.suptitle('Tech Giants Stock Market Dashboard 2021', fontsize=16)
fig.text(0.5, 0.02,  'This dashboard-infographics visualisation shows a summary of stock market trends for top tech companies in 2021', ha='center')

# Adjust spacing between subplots
fig.tight_layout(pad=3)

#saving the infographics in .png format
plt.savefig('22034665.png', dpi=300)

# Display the dashboard-infographics visualization
plt.show()
