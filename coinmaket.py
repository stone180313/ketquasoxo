import requests
import json
import pyfiglet
from prettytable import PrettyTable
while True:
    # base URLs
    globalURL = "https://api.coinmarketcap.com/v1/global/"
    tickerURL = "https://api.coinmarketcap.com/v1/ticker/"

    # get data from globalURL
    request = requests.get(globalURL)
    data = request.json()
    globalMarketCap = data['total_market_cap_usd']
    # menu
    print(pyfiglet.figlet_format('CoinMarketCap'))
    print("Kiem tra gia CoinMarketCap !")
    print("Tong giao dich tren thi truong: $" + str(globalMarketCap))
    print("Go all de xem 100 coin top list or co the go chinh xac ten 1 coin nhu bitcoin da duoc list tai coinmarketcap")
    print()
    choice = input("Your choice: ")

    if choice == "all":
        request = requests.get(tickerURL)
        data = request.json()
        for y in data:
            x = PrettyTable()
            x.field_names = ["TEN COIN", "GIA USD"]
            ticker = y['symbol']
            price = y['price_usd']
            x.add_row([ticker,price])
            print(x)
            # print(ticker + ":\t\t$" + price)
            print()
    else:
        tickerURL += '/'+choice+'/'
        request = requests.get(tickerURL)
        data = request.json()
        ticker = data[0]['symbol']
        price = data[0]['price_usd']
        percent_change_24h = data[0]['percent_change_24h']

        print(ticker + ":\t\t$" + price)
        print('biên độ 24 h qua ',percent_change_24h)


    choice2 = input("Kiem tra lai ? (co/khong): ")

    if choice2 == "co":
        continue
    if choice2 == "khong":
        break