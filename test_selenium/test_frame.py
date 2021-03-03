# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2020/12/19 3:09 下午
# @Author :Amaris
# @File   :test_frame.py
import time

from selenium import webdriver

from test_selenium.base import Base


class TestFrame(Base):

    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        # self.driver.switch_to_frame("iframeResult")
        self.driver.switch_to.frame("iframeResult")
        print(self.driver.find_element_by_id("draggable").text)

        # self.driver.switch_to.parent_frame()
        self.driver.switch_to.default_content()

        print(self.driver.find_element_by_id("submitBTN").text)




