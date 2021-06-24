# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2021/6/23 4:51 下午
# @Author :Amaris
# @File   :test_contact.py
from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestWX:

    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "qiyeweixin"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "True"

        # 与server建立连接，固定写法，IP可根据实际配置，实际上是创建了一个session
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    # 添加成员，用skip跳过执行该用例
    @pytest.mark.skip
    def test_contact(self):
        name = "hogwarts_00003"
        gender = "男"
        phonenum = "13812121214"
        # 点击【通讯录】
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # 点击【添加成员】
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("添加成员").instance(0));').click()
        # 点击【手动输入添加】
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "姓名")]/../android.widget.EditText').send_keys(name)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='性别']/..//*[@text='男']").click()
        if gender == "男":
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()

        self.driver.find_element(MobileBy.XPATH, "//*[@text='手机号']").send_keys(phonenum)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        # print(self.driver.page_source)
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']").click()
        result = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        assert result == "添加成功"
        print(self.driver.page_source)

    # 删除成员
    # 搜索的元素是在当前手机屏进行的，展示的屏上有多少个相关的元素就能查找到多少个（注意成员的部门公司里面是否也有相关的关键字，如果所属部门也是相关的，那么删除一个相关成员，就相当于少了2个相关元素），注意不止一屏相关数据时的展示
    def test_remove(self):
        search_name = "测试123"
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/hci').click()
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/g5f').send_keys(search_name)
        sleep(2)
        ele_list1 = self.driver.find_elements(MobileBy.XPATH, f"//*[contains(@text,'{search_name}')]")
        # print(f"删除前搜索到的元素：{ele_list1}\n")
        ele_beforelen = len(ele_list1)
        print(f"删除前搜索的元素个数为：{ele_beforelen}\n")
        # 搜索关键字也算一个元素
        if ele_beforelen < 2:
            print("没有可删除的人员")
        else:
            ele_list1[1].click()
            self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/hc9').click()
            self.driver.find_element(MobileBy.XPATH, "//*[@text='编辑成员']").click()
            self.driver.find_element(MobileBy.XPATH, "//*[@text='删除成员']").click()
            # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
            #                          'new UiScrollable(new UiSelector()'
            #                          '.scrollable(true).instance(0))'
            #                          '.scrollIntoView(new UiSelector()'
            #                          '.text("删除成员").instance(0));').click()
            self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']").click()

            sleep(2)
            self.driver.back()
            self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/hci').click()
            self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/g5f').send_keys(search_name)
            sleep(2)
            ele_list2 = self.driver.find_elements(MobileBy.XPATH, f"//*[contains(@text,'{search_name}')]")
            ele_afterlen = len(ele_list2)
            # print(f"删除后搜索到的元素：{ele_list2}\n")
            print(f"删除后搜索的元素个数为：{ele_afterlen}\n")
            assert ele_afterlen == ele_beforelen-1















