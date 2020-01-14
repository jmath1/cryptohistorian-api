import requests
import json

def coinbase(order_type):
    if order_type == "buy":
        endpoint = "https://api.coinbase.com/v2/prices/BTC-USD/buy"
    elif order_type == "sell":
        endpoint = "https://api.coinbase.com/v2/prices/BTC-USD/sell"
    res = requests.get(endpoint)
    data = res.content.decode('utf-8')
    data = json.loads(data)
    usd_price = data["data"]["amount"]
    
    return usd_price

def bittrex(order_type):
    endpoint = "https://api.bittrex.com/api/v1.1/public/getmarketsummaries"
    res = requests.get(endpoint)
    data = res.content.decode('utf-8')
    data = json.loads(data)["result"]

    for pair in data:
        if pair["MarketName"] == "USDT-BTC":
            if order_type == "buy":
                price = pair["Bid"]
            elif order_type == "sell":
                price = pair["Ask"]
            return price
    return "Not Found"

def binance(order_type=None):
    endpoint = "https://binance.com/api/v3/ticker/price"
    res = requests.get(endpoint)
    data = res.content.decode('utf-8')
    data = json.loads(data)
    for pair in data:
        if pair["symbol"] == "BTCUSDT":
            return pair["price"]

def bitfinex(order_type):
    endpoint = "https://api-pub.bitfinex.com/v2/ticker/tBTCUSD"
    res = requests.get(endpoint)
    data = res.content.decode('utf-8')
    data = json.loads(data)
    if order_type == "buy":
        price = data[0]
    elif order_type == "sell":
        price = data[2]
    return price


