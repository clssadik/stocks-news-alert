import os
from dotenv import load_dotenv
load_dotenv()
from stocks import Stocks
from datetime import datetime
from news import News
from twilio.rest import Client

STOCKS_API = os.getenv("STOCKS_API")
NEWS_API = os.getenv("NEWS_API")
STOCK = "TSLA"
COMPANY_NAME = "Tesla"
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

now = datetime.now()
date = now.date()
day = now.date().day
month = now.date().month
year = now.date().year

stocks_object = Stocks(api=STOCKS_API,day=day,month=month)
data_stocks = stocks_object.get_prices()
yesterday_price = data_stocks[20]["close"]
before_price = data_stocks[19]["close"]

news_object = News(NEWS_API)
data_news = news_object.get_news()

diff = ((yesterday_price - before_price) / before_price) * 100

text = ""

def get_text(params):
    global text
    text = (
        f"TSLA: {params}%\n"
        f"Headline: {data_news['articles'][0]['title']}\n"
        f"Brief: {data_news['articles'][0]['description']}\n\n"
        f"Headline: {data_news['articles'][1]['title']}\n"
        f"Brief: {data_news['articles'][1]['description']}\n\n"
        f"Headline: {data_news['articles'][2]['title']}\n"
        f"Brief: {data_news['articles'][2]['description']}"
    )

if diff <= 0:
    get_text("🔻")
else:
    get_text("🔺")

message = client.messages.create(
    from_='whatsapp:+14155238886',
    body= text,
    to='whatsapp:+905073519085'
)

print(message.status)














## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

