# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2020/12/21 6:46 下午
# @Author :Amaris
# @File   :index_page.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from test_web.podemo1.page.add_member_page import AddMemberPage
from test_web.podemo1.page.base_page import BasePage


class IndexPage(BasePage):
    # 先会实例化类变量才会去实例化init方法
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_add_member(self):
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()

        return AddMemberPage(self.driver)

