import pytest
from model.Windows.TDX.test_model_TDX import TestModel
import allure

threadName = '10000'

ts = TestModel()

@allure.feature('成交明细')
class TestransactionDetails:

    @allure.story('查看上证成交明细')
    @pytest.mark.transactiondetails
    def test_download(self):
        """
        用例描述：查看上证成交明细
        """
        ts.test_viewSH_ListDetails()

    @allure.story('查看深证成交明细')
    @pytest.mark.transactiondetails
    def test_download(self):
        """
        用例描述：查看深证成交明细
        """
        ts.test_viewSZ_ListDetails()