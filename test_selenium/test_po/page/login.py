# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2020/12/21 10:49 上午
# @Author :Amaris
# @File   :login.py
from selenium.webdriver.common.by import By

from test_selenium.test_po.page.base_page import BasePage
from test_selenium.test_po.page.register import Register


class Login(BasePage):
    def scan(self):
        pass

    def goto_register(self):
        self.find(By.CSS_SELECTOR, ".login_registerBar_link").click()
        return Register(self._driver)

