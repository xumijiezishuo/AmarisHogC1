# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2020/12/21 6:15 下午
# @Author :Amaris
# @File   :register_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class RegisterPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def register(self):
        # input company name
        self.driver.find_element(By.ID, "corp_name").send_keys("hello1")
        # input phonenum
        self.driver.find_element(By.ID, "register_tel").send_keys("13012345668")        # click register
        # click register
        self.driver.find_element(By.ID, "submit_btn").click()
        return True