from multiprocessing import Pool
import time
from historian.pricer import Pricer
from historian.models import PricePoint
from django.core.management.base import BaseCommand, CommandError
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

class BTCWorker():
    EXCHANGES = [
        "coinbase",
        "bittrex",
        "binance",
        "bitfinex",
    ]
    def __init__(self):
        self.pricer = Pricer("BTC")

    def api_call_buy(self, exchange):
        order_type = "buy"
        if exchange == "coinbase":
            data = self.pricer.coinbase(order_type)
        elif exchange == "bittrex":
            data = self.pricer.bittrex(order_type)
        elif exchange == "binance":
            data = self.pricer.binance(order_type)
        elif exchange == "bitfinex":
            data = self.pricer.bitfinex(order_type)
        return data, exchange

    def api_call_sell(self, exchange):
        order_type = "sell"
        if exchange == "coinbase":
            data = self.pricer.coinbase(order_type)
        elif exchange == "bittrex":
            data = self.pricer.bittrex(order_type)
        elif exchange == "binance":
            data = self.pricer.binance(order_type)
        elif exchange == "bitfinex":
            data = self.pricer.bitfinex(order_type)
        return data, exchange

    def get_all_buys(self):
        p = Pool(len(self.EXCHANGES))
        buys = p.map(self.api_call_buy, self.EXCHANGES)

        for price_point in buys:
            p = PricePoint.objects.create(price=price_point[0], exchange=price_point[1], order_type="buy")
            p.save()
            print(f"Saved {str(p)}")
            logger.info(f"Saved {str(p)}")

    def get_all_sells(self):
        p = Pool(len(self.EXCHANGES))
        sells = p.map(self.api_call_sell, self.EXCHANGES)

        for price_point in sells:
            p = PricePoint.objects.create(price=price_point[0], exchange=price_point[1], order_type="sell")
            p.save()
            print(f"Saved {str(p)}")
            logger.info(f"Saved {str(p)}")
