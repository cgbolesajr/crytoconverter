import requests
import json
from coin import Coin

class Manager:
    repo = {}
    def __init__(self):
        self.initialize_repo()

    def web_scrape(self):
        url = "https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,XRP,DASH,LTC&tsyms=USD,EUR"
        response = requests.get(url)
        return response

    def initialize_repo(self):
        response =  self.web_scrape()
        result = json.loads(response.content)
        for item in result:
            coin = Coin(item, result[item]['USD'],result[item]['EUR'])
            self.repo[item] = coin

    def coin_list(self):
        return self.repo.keys()

    def calculate(self, amount, symbol, to):
        coin = self.repo.get(symbol)
        rate = getattr(coin, to)
        return amount * rate
    
            
        


