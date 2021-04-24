#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "ChenXiaoFeng"
# Email: 929240396@qq.com
# Date: 2021/4/20
import win32api
from PIL import ImageGrab
import subprocess
import uiautomation as automation
import pytest
import allure
import os
import logging
import time
import pyautogui
from time import sleep
from datetime import datetime
from selenium import webdriver
# from pykeyboard import PyKeyboard
from aip import AipOcr
from pykeyboard import PyKeyboard

txtpath = 'C:/Users/Administrator/Desktop/md5.txt' #md5本地保存路径
PATH = os.path.abspath(os.path.join(os.path.dirname(__file__)))
global logger, path, driver
path = os.path.join(os.path.split(PATH)[0], 'result')
dir_path = 'C:\新建文件夹'  # 客户端本地下载路径
dataname = os.listdir(dir_path)[0]
screenshootjpg = r'C:\行情截图\1.jpg'
threadName = '10000'
# 创建一个logger
# logger = logging.getLogger("pyLogging")
# logger.setLevel(logging.INFO)
# 创建一个handler，用于写入日志文件
# fh = logging.FileHandler(os.path.join(path, 'log/0000.txt'))
# 定义handler的输出格式formatter
formatter = logging.Formatter('%(message)s')
# fh.setFormatter(formatter)
# 给logger添加handler
# logger.addHandler(fh)

class CustomerAsserts:

    def __init__(self, left, right):
        self.left = left
        self.right = right
        try:
            if isinstance(self.right, list) and isinstance(self.left, str):
                for k in self.right:
                    if self.left.find(k) >= 0:
                        self.left = k
            assert self.left in self.right
        except AssertionError:
            raise AssertionError("实际结果：%s" % str(self.left))

