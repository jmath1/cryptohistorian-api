import requests
import json

class Pricer():

    def __init__(self, coin):
        self.coin = coin
        
    def coinbase(self, order_type):
        if order_type == "buy":
            endpoint = f"https://api.coinbase.com/v2/prices/{self.coin}-USD/buy"
        elif order_type == "sell":
            endpoint = f"https://api.coinbase.com/v2/prices/{self.coin}-USD/sell"
        res = requests.get(endpoint)
        data = res.content.decode('utf-8')
        data = json.loads(data)
        usd_price = data["data"]["amount"]
        
        return usd_price

    def bittrex(self, order_type):
        endpoint = "https://api.bittrex.com/api/v1.1/public/getmarketsummaries"
        res = requests.get(endpoint)
        data = res.content.decode('utf-8')
        data = json.loads(data)["result"]

        for pair in data:
            if pair["MarketName"] == f"USDT-{self.coin}":
                if order_type == "buy":
                    price = pair["Bid"]
                elif order_type == "sell":
                    price = pair["Ask"]
                return price
        return "Not Found"

    def binance(self, order_type=None):
        endpoint = "https://binance.com/api/v3/ticker/price"
        res = requests.get(endpoint)
        data = res.content.decode('utf-8')
        data = json.loads(data)
        for pair in data:
            if pair["symbol"] == f"{self.coin}USDT":
                return pair["price"]

    def bitfinex(self, order_type):
        endpoint = f"https://api-pub.bitfinex.com/v2/ticker/t{self.coin}USD"
        res = requests.get(endpoint)
        data = res.content.decode('utf-8')
        data = json.loads(data)
        if order_type == "buy":
            price = data[0]
        elif order_type == "sell":
            price = data[2]
        return price

    def __str__(self):
        return f"{self.coin} pricer"