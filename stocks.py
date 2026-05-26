import requests

class Stocks:
    
    def __init__(self,api):
        self.api = api
    
    def get_stocks(self):
        URL_STOCKS = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey={self.api}"
        response_stocks = requests.get(URL_STOCKS)
        return response_stocks.json()