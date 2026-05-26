import requests

class Stocks:
    def __init__(self, api, day, month):
        self.api = api
        self.day = int(day)
        self.month = int(month)

    def get_prices(self, ticker="TSLA"):
        URL = f"https://api.tiingo.com/tiingo/daily/{ticker}/prices"
        start_date=f"2026-{self.month-1}-{self.day}"
        end_date=f"2026-{self.month}-{self.day}"
        params = {
            "startDate": start_date,
            "endDate": end_date,
            "token": self.api,
        }
        return requests.get(URL, params=params).json()