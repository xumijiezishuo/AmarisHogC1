# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2020/12/19 6:46 下午
# @Author :Amaris
# @File   :main.py
from selenium.webdriver.common.by import By

from test_selenium.test_po.page.base_page import BasePage
from test_selenium.test_po.page.login import Login
from test_selenium.test_po.page.register import Register


class Main(BasePage):
    # 继承，重写_base_url
    _base_url = "https://work.weixin.qq.com/"
    def goto_register(self):
        self.find(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        return Register(self._driver)

    def goto_login(self):
        self.find(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        return Login(self._driver)

