# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2020/12/18 3:06 下午
# @Author :Amaris
# @File   :test_selenium.py

import selenium
from selenium import webdriver

def test_selenium():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com/")
