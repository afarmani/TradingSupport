from binance.websockets import BinanceSocketManager
# twisted is the framework used to interact with a websocket
from datetime import datetime

from model.klineticker import KlineTicker
from services.setup import ClientSetup


class BinanceSocket(ClientSetup):

    def __init__(self, symbol):
        self.symbol = symbol
        self.bsm = None
        self.conn_key = None
        self.new_data_available = True
        self.ticker = None
        self.condition = None
        self.trans_range = None

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
        self.process_order()

    def process_order(self):
        close = float(self.ticker.close)
        if self.condition == 'buy':
            if close >= self.trans_range:
                print(datetime.now(), 'BUY', self.condition, self.trans_range)
        elif self.condition == 'sell':
            if close <= self.trans_range:
                print(datetime.now(), 'SELL', self.condition, self.trans_range)
        else:
            print(datetime.now(), 'NO ORDERS', self.condition, self.trans_range)

    def set_new_data_available(self, bol_value):
        self.new_data_available = bol_value

    def get_new_data_available(self):
        return self.new_data_available

    def set_market_conditions(self, condition):
        self.condition = condition

    def set_trans_range(self, trans_range):
        self.trans_range = trans_range
