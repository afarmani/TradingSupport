import unittest
import test
from Indicators.createAdx import CreateAdx
from model.binanceModelSetter import set_historical_klines_variables

from utils.pretty.print import PrettyPrint


class convertTest(unittest.TestCase, test.ClientSetupTest):

    # we want to avoid initializing the client and history classes each time a test method is ran
    # therefore we use setUpClass

    @classmethod
    def setUpClass(cls):
        super(convertTest, cls).clientSetupClass()

    def test_get_historical_klines(self):
        # data = self.history.get_historical_klines("10 day ago UTC")
        data = self.history.get_historical_klines("6 hours ago UTC")
        df = self.history.set_panda_dataFrame(data)
        self.assertIsNotNone(data)
        self.assertIsNotNone(df)
        # ModelTester
        adx = CreateAdx(df, 14)

        for index, row in df.iterrows():
            self.assertIsNotNone(row)
            self.assertIsNotNone(index)
            index, close, high, low, open, volume = set_historical_klines_variables(index, row)
            break


if __name__ == '__main__':
    unittest.main()
