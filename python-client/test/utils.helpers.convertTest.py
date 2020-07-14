import unittest

from utils.constants import DateTimeConstants
from utils.helpers.convert import get_datetime


class convertTest(unittest.TestCase):
    # TestCase subclasses will implement tests whose method names start with test
    def test_get_datetime(self):
        # "2018-02-10 19:28:14"
        print(get_datetime(1518308894.652, DateTimeConstants.S))
        print(get_datetime(1518308894652, DateTimeConstants.MS))
        self.assertEqual(get_datetime(1518308894.652, DateTimeConstants.S),
                         get_datetime(1518308894652, DateTimeConstants.MS))


if __name__ == '__main__':
    unittest.main()
