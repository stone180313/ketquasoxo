import requests
import json
from bs4 import BeautifulSoup
url = "https://xskt.com.vn/rss-feed/mien-nam-xsmn.rss"
resp = requests.get(url)
soup = BeautifulSoup(resp.content, features="xml")
items = soup.findAll('item')
news_items = []
def ketquasoxo():
    for item in items:
        news_item = {}
        news_item['title'] = item.title.text
        news_item['description'] = item.description.text
        news_item['link'] = item.link.text
        # news_item['image'] = item.content['url']
        news_items.append(news_item)
        # print(json.dumps(news_items,indent = 4)).encode("utf-8")
        # x = json.dumps(news_items)
    return news_items
dict =(ketquasoxo())
print(dict)
contacts = [{"John": "01217000111", "Addison": "01217000222", "Jack": "01227000123"}]

people = [
{'name': "Tom", 'age': 10},
{'name': "Mark", 'age': 5},
{'name': "Pam", 'age': 7}
]

def search(name):
    for p in people:
        if p['name'] == name:
            return p

print(search("Pam"))
def search(title):
    for d in dict:
        if d['title'] == title:
            return d

print(search("title"))
for title in dict:
    print(title['title'])
    print(title['description'])