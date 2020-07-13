from client.setup.binance.clientsetup import ClientSetup
from client.setup.binance.rest import BinanceRest
from client.setup.binance.socket import BinanceSocket
from utils.pretty.print import ppjson

ENV = 'test'

client = ClientSetup(ENV).setup()
rest = BinanceRest("XRPUSDT", client)

print("ACCOUNT INFO")
ppjson(rest.get_account())

print("TICKER INFO")
ppjson(rest.get_symbol_ticker())

BinanceSocket("XRPUSDT").connect()


# instead of making calls to REST API, use sockets
