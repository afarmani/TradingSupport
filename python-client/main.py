from binance.client import Client

from history.retrieve import RetrieveHistory
from services import ClientSetup
from services import BinanceRest
from services.socket import BinanceSocket
from utils.constants import AppConstants
from utils.pretty.print import PrettyPrint

symbol = "XRPUSDT"

client = ClientSetup(AppConstants.ENV_TEST).setup()
rest = BinanceRest(symbol, client)
history = RetrieveHistory(symbol, interval=Client.KLINE_INTERVAL_1DAY, client=client)

print("ACCOUNT INFO")
PrettyPrint.json(rest.get_account())

print("TICKER INFO")
PrettyPrint.json(rest.get_symbol_ticker())

print("HISTORY")
PrettyPrint.json(history.get_historical_klines("10 day ago UTC"))

BinanceSocket(symbol).connect()

# instead of making calls to REST API, use sockets
