# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2020/12/19 11:08 上午
# @Author :Amaris
# @File   :test_xpathandcss.py
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

'''
元素定位方式：XPATH，CSS SELECTOR
'''
class TestXpathcss:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")

    def test_xpathcss(self):
        # self.driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys("霍格沃兹测试学院")
        # self.driver.find_element(By.ID, 'kw').send_keys("霍格沃兹测试学院")
        # self.driver.find_element(By.CSS_SELECTOR, '#kw').send_keys("霍格沃兹测试学院")
        self.driver.find_element(By.CSS_SELECTOR, '[id=kw]').send_keys("霍格沃兹测试学院")

        self.driver.find_element(By.ID, 'su').click()



        time.sleep(2)
        self.driver.quit()
