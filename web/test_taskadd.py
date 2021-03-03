# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2020/12/21 3:56 下午
# @Author :Amaris
# @File   :test_taskadd.py

import shelve
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from web.func import username, memberAdd_acctid, memberAdd_phone

'''
作业:使用 cookie 登录企业微信，完成添加联系人，加上断言验证
'''
class TestTaskadd:
    def setup(self):
        # 复用浏览器,在此之前先命令行启动chrome，可以先登录到企业微信，可以复用已登录的状态
        option = Options()
        option.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_taskadd(self):
        db = shelve.open('cookies')
        cookies = db['cookie']
        db.close
        # 打开无痕新页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # 存入cookie
        for cookie in cookies:
            # 删除expiry
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        # 刷新当前页面，获取登录状态
        self.driver.refresh()
        # 点击【添加成员】
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()
        # 输入姓名、账号、手机号码并点击保存按钮
        name = username()
        accid = memberAdd_acctid()
        phone = memberAdd_phone()
        self.driver.find_element(By.ID, "username").send_keys(name)
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys(accid)
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys(phone)
        self.driver.find_element(By.CSS_SELECTOR, ".js_member_editor_form>div:nth-child(1)>a:nth-child(2)").click()
        # 断言
        tips = self.driver.find_element(By.ID, "js_tips").text
        assert "保存成功" == tips

        sleep(10)



