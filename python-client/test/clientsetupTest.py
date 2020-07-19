from history.retrieve import RetrieveHistory
from services import ClientSetup
from utils.constants import AppConstants


class ClientSetupTest(object):
    @classmethod
    def clientSetupClass(cls):
        cls.symbol = "XRPUSDT"
        cls.client = ClientSetup(AppConstants.ENV_TEST).setup()
        cls.history = RetrieveHistory(cls.symbol, interval=cls.client.KLINE_INTERVAL_1DAY, client=cls.client)

    # def get_history(self):
    #     return self.history
