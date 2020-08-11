from binance.client import Client
import os
import time
import win32api


class ClientSetup:

    client = None
    def __init__(self, env):
        self.api_key = os.environ.get('binance_api')
        self.api_secret = os.environ.get('binance_secret')
        self.client = None
        self.env = env

    def setup(self):
        # avoid committing/storing api/secret in code instead set as environment variables in os
        self.client = Client(self.api_key, self.api_secret)

        if self.env == 'test':
            self.client.API_URL = 'https://testnet.binance.vision/api'
        else:
            self.client.API_URL = 'https://api.binance.com/api'

        gt = self.client.get_server_time()
        tt = time.gmtime(int((gt["serverTime"]) / 1000))
        win32api.SetSystemTime(tt[0], tt[1], 0, tt[2], tt[3], tt[4], tt[5], 0)

        return self.client
