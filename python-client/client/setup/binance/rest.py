from typing import Type
from client.setup.binance.clientsetup import ClientSetup
from binance.client import Client


class BinanceRest(ClientSetup):

    def __init__(self, symbol, client: Type[Client]):
        self.client = client
        self.symbol = symbol

    def get_symbol_ticker(self):
        return self.client.get_symbol_ticker(symbol=self.symbol)

    def get_account(self):
        return self.client.get_account()