class BaseDriverPC:

    def __init__(self):
        pass

    def Log(self, msg):
        global threadName
        logger.info(threadName + "." + datetime.now().strftime("%H:%M:%S") + msg)

    def Login(self):
        self.screenshoot(650,350,800,800)
        msg = self.baiduOCR()
        if '输入账号' in msg:
            self.ClickButtonByName("输入账号")
        else:
            pass

    # 弹窗处理
    def dealWithpopup(self):
        self.screenallshoot()
        sleep(2)
        text = self.baiduOCR()
        sleep(5)
        if "今日不再提示" in text:
            self.DoubleClickByAutomationIdByButton("2")
        else:
            pass

    def TapKeyBoard(self,keys):
        sleep(1)
        k = PyKeyboard()
        k.type_string(keys)

    def TapF(self, keys):
        sleep(1)
        win32api.keybd_event(keys,0,0,0)


    def QuitDriver(self):
        try:
            sleep(2)
            driver.quit()
        except Exception as e:
            print(str(e))

    def startfile(self,filename): #打开文件
        try:
            os.startfile(filename)
        except:
            subprocess.Popen(['xdg-open', filename])

    def openprograms(self, url):
        try:
            sleep(2)
            subprocess.Popen(url)
        except Exception as e:
            print("程序加载异常" + '||原因：' + str(e))

    def IsNull(self,dir_path):
        """
        根据下载路径确认是否下载成功
        """
        pass

    @allure.step('点击按钮：{1}')
    def ClickButtonByName(self, name):
        try:
            sleep(2)
            automation.ButtonControl(Name = name).Click()
        except Exception as e:
            print("按钮点击异常" + '||原因：' + str(e))

    @allure.step('点击按钮：{1}')
    def ClickTextByName(self, name):
        try:
            sleep(2)
            automation.TextControl(Name = name).Click()
        except Exception as e:
            print("文本点击异常" + '||原因：' + str(e))

    @allure.step('点击按钮：{1}')
    def ClickEditByName(self, name):
        try:
            sleep(2)
            automation.EditControl(Name = name).Click()
        except Exception as e:
            print("编辑位置点击异常" + '||原因：' + str(e))

    @allure.step('点击按钮：{1}')
    def ClickMenuByName(self, name):
        try:
            sleep(2)
            automation.MenuItemControl(Name = name).Click()
        except Exception as e:
            print("菜单按钮点击异常" + '||原因：' + str(e))

    @allure.step('点击按钮：{1}')
    def ClickListItemByName(self, name):
        try:
            sleep(2)
            automation.ListItemControl(Name = name).Click()
        except Exception as e:
             print("ListItem点击异常" + '||原因：' + str(e))

    @allure.step('点击按钮：{1}')
    def ClickCheckBoxByName(self, name):
        try:
            sleep(2)
            automation.CheckBoxControl(Name=name).Click()
        except Exception as e:
            print("复选框点击异常" + '||原因：' + str(e))

    @allure.step('点击按钮：{1}')
    def ClickWindowByName(self, name):
        try:
            sleep(2)
            automation.WindowControl(Name=name).Click()
        except Exception as e:
            print("窗口程序点击异常" + '||原因：' + str(e))

    @allure.step('点击按钮：{1}')
    def ClickEditByClassName(self, classname):
        try:
            sleep(2)
            automation.EditControl(ClassName = classname).Click()
        except Exception as e:
            print("按钮点击异常" + '||原因：' + str(e))

    @allure.step('点击按钮：{1}')
    def ClickMenuByClassName(self, classname):
        try:
            sleep(2)
            automation.MenuItemControl(ClassName = classname).Click()
        except Exception as e:
            print("菜单按钮点击异常" + '||原因：' + str(e))

    @allure.step('点击按钮：{1}')
    def ClickToolBarByAutomationId(self, automationId):
        try:
            sleep(2)
            automation.ToolBarControl(AutomationId = automationId).Click()
        except Exception as e:
            print("菜单按钮点击异常" + '||原因：' + str(e))

    @allure.step('点击按钮：{1}')
    def ClickPaneByAutomationId(self, automationId):
        try:
            sleep(2)
            automation.PaneControl(AutomationId = automationId).Click()
        except Exception as e:
            print("Pane点击异常" + '||原因：' + str(e))

    @allure.step('点击按钮：{1}')
    def ClickButtonByAutomationId(self, automationId):
        try:
            sleep(2)
            automation.ButtonControl(AutomationId = automationId).Click()
        except Exception as e:
            print("菜单按钮点击异常" + '||原因：' + str(e))

    @allure.step('点击按钮：{1}')
    def RightClickButtonByName(self, name):
        try:
            sleep(2)
            automation.ButtonControl(Name = name).RightClick()
        except Exception as e:
            print("按钮右击异常" + '||原因：' + str(e))

    @allure.step('点击按钮：{1}')
    def RightClickWindowByName(self, name):
        try:
            sleep(2)
            automation.WindowControl(Name = name).RightClick()
        except Exception as e:
            print("窗口程序右击异常" + '||原因：' + str(e))

    @allure.step('点击按钮：{1}')
    def RightClickListItemByName(self, name):
        try:
            sleep(2)
            automation.ListItemControl(Name= name ).RightClick()
        except Exception as e:
            print("ListItem右击异常" + '||原因：' + str(e))

    @allure.step('点击按钮：{1}')
    def RightClickMenuItemByName(self, name):
        try:
            sleep(2)
            automation.MenuItemControl(Name= name ).RightClick()
        except Exception as e:
            print("按钮右击异常" + '||原因：' + str(e))

    @allure.step('点击按钮：{1}')
    def ClickByXY(self, X, Y):
        try:
            sleep(2)
            automation.Click(X, Y)
        except Exception as e:
            print("坐标点击异常" + '||原因：' + str(e))

    @allure.step('点击按钮：{1}')
    def DoubleClickByNameByListItem(self, name):
        try:
            sleep(2)
            automation.ListItemControl(Name = name).DoubleClick()
        except Exception as e:
            print("列表双击异常" + '||原因：' + str(e))

    @allure.step('点击按钮：{1}')
    def DoubleClickByAutomationIdByButton(self, automationId):
        try:
            sleep(2)
            automation.ButtonControl(AutomationId = automationId).DoubleClick()
        except Exception as e:
            print("按钮双击异常" + '||原因：' + str(e))

    @allure.step('点击按钮：{1}')
    def DoubleClickByName(self, name):
        try:
            sleep(2)
            automation.TextControl(Name = name).DoubleClick()
        except Exception as e:
            print("文本点击异常" + '||原因：' + str(e))

    def GetMd5Bytxt(self):
        with open(txtpath) as file_obj:
            txt = file_obj.read().upper()
            return txt

    def GetDirNames(self):
        for root, dirs, files in os.walk('C:/Users/Administrator/Desktop'):
            return files

    def GetMd5ByXpath(self, url, xpath):
        try:
            sleep(2)
            chromedriver = r'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
            browser = webdriver.Chrome(chromedriver)
            browser.get(url)
            browser.maximize_window()
            sleep(2)
            MD5 = browser.find_element_by_xpath(xpath).text
            sleep(2)
            browser.close()
            return MD5
        except Exception as e:
            print("获取MD5值异常" + '||原因：' + str(e))

    def DownTDX(self):
        try:
            sleep(2)
            chromedriver = r'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
            browser = webdriver.Chrome(chromedriver)
            browser.get("https://cdn.showcai.com.cn/swdownload/index/app.html")
            browser.maximize_window()
            sleep(2)
            browser.find_element_by_id("menu2").click()
            el = driver.find_element_by_xpath("/html/body/form/div[3]/div[15]/div[2]/div[1]/div")
            browser.execute_script("arguments[0].scrollIntoView();",el)
            sleep(2)
            browser.find_element_by_xpath("/html/body/form/div[3]/div[15]/div[1]/div[2]/a").click()
            sleep(100)
        except Exception as e:
            print("获取MD5值异常" + '||原因：' + str(e))


    def Sendkeys(self,keys):
        automation.SendKeys(keys)

    def SendKeysByEditClassName(self, classname, keys):
        try:
            sleep(2)
            el = automation.EditControl(ClassName = classname)
            el.SendKeys(keys)
        except Exception as e:
            print("输入值异常" + '||原因：' + str(e))

    def SetTopMostByName(self, name):
        try:
            sleep(2)
            el = automation.WindowControl(searchDepth=1, Name = name)
            el.SetTopmost(True)
        except Exception as e:
            print("窗口置顶异常" + '||原因：' + str(e))

    def ClosePrograms(self):
        os.remove(txtpath) #删除md5文件
        sleep(1)
        self.RightClickButtonByName("Hasher")
        self.ClickListItemByName("关闭窗口")
        sleep(1)
        self.RightClickButtonByName("软件下载 - Google Chrome")
        time.sleep(2)
        self.ClickListItemByName("关闭窗口")

    # 截图
    def screenshoot(self, x, y, w, h):
        im = pyautogui.screenshot(region=(x, y, w, h))
        im.save(screenshootjpg)

    # 全屏截图
    def screenallshoot(self):
        im = ImageGrab.grab()  #可以添加一个坐标元组进去
        im.save(screenshootjpg)

    # 百度识图
    def baiduOCR(self):
        result = ''
        APP_ID = '24046528'
        API_KEY = 'ycAGtCNL6rRdegHYc3fGzn16'
        SECRECT_KEY = 'wT5Zy7aHFVoZYcI07M36MBDqlUcpQuay'
        client = AipOcr(APP_ID, API_KEY, SECRECT_KEY)
        img = open(screenshootjpg, 'rb').read()
        message = client.basicGeneral(img)
        for item in message.get('words_result', 'None'):
            result += item['words'] + '\n'
        return result
