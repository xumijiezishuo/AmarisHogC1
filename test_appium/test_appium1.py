# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2020/12/22 12:23 上午
# @Author :Amaris
# @File   :test_appium1.py
'''
录播课1,未调试成功
'''
from appium import webdriver

desired_caps={}
desired_caps['platformName'] = 'Andriod'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'com.andriod.settings'
desired_caps['appActivity'] = 'com.andriod.settings.Setting'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.quit()

