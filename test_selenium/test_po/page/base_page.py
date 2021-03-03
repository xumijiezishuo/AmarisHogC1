# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2020/12/19 6:48 下午
# @Author :Amaris
# @File   :base_page.py
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _base_url = ""
    # :WebDriver用来标记的，删除了也可以，但是删除了就可能使用driver.时没有联想出对应的方法，是用来解决类型识别的
    # 如果不传driver，每次调用每个类，每次都要初始化一个新的。应该要能复用，所以传进来
    def __init__(self, driver:WebDriver=None):
        self._driver = ""
        if driver is None:
            self._driver = webdriver.Chrome()
        else:
            self._driver = driver

        if self._base_url !="":
            self._driver.get(self._base_url)

    def find(self, by, locator):
        return self._driver.find_element(by, locator)



