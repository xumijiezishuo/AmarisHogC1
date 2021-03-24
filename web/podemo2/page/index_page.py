# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2020/12/21 6:46 下午
# @Author :Amaris
# @File   :index_page.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from web.podemo1.page.add_member_page import AddMemberPage


class IndexPage:
    def __init__(self):
        option = Options()
        option.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

    def goto_add_member(self):
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()

        return AddMemberPage(self.driver)

