# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2020/12/21 7:04 下午
# @Author :Amaris
# @File   :add_member_page.py
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web.podemo1.page.base_page import BasePage


class AddMemberPage(BasePage):

    def add_member(self, name, accid, phone):
        # input name
        self.find(By.ID, "username").send_keys(name)
        # input account
        self.find(By.ID, "memberAdd_acctid").send_keys(accid)
        # input phonenum
        self.find(By.ID, "memberAdd_phone").send_keys(phone)
        # click save
        # 如果页面上相同属性的元素有多个， 那么 通过 find_element 定位到的元素是第一次出现的元素
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()

        return True

    def get_member(self):
        # # find_elements方法返回的是元素列表 [element1,elemnt2,.....]
        # elements = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        # titles = [element.get_attribute("title") for element in elements]
        # return titles

        # 考虑分页问题，元素不在首页
        title_total = []
        while True:
            elements = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
            titles = [element.get_attribute("title") for element in elements]
            title_total.extend(titles)

            page: str = self.find(By.CSS_SELECTOR, ".ww_pageNav_info_text").text
            num, total = page.split("/", 1)
            if int(num) == int(total):
                break
            else:
                self.find(By.CSS_SELECTOR, ".ww_commonImg_PageNavArrowRightNormal").click()

        return title_total


        # # 可用列表推导式达到同样的效果
        # titles = []
        # for element in elements:
        #     titles.append(element.get_attribute("title"))







