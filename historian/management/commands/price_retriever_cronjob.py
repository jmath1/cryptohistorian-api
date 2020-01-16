from multiprocessing import Pool
import time
from historian.pricer import * 
from historian.models import PricePoint
from historian.management.bitcoin.client import BTCWorker
from historian.management.ethereum.client import ETHWorker
from django.core.management.base import BaseCommand, CommandError
import logging

# this is the actual cronjob to implement BTC
class Command(BaseCommand):

    help = 'This is an abstract class for implementing a PriceCollector class'
    coin = None
    
    def add_arguments(self, parser):
        parser.add_argument('coin', nargs='+', type=str)

   
    def handle(self, *args, **options):
        self.coin = options["coin"][0]
        if self.coin == "BTC":
            self.worker = BTCWorker()
        elif self.coin == "ETH":
            self.worker = ETHWorker()
        print(f"Starting cronjob to record {self.coin} prices across exchanges.")
        print(f"Using exchanges {self.worker.EXCHANGES}")
        while True:
            self.worker.get_all_buys()
            self.worker.get_all_sells()
            time.sleep(60)