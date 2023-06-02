
from django.urls import path

from .views import (ExchangeInfo, Market, Klines, Order,
                    Account,
                    )


app_name = 'main'
urlpatterns = [
    path('', ExchangeInfo.as_view(), name='exchange_info'),
    path('market/', Market.as_view(), name='market'),
    path('order/<str:symbol>/<str:price>', Order.as_view(), name='order'),
    path('account/', Account.as_view(), name='account'),

    path('kline/', Klines.as_view(), name='kline'),
]
