# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2020/12/21 2:44 下午
# @Author :Amaris
# @File   :test_contact.py
import shelve
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

'''
浏览器复用
'''

class TestWX:
    def setup(self):
        # 复用浏览器,在此之前先命令行启动chrome，可以先登录到企业微信，可以复用已登录的状态
        option = Options()
        option.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()


    # def test_case1(self):
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
    #     self.driver.find_element(By.ID, "menu_contacts").click()

    @pytest.mark.skip
    def test_cookie(self):
        # 获取当前页面的cookie
        cookies = self.driver.get_cookies()
        # 格式化代码快捷键Ctrl + Alt + L（option+command+L）
        # 可以把cookies存到python自带的数据库中
        # cookies = [
        #     {'domain': '.qq.com', 'expiry': 1608534366, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
        #      'value': '1'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
        #      'value': '1688850902889602'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
        #      'value': 'tBFugfCjBaIaUsTtzCBhXco6xAxnh_WLHPADydaOu8j_EgPC9H0muWZLBjk8BH_rx43EUcZ6x8P7RqvGMAty8c05L_Mb_Uuzs7pBG1fL_2CJhs3Mcv1oILTz5ZMKdnqQyOa0BlQr-7-u6TMJVqYg1j9oMb2-ks_ophz3-ZsEw4u0DLuZ2uVfW283KT1jRxe78IWW-qJSYwsEP995fcZ8MZ0e7DtLE5gC6oJyi74YSvM0FC4oNNXYhLFc1VoFnRmJ_zMWlwzZJKnhJGAptwSktg'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
        #      'value': '1688850902889602'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
        #      'value': '1970324950203285'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
        #      'value': 'a9674083'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
        #      'value': 'L9Epu7fdMFA_nB6n4w1Wpqgb8xJ9wN7ZQfDVKBaS1ojoYs5nTJSSbvZV5t5AdkCj'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
        #      'value': '1'},
        #     {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
        #      'secure': False, 'value': '7284327319'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1640055144, 'httpOnly': False,
        #      'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
        #      'value': '1608102900,1608477503,1608516424'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
        #      'value': 'direct'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
        #      'value': '18992684712989258'},
        #     {'domain': '.qq.com', 'expiry': 1608620706, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
        #      'value': 'GA1.2.1422600789.1608477503'},
        #     {'domain': 'work.weixin.qq.com', 'expiry': 1608547777, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
        #      'secure': False, 'value': '2m3gved'},
        #     {'domain': '.qq.com', 'expiry': 1671606306, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
        #      'value': 'GA1.2.52401641.1608102900'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1639638899, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
        #      'path': '/', 'secure': False, 'value': '0'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1611126306, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
        #      'path': '/', 'secure': False, 'value': 'zh'}]

        # expiry在add_cookie时不支持小数，失效时间，可以去掉

        print(cookies)

        # 没有加cookie就不能进入
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        sleep(2)

        # 遍历cookies且加入
        for cookie in cookies:
            # 删除expiry
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        # 加了cookie后再次访问就能进入，也可以直接刷新页面
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.refresh()
        sleep(2)

    # 执行后会出现对应的db文件，表明已经存入成功
    @pytest.mark.skip
    def test_case2(self):
        cookies = [
            {'domain': '.qq.com', 'expiry': 1608534366, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688850902889602'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'tBFugfCjBaIaUsTtzCBhXco6xAxnh_WLHPADydaOu8j_EgPC9H0muWZLBjk8BH_rx43EUcZ6x8P7RqvGMAty8c05L_Mb_Uuzs7pBG1fL_2CJhs3Mcv1oILTz5ZMKdnqQyOa0BlQr-7-u6TMJVqYg1j9oMb2-ks_ophz3-ZsEw4u0DLuZ2uVfW283KT1jRxe78IWW-qJSYwsEP995fcZ8MZ0e7DtLE5gC6oJyi74YSvM0FC4oNNXYhLFc1VoFnRmJ_zMWlwzZJKnhJGAptwSktg'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688850902889602'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970324950203285'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a9674083'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'L9Epu7fdMFA_nB6n4w1Wpqgb8xJ9wN7ZQfDVKBaS1ojoYs5nTJSSbvZV5t5AdkCj'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '7284327319'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1640055144, 'httpOnly': False,
             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
             'value': '1608102900,1608477503,1608516424'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '18992684712989258'},
            {'domain': '.qq.com', 'expiry': 1608620706, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.1422600789.1608477503'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1608547777, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '2m3gved'},
            {'domain': '.qq.com', 'expiry': 1671606306, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.52401641.1608102900'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1639638899, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1611126306, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'}]

        # shelve模块，python自带的对象持久化存储
        db = shelve.open('cookies')
        db['cookie'] =cookies
        db.close

    # 使用已经存好的cookies文件
    @pytest.mark.skip
    def test_case3(self):
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


    def test_import(self):
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
        # 点击【导入通讯录】
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        # 上传文件，选择文件的完整路径上传
        self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_uploadInputMask").send_keys("/Users/qinchaolan/【测试开发工程师】四期学习计划.xlsx")
        # 断言上传文件名，与实际文件名一致
        result = self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_fileNames").text
        assert "【测试开发工程师】四期学习计划.xlsx" == result
        sleep(5)





    # def setup(self):
    #     # 复用浏览器,在此之前先命令行启动chrome，可以先登录到企业微信，可以复用已登录的状态
    #     option = Options()
    #     # 注意要与命令行启动的端口号一致
    #     option.debugger_address = "127.0.0.1:9222"
    #     self.driver = webdriver.Chrome(options=option)
    #
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
    #
    # def test_case1(self):
    #     pass







