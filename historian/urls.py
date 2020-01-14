from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('home/', home),
    path('price/<str:exchange>/<str:order_type>/', get_price)
]
