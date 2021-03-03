# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2020/12/19 3:26 下午
# @Author :Amaris
# @File   :base.py
import os

from selenium import webdriver

class Base:

    def setup(self):
        # 多浏览器
        # 接收参数  如执行测试用例命令为： browser=firefox  pytest test_frame.py
        browser = os.getenv("browser")
        if browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "headless":
            self.driver = webdriver.PhantomJS()
        else:
            self.driver = webdriver.Chrome()


        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()
