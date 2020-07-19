import unittest
import dateparser as dp


class DateParserTest(unittest.TestCase):

    def test_dateTime(self):
        print(dp.parse('12/12/12'))  # '2012-12-12 00:00:00'
        print(dp.parse(u'Fri, 12 Dec 2014 10:55:50'))  # '2014-12-12 10:55:50'
        print(dp.parse(1594339200000))
