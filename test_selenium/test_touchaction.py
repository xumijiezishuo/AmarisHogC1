# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2020/12/19 2:49 下午
# @Author :Amaris
# @File   :test_touchaction.py
import time

from selenium import webdriver
from selenium.webdriver import TouchActions


class TestTouchAction:

    def setup(self):
        # 处理不是w3c标准报错
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)

        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_touchaction(self):
        self.driver.get("https://www.baidu.com/")
        el = self.driver.find_element_by_id("kw")
        el_search = self.driver.find_element_by_id("su")

        el.send_keys("selenium测试")
        action = TouchActions(self.driver)
        action.tap(el_search)
        action.perform()
        # 滑到底部，设置很大的偏移量
        action.scroll_from_element(el, 0, 10000).perform()
        time.sleep(3)





