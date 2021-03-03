# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2020/12/21 11:28 上午
# @Author :Amaris
# @File   :test_demo.py

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTestcase():
    def setup_method(self, method):
        # 需要把浏览器驱动配置到环境变量才可直接使用，否则会报错找不到驱动
        # self.driver = webdriver.Firefox()


        self.driver = webdriver.Chrome()

        # 没有把驱动配置到环境变量的情况下使用
        # self.driver = webdriver.Firefox(executable_path="浏览器驱动所在的路径")

        # 隐式等待
        self.driver.implicitly_wait(5)



    def teardown_method(self, method):
        self.driver.quit()

    def test_testcase(self):
        self.driver.get("https://ceshiren.com/")
        self.driver.find_element(By.LINK_TEXT, "所有分类").click()

        element = self.driver.find_element(By.LINK_TEXT, "所有分类")
        # 获取class属性
        result = element.get_attribute("class")
        assert 'active' == result

    def test_wx(self):
        # 新打开的窗口是一个无痕的窗口
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(10)


