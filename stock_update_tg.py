import yfinance as yf
import time
import requests
import pandas as pd  

# Telegram message sending function
def send_telegram_message(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {"chat_id": chat_id, "text": message}
    try:
        response = requests.post(url, data=data, timeout=10)
        response.raise_for_status()
        print("Message sent successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send message: {e}")

# Define stop prices
stop_prices = {
    "KRSTL.IS": 5.98,
    "SAYAS.IS": 43.48,
    "MOBTL.IS": 4.27,
    "ISSEN.IS": 9.32,
    "AZTEK.IS": 48.36,
    "MIATK.IS": 43.0,
}

# Dictionary to hold previous prices
previous_prices = {}

# Function to get stock price
def get_stock_price(stock_code):
    try:
        stock = yf.Ticker(stock_code)
        price = stock.history(period="1d")["Close"].iloc[-1]
        if pd.isna(price):
            raise ValueError("Stock price could not be retrieved.")
        return price
    except Exception as e:
        print(f"An error occurred while retrieving the price for {stock_code}: {e}")
        return None

# Stop price check function
def check_stop_price(stock_code, price):
    stop_price = stop_prices.get(stock_code)
    if stop_price and price <= stop_price:
        return f"{stock_code} has reached the stop price: {price} TL"
    return None

# Telegram bot information
bot_token = " "#your telegram bot token
chat_id = " "#your telegram chat id

# List of stock symbols
stocks = list(stop_prices.keys())

# Main loop
while True:
    try:
        for stock_code in stocks:
            price = get_stock_price(stock_code)
            if price is None:
                continue  # Skip to the next stock if price cannot be retrieved

            # Price change and message sending
            if stock_code not in previous_prices:
                previous_prices[stock_code] = price
                message = f"Initial price for {stock_code}: {price:.2f} TL"
                send_telegram_message(bot_token, chat_id, message)
                continue

            # Calculate price change and create message
            previous_price = previous_prices[stock_code]
            price_change = price - previous_price
            percent_change = (price_change / previous_price) * 100

            if price_change > 0:
                message = f"{stock_code} price increased by {price_change:.2f} TL ({percent_change:.2f}%) and the new price is: {price} TL"
            elif price_change < 0:
                message = f"{stock_code} price decreased by {-price_change:.2f} TL ({-percent_change:.2f}%) and the new price is: {price:.2f} TL"
            else:
                message = f"{stock_code} price remained the same. The new price is: {price:.2f} TL"

            # Send message
            send_telegram_message(bot_token, chat_id, message)

            # Check stop price
            stop_check = check_stop_price(stock_code, price)
            if stop_check:
                send_telegram_message(bot_token, chat_id, stop_check)

            # Update previous price
            previous_prices[stock_code] = price

        time.sleep(1800)  # Wait for 30 minute
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        time.sleep(1800)