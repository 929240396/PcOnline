#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "chenxiaofeng"
# Email: wnagkun@myht.com.cn
# Date: 2021/4/20
import pytest
import re
import os
from time import sleep
from BaseFunction.basedriverWindows import BaseDriverPC,CustomerAsserts
from BaseFunction.basedriverWindows import dir_path, dataname, txtpath

class CustomizationError(Exception):
    def __init__(self, value):
        self.value = value
        BaseDriverPC().QuitDriver()

    def __str__(self):
        return repr(self.value)


class TestModel:
    func = BaseDriverPC()
    md5xpath = '//*[@id="swDownLoadForm"]/div[3]/div[20]/div[2]/div[3]/div'
    chromepath = r'C:\Program Files\Google\Chrome\Application\chrome.exe'  # 浏览器启动路径
    downloadurl = 'https://cdn.showcai.com.cn/swdownload/index/app.html'  # 客户端下载地址
    md5path = r'C:\Program Files\新建文件夹\hasher\Hasher.exe'  # md5解码器路径
    lastpath = os.path.join(dir_path, dataname)

    # def test_DownloadClient(self):
    #     """
    #     下载客户端
    #     :return:
    #     """
    #     try:
    #         self.func.DownTDX()
    #         assert '.exe' in dataname
    #         self.func.openprograms(self.md5path)
    #         self.func.ClickByXY(750,300)
    #         self.func.ClickButtonByName("计算机")
    #         self.func.ClickEditByClassName("Edit")
    #         self.func.SendKeysByEditClassName("Edit", self.lastpath)
    #         self.func.ClickButtonByName("打开(O)")
    #         self.func.ClickByXY(1130,550)
    #         file = open(txtpath, 'w')
    #         file.close()
    #         self.func.startfile(txtpath)
    #         self.func.RightClickWindowByName("md5 - 记事本")
    #         self.func.ClickMenuByName("粘贴(P)")
    #         self.func.SetTopMostByName("md5 - 记事本")
    #         self.func.ClickButtonByName("关闭")
    #         self.func.ClickButtonByName("保存(S)")
    #         strMsgText1 = self.func.GetMd5ByXpath(self.downloadurl, self.md5xpath)
    #         strMsgText2 = self.func.GetMd5Bytxt()
    #         CustomerAsserts(strMsgText2, strMsgText1)
    #         self.func.ClosePrograms()
    #     except AssertionError as e:
    #         raise AssertionError('客户端下载' + "异常||原因：" + str(e))
    #     except Exception as e:
    #         raise CustomizationError('客户端下载' + "异常||原因：" + str(e))
    #
    # def test_installprogram(self):
    #     """
    #     安装客户端
    #     :return:
    #     """
    #     try:
    #         self.func.openprograms(self.lastpath)
    #         sleep(10)
    #         self.func.ClickButtonByName("开始安装")
    #         sleep(2)
    #         self.func.ClickButtonByName("确定")
    #         sleep(40)
    #         self.func.screenshoot(600,250,800,800)
    #         sleep(4)
    #         strMsgtext = self.func.baiduOCR()
    #         assert '安装成功' in strMsgtext
    #         sleep(2)
    #         self.func.ClickButtonByName("确定")
    #         dirname = self.func.GetDirNames()
    #         CustomerAsserts('东吴证券合一版.lnk', dirname)
    #     except AssertionError as e:
    #         raise AssertionError('客户端安装' + "异常||原因：" + str(e))
    #     except Exception as e:
    #         raise CustomizationError('客户端安装' + "异常||原因：" + str(e))

    # def test_runningclient(self):
    #     """
    #     运行客户端
    #     :return:
    #     """
    #     try:
            # self.func.openprograms(r'C:\new_dwzq\TdxW.exe')
            # sleep(15)
            # self.func.ClickPaneByAutomationId("365")
            # sleep(5)
            # self.func.dealWithpopup()
        #     sleep(2)
        #     self.func.screenshoot(15,15,1000,700)
        #     strMsgText = self.func.baiduOCR()
        #     assert strMsgText != ' '
        #     self.func.ClickPaneByAutomationId("9601")
        #     self.func.ClickButtonByName("退出")
        # except AssertionError as e:
        #     raise AssertionError('客户端打开' + "异常||原因：" + str(e))
        # except Exception as e:
        #     raise CustomizationError('客户端打开' + "异常||原因：" + str(e))

    def test_marketstock_refresh(self):
        """
        初始化查看
        :return:
        """
        try:
            self.func.openprograms(r'C:\new_dwzq\TdxW.exe')
            sleep(15)
            self.func.ClickPaneByAutomationId("365")
            sleep(15)
            self.func.dealWithpopup()
            sleep(2)
            self.func.Sendkeys("06")
            sleep(2)
            self.func.DoubleClickByNameByListItem("06      自选股                功能键")
            self.func.screenshoot(0, 1010, 400, 25)
            sleep(2)
            strMsgtext = self.func.baiduOCR()
            sleep(2)
            pattern = re.compile('[0-9]+')
            match = pattern.findall(strMsgtext)
            assert match != ''
            self.func.ClickPaneByAutomationId("9601")
            self.func.ClickButtonByName("退出")
        except AssertionError as e:
            raise AssertionError('客户端初始化' + "异常||原因：" + str(e))
        except Exception as e:
            raise CustomizationError('客户端初始化' + "异常||原因：" + str(e))

    def test_view_individualstock(self):
        """
        个股菜单查看集合竞价价格
        :return:
        """
        try:
            self.func.openprograms(r'C:\new_dwzq\TdxW.exe')
            sleep(5)
            self.func.ClickPaneByAutomationId("365")
            sleep(5)
            self.func.dealWithpopup()
            sleep(2)
            self.func.TapKeyBoard('6')
            self.func.TapKeyBoard('0')
            self.func.TapKeyBoard('1')
            self.func.TapKeyBoard('5')
            self.func.TapKeyBoard('5')
            self.func.TapKeyBoard('5')
            sleep(5)
            self.func.DoubleClickByNameByListItem("601555  东吴证券             上海A股")
            sleep(5)
            self.func.screenallshoot()
            sleep(2)
            strMsgText = self.func.baiduOCR()
            assert strMsgText != ' '
            self.func.ClickPaneByAutomationId("9601")
            self.func.ClickButtonByName("退出")
        except AssertionError as e:
            raise AssertionError('客户端运行' + "异常||原因：" + str(e))
        except Exception as e:
            raise CustomizationError('客户端运行' + "异常||原因：" + str(e))
    #
    # def test_Marketrefresh(self):
    #     """
    #     查看板块行情刷新
    #     :return:
    #     """
    #     try:
    #         self.func.openprograms(r'C:\new_dwzq\TdxW.exe')
    #         sleep(15)
    #         self.func.ClickPaneByAutomationId("365")
    #         sleep(15)
    #         self.func.dealWithpopup()
    #         sleep(2)
    #         self.func.TapKeyBoard('.')
    #         self.func.TapKeyBoard('6')
    #         self.func.TapKeyBoard('4')
    #         self.func.TapKeyBoard('7')
    #         sleep(5)
    #         self.func.DoubleClickByNameByListItem(".647    中金所期货          市场类型")
    #         sleep(2)
    #         self.func.screenshoot(200,20,1700,950)
    #         sleep(2)
    #         strMsgText1 = self.func.baiduOCR()
    #         sleep(10)
    #         self.func.screenshoot(200,20,1700,950)
    #         sleep(2)
    #         strMsgText2 = self.func.baiduOCR()
    #         assert strMsgText1 != strMsgText2
    #         self.func.ClickPaneByAutomationId("9601")
    #         self.func.ClickButtonByName("退出")
    #     except AssertionError as e:
    #         raise AssertionError('客户端运行' + "异常||原因：" + str(e))
    #     except Exception as e:
    #         raise CustomizationError('客户端运行' + "异常||原因：" + str(e))

    def test_viewSH_ListDetails(self):
        """
        查看上证成交明细菜单
        :return:
        """
        try:
            self.func.openprograms(r'C:\new_dwzq\TdxW.exe')
            sleep(15)
            self.func.ClickPaneByAutomationId("365")
            sleep(15)
            self.func.dealWithpopup()
            sleep(2)
            self.func.TapF(114)
            self.func.TapKeyBoard('0')
            self.func.TapKeyBoard('1')
            sleep(10)
            self.func.DoubleClickByNameByListItem("01      分时成交明细          功能键")
            sleep(5)
            self.func.screenallshoot()
            sleep(2)
            strMsgText = self.func.baiduOCR()
            sleep(8)
            print(strMsgText)
            assert strMsgText != ''
            self.func.ClickPaneByAutomationId("9601")
            self.func.ClickButtonByName("退出")
        except AssertionError as e:
            raise AssertionError('客户端运行' + "异常||原因：" + str(e))
        except Exception as e:
            raise CustomizationError('客户端运行' + "异常||原因：" + str(e))

    def test_viewSZ_ListDetails(self):
        """
        查看深证成交明细菜单
        :return:
        """
        try:
            self.func.openprograms(r'C:\new_dwzq\TdxW.exe')
            sleep(15)
            self.func.ClickPaneByAutomationId("365")
            sleep(15)
            self.func.dealWithpopup()
            sleep(2)
            self.func.TapF(115)
            self.func.TapKeyBoard('0')
            self.func.TapKeyBoard('1')
            sleep(10)
            self.func.DoubleClickByNameByListItem("01      分时成交明细          功能键")
            sleep(5)
            self.func.screenallshoot()
            sleep(2)
            strMsgText = self.func.baiduOCR()
            sleep(8)
            print(strMsgText)
            assert strMsgText != ''
            self.func.ClickPaneByAutomationId("9601")
            self.func.ClickButtonByName("退出")
        except AssertionError as e:
            raise AssertionError('客户端运行' + "异常||原因：" + str(e))
        except Exception as e:
            raise CustomizationError('客户端运行' + "异常||原因：" + str(e))