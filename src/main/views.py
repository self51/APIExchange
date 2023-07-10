from django.shortcuts import render
from django.views.generic import (View)

from .services import APIRequestManager


class ExchangeInfo(View):
    def get(self, *args):
        url = "https://api.mexc.com/api/v3/exchangeInfo?"
        request_builder = APIRequestManager(url, {})
        status_code, data = request_builder.make_request()

        if status_code == 200:
            return render(self.request, 'main/exchange_info.html', {'exchange_info': data})

        return render(self.request, 'main/not_available.html')


class Market(View):
    def get(self, *args):
        url = "https://api.mexc.com/api/v3/ticker/24hr?"
        request_builder = APIRequestManager(url, {})
        status_code, data = request_builder.make_request()

        if status_code == 200:
            return render(self.request, 'main/market.html', {'ticker': data})

        return render(self.request, 'main/not_available.html')


class Klines(View):
    def get(self, *args):
        url = "https://api.mexc.com/api/v3/klines?"
        params = {
            'symbol': 'TOMO3LUSDT',
            'interval': '1d',
        }
        request_builder = APIRequestManager(url, params)
        status_code, data = request_builder.make_request()

        if status_code == 200:
            return render(self.request, 'main/kline.html', {'klines': data})

        return render(self.request, 'main/not_available.html')


class Order(View):
    def get(self, *args, **kwargs):
        url = "https://api.mexc.com/api/v3/order/test?"
        params = {
            'symbol': kwargs['symbol'],
            'side': 'BUY',
            'type': 'LIMIT',
            'quantity': 1,
            'price': kwargs['price'],
            'recvWindow': 5000,
        }
        request_builder = APIRequestManager(url, params, method='post', signature=True)
        status_code, data = request_builder.make_request()

        if status_code == 200:
            return render(self.request, 'main/successful.html', {'data': data})

        return render(self.request, 'main/not_available.html')


class Account(View):
    def get(self, *args, **kwargs):
        url = "https://api.mexc.com/api/v3/account?"
        params = {}
        request_builder = APIRequestManager(url, params, method='get', signature=True)
        status_code, data = request_builder.make_request()

        if status_code == 200:
            return render(self.request, 'main/successful.html', {'data': data})

        return render(self.request, 'main/not_available.html')


class Wallet(View):
    def get(self, *args, **kwargs):
        url = "https://api.mexc.com/api/v3/capital/config/getall?"
        params = {}
        request_builder = APIRequestManager(url, params, method='get', signature=True)
        status_code, data = request_builder.make_request()

        if status_code == 200:
            return render(self.request, 'main/successful.html', {'data': data})

        return render(self.request, 'main/not_available.html')
