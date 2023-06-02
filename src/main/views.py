import time
import requests
import hashlib
import hmac
import base64

import environ
from pathlib import Path

from django.shortcuts import render
from django.views.generic import (View)

BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()
environ.Env.read_env()


class ExchangeInfo(View):
    def get(self, *args):
        url = "https://api.mexc.com/api/v3/exchangeInfo"
        response = requests.get(url)
        if response.status_code == 200:
            return render(self.request, 'main/exchange_info.html', {'exchange_info': response.json()})

        return render(self.request, 'main/not_available.html')


class Market(View):
    def get(self, *args):
        url = "https://api.mexc.com/api/v3/ticker/24hr"
        response = requests.get(url)
        if response.status_code == 200:
            return render(self.request, 'main/market.html', {'ticker': response.json()})

        return render(self.request, 'main/not_available.html')


class Klines(View):
    def get(self, *args):
        url = "https://api.mexc.com/api/v3/klines?symbol=TOMO3LUSDT&interval=1d"
        response = requests.get(url)
        if response.status_code == 200:
            return render(self.request, 'main/kline.html', {'klines': response.json()})

        return render(self.request, 'main/not_available.html')


class Order(View):
    def get(self, *args, **kwargs):
        url = "https://api.mexc.com/api/v3/order/test?"
        api_key = f"api_key={env('API_KEY')}&"
        url_data = "symbol={}&side=BUY&type=LIMIT&quantity=1&price={}&recvWindow=5000&timestamp={}".format(
            kwargs['symbol'], kwargs['price'], int(time.time() * 1000),
        )
        secret = env('API_SECRET').encode('utf-8')
        total_params = (api_key+url_data).encode('utf-8')
        signature = hmac.new(secret, total_params, hashlib.sha256).hexdigest()

        final_url = url + api_key + url_data + f"&signature={signature}"
        response = requests.post(final_url)
        data = response.json()

        return render(self.request, 'main/successful.html', {'data': data, 'url': final_url})


class Account(View):
    def get(self, *args, **kwargs):
        url = "https://api.mexc.com/api/v3/account?"
        api_key = f"api_key={env('API_KEY')}&"
        url_data = "timestamp={}".format(
            int(time.time() * 1000),
        )
        secret = env('API_SECRET').encode('utf-8')
        total_params = (api_key+url_data).encode('utf-8')
        signature = hmac.new(secret, total_params, hashlib.sha256).hexdigest()

        final_url = url + api_key + url_data + f"&signature={signature}"
        response = requests.get(final_url)
        data = response.json()

        return render(self.request, 'main/successful.html', {'data': data, 'url': final_url})
