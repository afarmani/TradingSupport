import os
import time
import win32api

from binance.client import Client

# init
api_key = os.environ.get('binance_api')
api_secret = os.environ.get('binance_secret')

print(api_key)
print(api_secret)

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

