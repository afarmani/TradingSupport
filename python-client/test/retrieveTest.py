import unittest
import test

from utils.pretty.print import PrettyPrint


class convertTest(unittest.TestCase, test.ClientSetupTest):

    # we want to avoid initializing the client and history classes each time a test method is ran
    # therefore we use setUpClass

    @classmethod
    def setUpClass(cls):
        super(convertTest, cls).clientSetupClass()

    def test_get_historical_klines(self):
        self.data = self.history.get_historical_klines("10 day ago UTC")
        PrettyPrint.json(self.data)
        print(self.data)
        self.assertIsNotNone(self.data)


if __name__ == '__main__':
    unittest.main()
