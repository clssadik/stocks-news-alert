import requests
from datetime import datetime, timedelta

class Stocks:
    def __init__(self, api):
        self.api = api

    def get_prices(self, ticker="TSLA"):
        end = datetime.now()
        start = end - timedelta(days=30)
        URL = f"https://api.tiingo.com/tiingo/daily/{ticker}/prices"
        params = {
            "startDate": start.strftime("%Y-%m-%d"),
            "endDate": end.strftime("%Y-%m-%d"),
            "token": self.api,
        }
        return requests.get(URL, params=params).json()