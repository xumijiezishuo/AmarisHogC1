# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2020/12/22 11:06 下午
# @Author :Amaris
# @File   :test_appium3.py.py
'''
录播课3
'''
from time import sleep

from appium import webdriver

desired_caps={}
desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "6.0"
desired_caps["deviceName"] = "emulator-5554"
desired_caps["appPackage"] = "com.xueqiu.android"
desired_caps["appActivity"] = ".view.WelcomeActivityAlias"
desired_caps["noReset"] = "true"
desired_caps["dontStopAppOnReset"] = "true"
desired_caps["skipDeviceInitialization"] = "true"

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)
driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
driver.find_element_by_id("com.xueqiu.android:id/search_input_text").click()
driver.back()
driver.back()
driver.quit()
