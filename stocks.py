import requests
from datetime import datetime, timedelta


class Stocks:
    
    def __init__(self,api):
        self.api = api
    
    def get_stocks(self):
        URL_STOCKS = "https://finnhub.io/api/v1/stock/candle"
        start_date = "2023-01-01"
        end_date = "2024-01-01"
        from_ts = int(datetime.strptime(start_date, "%Y-%m-%d").timestamp())
        to_ts = int(datetime.strptime(end_date, "%Y-%m-%d").timestamp())
        params = {
            "symbol": "TSLA",
            "resolution": "D",
            "from": from_ts,
            "to": to_ts,
            "token": self.api
        }
        response_stocks = requests.get(URL_STOCKS,params=params)
        return response_stocks.json()