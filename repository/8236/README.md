# Automated Trading Bot  - 8236

**Language**: `Python`

**Lines of code**: `42`

## Description

This program is a Python script that implements a basic trading strategy for buying and selling stocks automatically. The bot retrieves real-time stock prices using the Alpha Vantage API and makes decisions based on a simple moving average crossover strategy. The bot will buy a stock when its short-term moving average crosses above its long-term moving average and sell when the opposite occurs.

Note: This is a sample program and should not be used for actual trading. Always use caution and consult with a professional before making any financial decisions.

## Code

``` Python
import requests
import json
import time

# Set API key and stock symbol
api_key = "YOUR_API_KEY"
symbol = "AAPL"

# Set moving average window sizes
short_window = 20
long_window = 50

# Initialize position
position = 0

while True:
    # Get current stock price
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"
    response = requests.get(url)
    data = json.loads(response.text)
    price = float(data["Global Quote"]["05. price"])

    # Get moving averages
    if len(prices) > long_window:
        short_ma = sum(prices[-short_window:]) / short_window
        long_ma = sum(prices[-long_window:]) / long_window

        # Buy if short MA crosses above long MA and we're not already long
        if short_ma > long_ma and position == 0:
            position = 1
            print("Buying at:", price)
        
        # Sell if short MA crosses below long MA and we're long
        elif short_ma < long_ma and position == 1:
            position = 0
            print("Selling at:", price)
    
    # Add current price to list of previous prices
    prices.append(price)

    # Wait for one minute before checking again
    time.sleep(60)

```

## Prompt

```
Make me a program in any language that is more than 20 lines of code long and is complex and interesting.

When you create the program make a title for it and a short description of what it does.
```