Stock Price Tracker with Telegram Notifications

Overview

This Python script fetches real-time stock prices using Yahoo Finance (yfinance) and sends notifications via Telegram when significant price changes occur. It also monitors predefined stop prices and alerts the user if a stock reaches or falls below its stop price.

Features

Retrieves real-time stock prices.

Sends price updates to a Telegram chat.

Tracks price changes and calculates percentage differences.

Alerts the user if a stock reaches a predefined stop price.

Runs continuously with updates every 30 minutes.

Requirements

To run this script, ensure you have the following dependencies installed:

pip install yfinance requests pandas

Setup

Get a Telegram Bot Token

Create a Telegram bot using BotFather.

Save your bot_token from BotFather.

Find Your Chat ID

Send a message to your bot.

Use the API endpoint https://api.telegram.org/bot<your_bot_token>/getUpdates to retrieve your chat ID.

Modify the Script

Replace bot_token and chat_id with your own values.

Update the stop_prices dictionary with the stocks you want to track.

Usage

Run the script with:

python stock_tracker.py

Configuration

You can modify the stop_prices dictionary to set custom stop prices for stocks.

The script checks stock prices every 30 minutes (time.sleep(1800)). You can adjust this interval as needed.

Example Output

Initial price for KRSTL.IS: 6.10 TL
KRSTL.IS price decreased by -0.12 TL (-1.97%) and the new price is: 5.98 TL
KRSTL.IS has reached the stop price: 5.98 TL

Disclaimer

This script is for informational purposes only and should not be used for financial decisions. Always conduct your own research before making investment choices.


