import pytest
from model.Windows.TDX.test_model_TDX import TestModel
import allure

threadName = '10000'

ts = TestModel()

@allure.feature('客户端下载安装')
class Testclientinitialization:

    @allure.story('客户端下载')
    @pytest.mark.initialization
    @pytest.mark.download
    def test_download(self):
        """
        用例描述：客户端下载
        """
        # ts.test_DownloadClient()
        pass

    @allure.story('客户端安装')
    @pytest.mark.initialization
    @pytest.mark.Install
    def test_Install(self):
        """
        用例描述：客户端安装
        """
        ts.test_installprogram()

    @allure.story('客户端运行')
    @pytest.mark.initialization
    @pytest.mark.clientworking
    def test_working(self):
        """
        用例描述：客户端运行
        """
        ts.test_runningclient()


