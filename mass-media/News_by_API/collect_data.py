import requests
from newsapi import NewsApiClient
import json

with open('credentials.json', mode='r', encoding='utf-8') as f:
    credentials = json.load(f)
    ADDRESS = credentials["address"]
    API_KEY = credentials["api_key"]


def country_abbreviation():
    with open('countries.txt', 'r') as f:
        countries_list = f.readlines()
        abbreviation_lst = [country.strip() for country in countries_list]
        f.close()
    return abbreviation_lst


def news_sources():
    countries_list = country_abbreviation()
    dict_of_sources = dict()
    for country in countries_list:
        url = ADDRESS + country + API_KEY
        response = requests.get(url).json()['sources']

        list_of_sources = []
        if response:
            for k in response:
                list_of_sources.append(k['id'])
            dict_of_sources[country] = ','.join(list_of_sources)

    return dict_of_sources


def news_articles():
    news_api = NewsApiClient(api_key=API_KEY[8:])
    for country in news_sources().keys():
        headlines = news_api.get_everything(q='Ukraine',
                                            sources=news_sources()[country],
                                            from_param='2020-04-20',
                                            to='2020-05-10',
                                            page=1
                                            )
        with open(country + '.json', 'w', encoding='utf-8') as f:
            json.dump(headlines, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    news_articles()
