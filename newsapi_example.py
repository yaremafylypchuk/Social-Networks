import requests
from newsapi import NewsApiClient
import json

with open('credentials.json', mode='r', encoding='utf-8') as f:
    credentials = json.load(f)
    ADDRESS = credentials["address"]
    API_KEY = credentials["api_key"]


def news_articles():
    news_api = NewsApiClient(api_key=API_KEY[8:])
    headlines = news_api.get_everything(q='Ukraine',
                                        from_param='2020-04-20',
                                        to='2020-05-10',
                                        page=1
                                        )
    with open('example_news_api.json', 'w', encoding='utf-8') as f:
        json.dump(headlines, f, ensure_ascii=False, indent=4)

news_articles()