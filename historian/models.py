from django.db import models


class PricePoint(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=14, decimal_places=6)
    exchange = models.CharField(max_length=30, default="Default")
    order_type = models.CharField(max_length=5, default="No Order Type")
    coin = models.CharField(max_length=5, default="No default should be saved")

    def __str__(self):
        return f"{self.coin} {self.created}: {self.exchange} - \
{self.order_type} - {self.price}"
