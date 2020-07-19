from typing import Type
from binance.client import Client
from services.setup import ClientSetup


class BinanceRest(ClientSetup):

    def __init__(self, symbol, client: Type[Client]):
        self.client = client
        self.symbol = symbol

    def get_symbol_ticker(self):
        return self.client.get_symbol_ticker(symbol=self.symbol)

    def get_account(self):
        return self.client.get_account()