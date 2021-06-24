# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2020/12/22 11:06 下午
# @Author :Amaris
# @File   :test_appium3.py.py
'''
录播课4
'''
from time import sleep

import pytest
from appium import webdriver

class TestDW():
    def setup(self):
        desired_caps={}
        desired_caps["platformName"] = "Android"
        desired_caps["platformVersion"] = "6.0"
        desired_caps["deviceName"] = "emulator-5554"
        desired_caps["appPackage"] = "com.xueqiu.android"
        desired_caps["appActivity"] = ".view.WelcomeActivityAlias"
        desired_caps["noReset"] = "true"
        # desired_caps["dontStopAppOnReset"] = "true"
        desired_caps["skipDeviceInitialization"] = "true"
        desired_caps["unicodeKeyBoard"] = "true"
        desired_caps["resetKeyBoard"] = "true"


        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def setdown(self):
        self.driver.quit()
    def test_search(self):
        '''
        1、打开雪球app
        2、点击搜索输入框
        3、向搜索框输入"阿里巴巴"
        4、在搜索结果里面选择"阿里巴巴"，然后进行点击
        5、获取这支香港阿里巴巴的股价，并判断这支股价的价格>200
        :return:
        '''
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath()

if __name__ == '__main__':
    pytest.mian()
