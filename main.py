import os
from dotenv import load_dotenv
load_dotenv()
from stocks import Stocks
from news import News
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla"
STOCKS_API = os.getenv("STOCKS_API")
NEWS_API = os.getenv("NEWS_API")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

stocks_object = Stocks(api=STOCKS_API)
data_stocks = stocks_object.get_prices()

if len(data_stocks) < 2:
    print("Not enough stock data")
    exit()

closes = [item["close"] for item in sorted(data_stocks, key=lambda x: x["date"])]
yesterday_price = closes[-1]
before_price = closes[-2]

diff = ((yesterday_price - before_price) / before_price) * 100

if abs(diff) >= 0:
    news_object = News(NEWS_API)
    data_news = news_object.get_news()
    articles = data_news.get("articles", [])[:3]

    emoji = "🔺" if diff > 0 else "🔻"
    text = f"TSLA: {emoji} {abs(diff):.3f}%\n\n"
    for a in articles:
        text += f"Headline: {a.get('title', '')}\nBrief: {a.get('description', '')}\n\n"

    message = client.messages.create(
        from_="whatsapp:+14155238886",
        body=text,
        to="whatsapp:+905073519085"
    )
    print("Sent:", message.status)
else:
    print(f"Change: {diff:.2f}%, under 5% threshold")