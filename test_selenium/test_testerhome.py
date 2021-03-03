# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2020/12/18 4:25 下午
# @Author :Amaris
# @File   :test_testerhome.py

# 1.导入依赖
from selenium import webdriver


class TestTesterhome():

    def setup(self):
        # Chrome浏览器
        self.driver = webdriver.Chrome()
        # 最大化浏览器窗口
        self.driver.maximize_window()
        # 隐式等待，全局，设置过长时间时会对测试效率等影响
        self.driver.implicitly_wait(5)

    def teardown(self):
        # 推出浏览器
        self.driver.quit()

    def test_hogwarts(self):
        # 测试网址
        self.driver.get("https://testerhome.com/")
        # 对网页元素进行定位和操作
        self.driver.find_element_by_link_text("社团").click()
        self.driver.find_element_by_link_text("Testerhome测试媛测开群").click()
