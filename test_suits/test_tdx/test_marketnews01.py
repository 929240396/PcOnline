import pytest

from model.Windows.TDX.test_model_TDX import TestModel
import allure

threadName = '10000'

ts = TestModel()
@pytest.mark.下班
@allure.feature('行情')
class Testinformation:

    @allure.story('查看指数初始化')
    @pytest.mark.StockIndex
    def test_SHSZrefresh(self):
        """
        用例描述：查看上证指数、深证指数初始化
        """
        ts.test_marketstock_refresh()

    # @allure.story('查看个股集合竞价')
    # @pytest.mark.Individualstock
    # def test_individualstock(self):
    #     """
    #     用例描述：查看个股集合竞价
    #     """
    #     ts.test_view_individualstock()