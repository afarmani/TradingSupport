import os
import time
import win32api

from binance.client import Client

# avoid committing/storing api/secret in code instead set as environment variables in os
api_key = os.environ.get('binance_api')
api_secret = os.environ.get('binance_secret')

# client initializer
client = Client(api_key, api_secret)
client.API_URL = 'https://testnet.binance.vision/api'

# timestamp issue: binance.exceptions.BinanceAPIException: APIError(code=-1021):
# Timestamp for this request is outside of the recvWindow.
# timestamp solution: https://github.com/ccxt/ccxt/issues/936

gt = client.get_server_time()
tt = time.gmtime(int((gt["serverTime"]) / 1000))
win32api.SetSystemTime(tt[0], tt[1], 0, tt[2], tt[3], tt[4], tt[5], 0)

# all account info
print(client.get_account())

# print(client.futures_account_balance())
# print(client.get_margin_account())

# print ticker info
print(client.get_asset_balance(asset='XRP'))

# retrieve symbol ticker info
btc_ticker = client.get_symbol_ticker(symbol='XRPUSDT')
# output:
# {'symbol': 'BTCUSDT', 'price': '10000.00000000'}
print(btc_ticker['symbol'])
print(btc_ticker['price'])

# instead of making calls to REST API, use sockets

from binance.websockets import BinanceSocketManager
# twisted is the framework used to interact with a websocket
from twisted.internet import reactor

btc_ticker_streamed = {'error': False}


def btc_ticker_history(msg):
    if msg['e'] != 'error':
        btc_ticker_streamed['last'] = msg['c']
        btc_ticker_streamed['bid'] = msg['b']
    else:
        btc_ticker_streamed['error'] = True
    print(btc_ticker_streamed)


bsm = BinanceSocketManager(client)
conn_key = bsm.start_symbol_ticker_socket('XRPUSDT', btc_ticker_history)
bsm.start()

# closing the socket connections:
# bsm.stop_socket(conn_key)
# reactor.stop()
