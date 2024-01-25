from django.urls import path

from .views import currency_exchange_api

urlpatterns = [
    path('get-current-usd/', currency_exchange_api, name='currency'),
]
