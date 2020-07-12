from client.setup.binance.clientsetup import ClientSetup
# from client.setup.connect.rest import BinanceRest
from client.setup.connect.socket import BinanceSocket

ENV = 'test'

client = ClientSetup(ENV).setup()
# BinanceRest(client)
# restclient = binance.get_client()


# client = BinanceRest(ENV).client

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

BinanceSocket('XRPUSDT').connect()


# instead of making calls to REST API, use sockets
