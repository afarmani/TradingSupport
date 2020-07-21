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


def refreshDataFrame():
    global df
    # print(datetime.now().replace(second=0, microsecond=0))
    # print(df.index.max())
    if datetime.now().replace(second=0, microsecond=0) > df.index.max():
        time.sleep(2)
        data = history.get_historical_klines("6 hours ago UTC")
        df = history.set_panda_dataFrame(data)
        df['Avg Volume'] = set_mean(df['Volume'], 20)
        # print("update data set")
        print('Curr Avg Volume: %s' % df['Avg Volume'].tail(1).values)
        print('Curr Volume: %s' % df['Volume'].tail(1).values)


# print("initialize socket")
socket = BinanceSocket(symbol)
socket.connect()

# print("initialize data set")
data = history.get_historical_klines("6 hours ago UTC")
df = history.set_panda_dataFrame(data)
print(df)

holdings = 0
while holdings == 0:
    if socket.get_new_data_available():
        # print("new socket data available")
        refreshDataFrame()
        socket.set_new_data_available(False)

    # time.sleep(10)
    # print("10 seconds")
