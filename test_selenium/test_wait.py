# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2020/12/18 5:00 下午
# @Author :Amaris
# @File   :test_wait.py
'''
显示等待以及元素定位还需加深理解，当前模块暂未调试成功
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://ceshiren.com/")
        self.driver.implicitly_wait(10)
    def teardwon(self):
        self.driver.quit()

    def test_wait(self):
        self.driver.find_element(By.XPATH, '/html/body/section/div/div[2]/div[3]/div/section/ul/li[7]/a').click()
        # self.driver.find_element(By.XPATH, '/html/body/section/div/div[2]/div[5]/div[2]/div/div/div/div/div[1]/table/tbody/tr[1]/td[1]/h3/a/div/span').click()
        # self.driver.find_element(By.XPATH, '/html/body/section/div/div[2]/div[3]/div/section/div[2]/ul/li[7]/a').click()

        # # 该自定义方法一定需要有参数，用来接参
        # def wait(x):
        #         return len(self.driver.find_elements(By.XPATH, '//*[@id="ember346"]/div[1]')) >= 1
        # wait不要写括号，写括号就是调用而不是传递
        # WebDriverWait(self.driver, 10).until(wait)

        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(By.XPATH, '/html/body/section/div/div[2]/div[5]/div[2]/div/div/div/div/div[2]/div/div[1]'))
        self.driver.find_element(By.XPATH, '/html/body/section/div/div[2]/div[3]/div/section/ul/li[1]/a').click()


