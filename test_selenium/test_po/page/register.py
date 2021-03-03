# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2020/12/21 10:37 上午
# @Author :Amaris
# @File   :register.py
from selenium.webdriver.common.by import By

from test_selenium.test_po.page.base_page import BasePage


class Register(BasePage):
    def register(self):
        self.find(By.ID, "corp_name").send_keys("hello1")
        self.find(By.ID, "manager_name").send_keys("hello2")
        return True




