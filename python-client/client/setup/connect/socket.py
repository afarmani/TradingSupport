from binance.websockets import BinanceSocketManager
# twisted is the framework used to interact with a websocket

from client.setup.binance.clientsetup import ClientSetup
from client.setup.binance.model.klineticker import KlineTicker


class BinanceSocket(ClientSetup):

    def __init__(self, symbol):
        self.symbol = symbol
        self.bsm = None
        self.conn_key = None

    def connect(self):
        self.bsm = BinanceSocketManager(self.client)
        self.conn_key = self.bsm.start_kline_socket(self.symbol, self.process_msg)
        self.bsm.start()

    def disconnect(self):
        self.bsm.stop_socket(self.conn_key)
        self.bsm.close()
        self.reactor.stop()

    def process_msg(self, msg):
        ticker = KlineTicker(msg)
        print(ticker.__str__())

    # def __init__(self, ticker):
    # btc_ticker_streamed = {'error': False}
    #
    # def ticker_history(msg):
    #     if msg['e'] != 'error':
    #         btc_ticker_streamed['last'] = msg['c']
    #         btc_ticker_streamed['bid'] = msg['b']
    #     else:
    #         btc_ticker_streamed['error'] = True
    #     print(btc_ticker_streamed)
    #
    # bsm = BinanceSocketManager(self.client)
    # bsm.start_symbol_ticker_socket(ticker, ticker_history)
    # bsm.start()

    # def socket_start

# closing the socket connections:
# bsm.stop_socket(conn_key)
# reactor.stop()
