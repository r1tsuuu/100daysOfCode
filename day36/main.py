import os
import requests
import datetime
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# -------------------- STEP 1: Alpha Vantage --------------------
alphavantage_api_key = os.environ.get("ALPHAVANTAGE_API_KEY")
alphavantage_endpoint = "https://www.alphavantage.co/query"

alphavantage_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "datatype": "json",
    "apikey": alphavantage_api_key
}

response = requests.get(alphavantage_endpoint, params=alphavantage_parameters)
stock_data = response.json()["Time Series (Daily)"]

# Get last two market days (safe for weekends)
dates = list(stock_data.keys())
yesterday = dates[0]
day_before_yesterday = dates[1]

yesterday_price = float(stock_data[yesterday]["4. close"])
day_before_price = float(stock_data[day_before_yesterday]["4. close"])

def check_price_change(day1: float, day2: float) -> float:
    return ((day1 - day2) / day2) * 100

price_change = check_price_change(yesterday_price, day_before_price)

# -------------------- STEP 2: News API --------------------
news_api_key = os.environ.get("NEWS_API_KEY")
news_api_endpoint = "https://newsapi.org/v2/everything"

news_parameters = {
    "q": COMPANY_NAME,
    "apiKey": news_api_key,
    "pageSize": 3,
    "sortBy": "publishedAt",
    "language": "en"
}

def get_news(change: float) -> list:
    if abs(change) < 5:
        return []

    response = requests.get(news_api_endpoint, params=news_parameters)
    data = response.json()

    if "articles" not in data:
        return []

    return data["articles"][:3]

news_content = get_news(price_change)

# -------------------- STEP 3: Twilio --------------------
# Twilio Trial accounts cannot reliably send SMS to Philippine (+63) numbers.
# Even if the number is verified, outbound SMS to PH is often blocked on trial
# due to carrier and fraud restrictions.

def send_messages(phone_number: str):
    twilio_sid = os.environ.get("TWILIO_ACCOUNT_SID")
    twilio_token = os.environ.get("TWILIO_AUTH_TOKEN")
    twilio_from = os.environ.get("TWILIO_PHONE_NUMBER")  # MUST be real Twilio number

    client = Client(twilio_sid, twilio_token)

    emoji = "🔺" if price_change > 0 else "🔻"
    percent = round(abs(price_change), 2)

    for article in news_content:
        message_body = (
            f"{STOCK}: {emoji}{percent}%\n"
            f"Headline: {article['title']}\n"
            f"Brief: {article['description']}"
        )

        client.messages.create(
            from_=twilio_from,
            to=phone_number,
            body=message_body
        )

# Send only if there is news
if news_content:
    send_messages("+639876543210")
