import requests

class News():

    def __init__(self,api):
        self.api = api
    
    def get_news(self):
        URL_NEWS = "https://newsapi.org/v2/everything"
        params = {
            "q": "Tesla",
            "from": "2026-05-20",
            "to": "2026-05-27",
            "sortBy": "publishedAt",
            "pageSize": 3,
            "apiKey": self.api,
        }
        response_news = requests.get(URL_NEWS, params=params)
        return response_news.json()