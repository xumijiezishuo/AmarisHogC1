# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2020/12/19 3:09 下午
# @Author :Amaris
# @File   :test_form.py
import time

from selenium import webdriver

from test_selenium.base import Base


class TestWindow(Base):

    def test_window(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_link_text("登录").click()
        print(self.driver.window_handles)
        print(self.driver.current_window_handle)
        # 有时输入的文字明明正确却报错的，在检查元素页面直接复制进来
        self.driver.find_element_by_link_text("立即注册").click()
        print(self.driver.window_handles)

        windows = self.driver.window_handles

        self.driver.switch_to_window(windows[-1])

        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("username")
        self.driver.find_element_by_id("TANGRAM__PSP_4__phone").send_keys("13800000000")
        time.sleep(3)

        self.driver.switch_to_window(windows[0])
        self.driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()
        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("login_username")
        self.driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys("login_password")

        time.sleep(3)



        time.sleep(3)
