from django.urls import path

from .views import (ExchangeInfo, Market, Klines, Order,
                    Account, Wallet, )


app_name = 'main'
urlpatterns = [
    path('', ExchangeInfo.as_view(), name='exchange_info'),
    path('market/', Market.as_view(), name='market'),
    path('order/<str:symbol>/<str:price>', Order.as_view(), name='order'),
    path('account/', Account.as_view(), name='account'),
    path('wallet/', Wallet.as_view(), name='wallet'),
    path('kline/', Klines.as_view(), name='kline'),
]
