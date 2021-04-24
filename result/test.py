import os
from time import sleep
from BaseFunction.basedriverWindows import BaseDriverPC, CustomerAsserts
from BaseFunction.basedriverWindows import dir_path, dataname, txtpath
import re

md5xpath = '//*[@id="swDownLoadForm"]/div[3]/div[20]/div[2]/div[3]/div'
chromepath = r'C:\Program Files\Google\Chrome\Application\chrome.exe'  # 浏览器启动路径
downloadurl = 'https://cdn.showcai.com.cn/swdownload/index/app.html'  # 客户端下载地址
md5path = r'C:\Program Files\新建文件夹\hasher\Hasher.exe'  # md5解码器路径
lastpath = os.path.join(dir_path, dataname)

func = BaseDriverPC()
sleep(5)
func.dealWithpopup()

# sleep(5)
# func.screenshoot(0, 1010, 400, 25)
# sleep(2)
# strMsgText =func.baiduOCR()
# pattern = re.compile('[0-9]+')
#
# match = pattern.findall(strMsgText)
# assert match != ''
# print(strMsgText)
# print(match)
