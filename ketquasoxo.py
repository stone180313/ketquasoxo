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
        # news_item['image'] = item.content['url']
        news_items.append(news_item)
        # print(json.dumps(news_items,indent = 4)).encode("utf-8")
        # x = json.dumps(news_items)
    return news_items
# dict =(ketquasoxo())
# print(dict[1]['title'])
#
# print(dict[1]['description'])

# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# data = json.loads(response.text)
# with open('data.json', 'w') as outfile:
#     json.dump(x, outfile)



# a=""
# b=""
# for title in dict:
#     # print(title['title'])
#     # print(title['description'])
#     dict.append(title['title'])
#     dict.append(title['description'])
#
#     break
