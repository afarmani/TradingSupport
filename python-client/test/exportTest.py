import os
import unittest
import test
from history import Exporter
from utils.constants import ExporterConstants

fileName = "exportedFile"
fakeFileName = "FAKE"


def remove_file():
    # pass
    if os.path.isfile(fileName):
        os.remove(fileName)
        print("file removed")


class exportTest(unittest.TestCase, test.ClientSetupTest):

    @classmethod
    def setUpClass(cls):
        cls.data = None
        super(exportTest, cls).clientSetupClass()

    def test_export_json(self):
        self.check_data_loaded(exportTest.data)
        print("Exporting File for test_export_json")
        Exporter(fileName, exportTest.data, ExporterConstants.JSON)
        self.assertFalse(os.path.isfile(fakeFileName))
        self.assertTrue(os.path.isfile(fileName))
        print("File Exported for test_export_json")

    def test_export_csv(self):
        self.check_data_loaded(exportTest.data)
        print("Exporting File for test_export_csv")
        Exporter(fileName, exportTest.data, ExporterConstants.CSV)
        self.assertFalse(os.path.isfile(fakeFileName))
        self.assertTrue(os.path.isfile(fileName))
        print("File Exported for test_export_csv")

    def test_export_pd(self):
        self.check_data_loaded(exportTest.data)
        print("Retrieve pandas data frame")
        exporter = Exporter(fileName, exportTest.data, None)
        df = None
        df = exporter.export_pandas()
        # None is falsy, as well as 0, "", [], ...
        print(df.head())
        self.assertIsNotNone(df)
        print("Finish Retrieving pandas data frame")
        print("Export pandas data frame to csv")
        df.to_csv(fileName)
        self.assertFalse(os.path.isfile(fakeFileName))
        self.assertTrue(os.path.isfile(fileName))
        print("Finish Export pandas data frame to csv")

    def check_data_loaded(self, data):
        if data is None:
            print("load data")
            exportTest.data = self.history.get_historical_klines("10 day ago UTC")

    def setUp(self):
        remove_file()

    def tearDown(self):
        remove_file()


if __name__ == '__main__':
    unittest.main()
