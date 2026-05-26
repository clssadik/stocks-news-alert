import os
from dotenv import load_dotenv
load_dotenv()
import requests
from stocks import Stocks
from news import News

STOCKS_API = os.getenv("STOCKS_API")
NEWS_API = os.getenv("NEWS_API")
STOCK = "TSLA"
COMPANY_NAME = "Tesla"

stocks_object = Stocks(STOCKS_API)
data_stocks = stocks_object.get_stocks()
print(data_stocks)
# dates = sorted(data_stocks["Time Series (Daily)"].keys(),reverse=True)
# yesterday_price = float( data_stocks["Time Series (Daily)"][dates[0]]["4. close"] )
# before_price = float( data_stocks["Time Series (Daily)"][dates[1]]["4. close"] )

# diff = ((yesterday_price - before_ppip install yfinancerice) / before_price) * 100
# if abs(diff) >= 5:
#     print("Get News!")

news_object = News(NEWS_API,COMPANY_NAME)
data_news = news_object.get_news()
# print(data_news)















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

