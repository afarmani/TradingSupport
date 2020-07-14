import unittest

from binance.client import Client

from client.setup.binance.history.retrieve import RetrieveHistory
from client.setup.binance.services.clientsetup import ClientSetup
from utils.constants import AppConstants
from utils.pretty.print import PrettyPrint


class convertTest(unittest.TestCase):

    # we want to avoid initializing the client and history classes each time a test method is ran
    # therefore we use setUpClass and store the symbol, client, history as class variables (static)
    @classmethod
    def setUpClass(cls):
        super(convertTest, cls).setUpClass()
        cls.symbol = "XRPUSDT"
        cls.client = ClientSetup(AppConstants.ENV_TEST).setup()
        cls.history = RetrieveHistory(cls.symbol, interval=Client.KLINE_INTERVAL_1DAY, client=cls.client)

    # setUp runs each time a test method is executed
    def setUp(self):
        self.symbol = convertTest.symbol
        self.client = convertTest.client
        self.history = convertTest.history

    def test_get_historical_klines(self):
        self.assertEqual(0, 0)
        PrettyPrint.json(self.history.get_historical_klines("10 day ago UTC"))
        print(self.history.get_historical_klines("10 day ago UTC"))


if __name__ == '__main__':
    unittest.main()
