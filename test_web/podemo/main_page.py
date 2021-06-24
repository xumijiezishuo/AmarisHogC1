# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2020/12/21 6:08 下午
# @Author :Amaris
# @File   :main_page.py
from selenium import webdriver
from selenium.webdriver.common.by import By

from test_web.podemo.login_page import LoginPage
from test_web.podemo.register_page import RegisterPage


class MainPage:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.implicitly_wait(5)

    def goto_login(self):
        # click login
        self.driver.find_element(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        # 进入到登录页面
        return LoginPage(self.driver)

    def goto_register(self):
        # click register
        self.driver.find_element(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        # 进入到注册页面
        return RegisterPage(self.driver)

