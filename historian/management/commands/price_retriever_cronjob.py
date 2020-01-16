import time
from historian.management.worker import Worker
from django.core.management.base import BaseCommand


# this is the actual cronjob to implement BTC
class Command(BaseCommand):

    help = 'This is an abstract class for implementing a PriceCollector class'
    coin = None

    def add_arguments(self, parser):
        parser.add_argument('coin', nargs='+', type=str)

    def handle(self, *args, **options):
        self.coin = options["coin"][0]
        self.worker = Worker(self.coin)
        print(
            f"Starting cronjob to record {self.coin} prices across exchanges."
        )
        print(f"Using exchanges {self.worker.EXCHANGES}")
        while True:
            self.worker.get_all_buys()
            self.worker.get_all_sells()
            time.sleep(60)
