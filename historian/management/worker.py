
from historian.pricer import Pricer
from multiprocessing import Pool
from historian.models import PricePoint
import logging

logger = logging.getLogger(__name__)

class Worker():
    EXCHANGES = [
        "coinbase",
        "bittrex",
        "binance",
        "bitfinex",
    ]

    def __init__(self, coin):
        self.pricer = Pricer(coin)
        self.coin = coin

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
            p = PricePoint.objects.create(price=price_point[0], exchange=price_point[1], order_type="buy", coin=self.coin)
            p.save()
            print(f"Saved {str(p)}")
            logger.info(f"Saved {str(p)}")

    def get_all_sells(self):
        p = Pool(len(self.EXCHANGES))
        sells = p.map(self.api_call_sell, self.EXCHANGES)

        for price_point in sells:
            p = PricePoint.objects.create(price=price_point[0], exchange=price_point[1], order_type="sell", coin=self.coin)
            p.save()
            print(f"Saved {str(p)}")
            logger.info(f"Saved {str(p)}")
