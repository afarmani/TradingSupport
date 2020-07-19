from binance.websockets import BinanceSocketManager
# twisted is the framework used to interact with a websocket

from services import ClientSetup
from model.klineticker import KlineTicker


def process_msg(msg):
    ticker = KlineTicker(msg)
    print(ticker.__str__())


class BinanceSocket(ClientSetup):

    def __init__(self, symbol):
        self.symbol = symbol
        self.bsm = None
        self.conn_key = None

    def connect(self):
        self.bsm = BinanceSocketManager(self.client)
        self.conn_key = self.bsm.start_kline_socket(self.symbol, process_msg)
        self.bsm.start()

    def disconnect(self):
        self.bsm.stop_socket(self.conn_key)
        self.bsm.close()
        self.reactor.stop()
