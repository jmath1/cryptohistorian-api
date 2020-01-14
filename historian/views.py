from django.shortcuts import render
from django.http import JsonResponse
from .pricer import *

# Create your views here.
def home(request):
    return render(request, "You are home")

def get_price(request, exchange, order_type):
    if exchange == "coinbase":
        data = coinbase(order_type)
    return JsonResponse(data, safe=False)