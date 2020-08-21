import unittest
import test


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



if __name__ == '__main__':
    unittest.main()
