from multiprocessing import Pool
import time
from historian.pricer import * 
from historian.models import PricePoint
from django.core.management.base import BaseCommand, CommandError
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

EXCHANGES = [
    "coinbase",
    "bittrex",
    "binance",
    "bitfinex",
]
def api_call_buy(exchange):
    order_type = "buy"
    if exchange == "coinbase":
        data = coinbase(order_type)
    elif exchange == "bittrex":
        data = bittrex(order_type)
    elif exchange == "binance":
        data = binance(order_type)
    elif exchange == "bitfinex":
        data = bitfinex(order_type)
    return data, exchange

def api_call_sell(exchange):
    order_type = "sell"
    if exchange == "coinbase":
        data = coinbase(order_type)
    elif exchange == "bittrex":
        data = bittrex(order_type)
    elif exchange == "binance":
        data = binance(order_type)
    elif exchange == "bitfinex":
        data = bitfinex(order_type)
    return data, exchange


class Command(BaseCommand):
    help = 'Cronjob initializer for recording buy and sell prices across all supported exchanges'

    def get_all_buys(self):
        p = Pool(len(EXCHANGES))
        buys = p.map(api_call_buy, EXCHANGES)

        for price_point in buys:
            p = PricePoint.objects.create(price=price_point[0], exchange=price_point[1], order_type="buy")
            p.save()
            print(f"Saved {str(p)}")
            logger.info(f"Saved {str(p)}")
            
    def get_all_sells(self):
        p = Pool(len(EXCHANGES))
        buys = p.map(api_call_sell, EXCHANGES)

        for price_point in buys:
            p = PricePoint.objects.create(price=price_point[0], exchange=price_point[1], order_type="sell")
            p.save()
            print(f"Saved {str(p)}")
            logger.info(f"Saved {str(p)}")
    
    def handle(self, *args, **options):
        print("Starting cronjob to record BTC prices across exchanges.")
        print(f"Using exchanges {EXCHANGES}")
        while True:
            self.get_all_buys()
            self.get_all_sells()
            time.sleep(60)