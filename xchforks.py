import time

import requests
from datetime import datetime
import hashlib
import hmac

class xchforksConnector:
    def __init__(self, key, secret, trading_allowed=False, verify=False):
        self.__api_link = r'https://www.xchforks.trade/api/v2/peatio'
        self.__key = key
        self.__secret = secret
        self.__verify = verify
        self.__trading_allowed = trading_allowed


    def __get_headers(self):
        stamp = str(int(time.time() * 1000))
        hash = hmac.new(bytes(self.__secret, encoding='utf-8'), bytes(stamp + self.__key, encoding='utf-8'), hashlib.sha256)
        signature = hash.hexdigest()
        headers = {"X-Auth-Apikey": self.__key, "X-Auth-Nonce": stamp,
                   "X-Auth-Signature": signature, "Content-Type": "application/json"}
        return headers

    def __request_get(self, link, public=False):
        if public:
            resp = requests.get(link, verify=self.__verify)
        else:
            resp = requests.get(link, headers=self.__get_headers(), verify=self.__verify)
        return resp.text

    def __request_post(self, link, json=None, public=False):
        if public:
            resp = requests.post(link, verify=self.__verify, json=json)
        else:
            resp = requests.post(link, headers=self.__get_headers(), verify=self.__verify, json=json)
        return resp.text

    # OPEN LIBRARY METHODS:
        # PUBLIC METHODS:
    def get_tickers_by_market(self, market):
        link = self.__api_link + f'/public/markets/{market}/tickers'
        return self.__request_get(link, public=True)

    def get_all_tickers(self):
        link = self.__api_link + '/public/markets/tickers'
        return self.__request_get(link, public=True)

    def get_ohlc_by_market(self, market):
        link = self.__api_link + f'/public/markets/{market}/k-line'
        return self.__request_get(link, public=True)

    def get_depth_by_market(self, market):
        link = self.__api_link + f'/public/markets/{market}/depth'
        return self.__request_get(link, public=True)

    def get_trades_by_market(self, market):
        link = self.__api_link + f'/public/markets/{market}/trades'
        return self.__request_get(link, public=True)

    def get_order_book_by_market(self, market):
        link = self.__api_link + f'/public/markets/{market}/order-book'
        return self.__request_get(link, public=True)

    def get_markets(self):
        link = self.__api_link + '/public/markets'
        return self.__request_get(link, public=True)

    def get_currencies(self):
        link = self.__api_link + '/public/currencies'
        return self.__request_get(link, public=True)

    def get_currency_by_currency_id(self, id):
        link = self.__api_link + f'/public/currencies/{id}'
        return self.__request_get(link, public=True)

    # OPEN LIBRARY METHODS:
        # PRIVATE METHODS:
            # GET DATA:
    def get_account_balances(self):
        link = self.__api_link + '/account/balances'
        return self.__request_get(link)

    def get_account_balance_by_currency_id(self, currency):
        link = self.__api_link + f'/account/balances/{currency}'
        return self.__request_get(link)

    def get_deposit_address_by_currency_id(self, currency):
        link = self.__api_link + f'/account/deposit_address/{currency}'
        return self.__request_get(link)

    def get_deposit_details_by_transaction_id(self, transaction_id):
        link = self.__api_link + f'/account/deposits/{transaction_id}'
        return self.__request_get(link)

    def get_deposits_history(self):
        link = self.__api_link + '/account/deposits'
        return self.__request_get(link)

    def get_your_orders(self):
        link = self.__api_link + '/market/orders'
        return self.__request_get(link)

    def get_all_your_withdraws(self):
        link = self.__api_link + '/account/withdraws'
        return self.__request_get(link)

    def get_your_trades(self):
        link = self.__api_link + '/market/trades'
        return self.__request_get(link)

    def get_your_orders(self):
        link = self.__api_link + '/market/orders'
        return self.__request_get(link)

    def get_order_info_by_order_id(self, order_id):
        link = self.__api_link + f'/market/orders/{order_id}'
        return self.__request_get(link)

    # OPEN LIBRARY METHODS:
        # PRIVATE METHODS:
            # ACTIONS:
    def cancel_all_orders(self, side=None):
        link = self.__api_link + '/market/orders/cancel'
        return self.__request_post(link, json={'side': side})

    def cancel_order_by_id(self, order_id):
        link = self.__api_link + f'/market/orders/{order_id}/cancel'
        return self.__request_post(link, json={'id': order_id})

    def create_withdrawal(self, otp, rid, currency, amount):
        if not self.__trading_allowed:
            return
        link = self.__api_link + '/account/withdraws'
        return self.__request_post(link, json={'otp': otp, 'rid': str(rid),
                                               'currency': str(currency), 'amount': amount})

    def send_order(self, market, side, volume, ord_type, price):
        if not self.__trading_allowed:
            return
        link = self.__api_link + '/market/orders'
        return self.__request_post(link, json={'market': str(market), 'side': str(side),
                                               'volume': volume, 'ord_type': str(ord_type),
                                               'price': price})