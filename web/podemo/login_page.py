# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2020/12/21 6:15 下午
# @Author :Amaris
# @File   :login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web.podemo.register_page import RegisterPage


class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def scan(self):
        pass

    def goto_register(self):
        # click register
        self.driver.find_element(By.CSS_SELECTOR, ".login_registerBar_link").click()
        # enter register page
        return RegisterPage(self.driver)
