from unittest import mock
from unittest.mock import MagicMock
import mp_sample
import WebAPI

class Test_MpSample():

    def test1(self):
        web_api = WebAPI
        web_api.get_value = MagicMock(return_value=1)

        sample = mp_sample.MPsample(web_api)
        q = sample.get_queue()
        sample.start()
        sample.stop()

        assert q.get() == 1
