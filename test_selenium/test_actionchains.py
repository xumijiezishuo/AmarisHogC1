# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2020/12/19 11:29 上午
# @Author :Amaris
# @File   :test_actionchains.py
import time
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

'''
move to 操作还未调试成功
'''
class TestActionChains:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        # self.driver.find_element_by_xpath("/html/body/form/input[3]").click()
        element_click = self.driver.find_element_by_xpath("//input[@value='click me']")
        element_doubleclick = self.driver.find_element_by_xpath("//input[@value='dbl click me']")
        element_rightclick = self.driver.find_element_by_xpath("//input[@value='right click me']")
        action = ActionChains(self.driver)
        action.click(element_click)
        action.double_click(element_doubleclick)
        action.context_click(element_rightclick)

        time.sleep(3)

        action.perform()

        time.sleep(5)

    # def test_movetoelement(self):
    #     self.driver.get("https://www.baidu.com/")
    #     self.driver.find_element_by_link_text("新闻")
    #     action = ActionChains(self.driver)
    #     action.move_to_element(action)
    #     action.perform()
    #     time.sleep(10)
    @pytest.mark.skip
    def test_case(self):
        self.driver.get("https://www.baidu.com/")
        eleclick1 = self.driver.find_element_by_link_text("新闻")
        action = ActionChains(self.driver)
        # eleclick = action.move_to_element(self.driver.find_element_by_link_text("新闻"))
        time.sleep(3)
        action.click(eleclick1)
        action.perform()
        time.sleep(2)

    # 把一个元素拖动到另一个元素
    def test_dragdrop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        ele_drag = self.driver.find_element_by_id("dragger")
        ele_drop = self.driver.find_element_by_xpath("/html/body/div[2]")
        action = ActionChains(self.driver)

        # action.drag_and_drop(ele_drag, ele_drop).perform()
        # action.click_and_hold(ele_drag).release(ele_drop).perform()
        action.click_and_hold(ele_drag).move_to_element(ele_drop).release().perform()

        time.sleep(4)

    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele = self.driver.find_element_by_xpath("/html/body/label[1]/input")
        ele.click()
        action = ActionChains(self.driver)
        action.send_keys("username").pause(5)
        action.send_keys(Keys.SPACE).pause(5)
        action.send_keys("tom").pause(5)
        action.send_keys(Keys.BACK_SPACE).perform()
        time.sleep(3)
















# # 执行方式
# if __name__ == '__main__':
#     pytest.main('-v', '-s', 'test_actionchains.py')

