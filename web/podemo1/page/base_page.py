# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2021/3/22 5:20 下午
# @Author :Amaris
# @File   :base_page.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _base_url = ""
    def __init__(self, driver:WebDriver = None):
        if driver == None:
            option = Options()
            option.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=option)
            self.driver.implicitly_wait(20)
        else:
            self.driver = driver
        if self._base_url != "":
            self.driver.get(self._base_url)

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)






