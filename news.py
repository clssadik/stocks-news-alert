import yfinance as yf

class News():
    
    def __init__(self,api,name):
        self.api = api
        self.name = name
    
    def get_news(self):
        df = yf.download("TSLA", start="2023-01-01", end="2024-01-01")
        data = df.reset_index().to_dict(orient="records")
        return data