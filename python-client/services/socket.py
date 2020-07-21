from binance.websockets import BinanceSocketManager
# twisted is the framework used to interact with a websocket

from model.klineticker import KlineTicker
from services.setup import ClientSetup


class BinanceSocket(ClientSetup):

    def __init__(self, symbol):
        self.symbol = symbol
        self.bsm = None
        self.conn_key = None
        self.new_data_available = True
        # self.old_start = None
        # self.curr_start = None
        self.ticker = None

    def connect(self):
        self.bsm = BinanceSocketManager(self.client)
        self.conn_key = self.bsm.start_kline_socket(self.symbol, self.process_msg)
        self.bsm.start()

    def disconnect(self):
        self.bsm.stop_socket(self.conn_key)
        self.bsm.close()
        self.reactor.stop()

    def process_msg(self, msg):
        self.ticker = KlineTicker(msg)
        print(self.ticker.__str__())
        self.new_data_available = True
        # self.curr_start = self.ticker.get_start()
        # self.update_new_data_available()

    # def update_new_data_available(self):
    #     if self.old_start is None or self.curr_start > self.old_start:
    #         self.new_data_available = True
    #         self.old_start = self.curr_start
    #     else:
    #         self.new_data_available = False

    def set_new_data_available(self, bol_value):
        self.new_data_available = bol_value

    def get_new_data_available(self):
        return self.new_data_available
