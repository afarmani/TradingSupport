import time
from datetime import datetime, timedelta

from binance.client import Client

from history.retrieve import RetrieveHistory
from services.rest import BinanceRest
from services.setup import ClientSetup
from services.socket import BinanceSocket
from trading.helpers.stats import set_mean
from utils.constants import AppConstants

symbol = "XRPUSDT"
client = ClientSetup(AppConstants.ENV_TEST).setup()
rest = BinanceRest(symbol, client)
history = RetrieveHistory(symbol, interval=Client.KLINE_INTERVAL_1MINUTE, client=client)

# initialize socket
socket = BinanceSocket(symbol)
socket.connect()

holdings = 0
old_time = datetime.now().replace(second=0, microsecond=0)

while holdings == 0:
    curr_time = datetime.now().replace(second=0, microsecond=0)
    time.sleep(1)
    # socket data, retrieves data every minute
    if socket.get_new_data_available():
        socket.set_new_data_available(False)

    # refresh data every minute
    if curr_time > old_time:
        old_time = datetime.now().replace(second=0, microsecond=0)
        data = history.get_historical_klines("6 hours ago UTC")
        df = history.set_panda_dataFrame(data)
        ma20 = df['Close'].rolling(window=20).mean()
        print(datetime.now(), ma20.values[ma20.size - 1], ma20.values[ma20.size - 2], ma20.values[ma20.size - 3])
        if ma20.values[ma20.size - 1] < ma20.values[ma20.size - 2] < ma20.values[ma20.size - 3]:
            print(datetime.now(), 'sell')
        elif ma20.values[ma20.size - 1] > ma20.values[ma20.size - 2] > ma20.values[ma20.size - 3]:
            print(datetime.now(), 'buy')
        else:
            print(datetime.now(), 'neutral')

