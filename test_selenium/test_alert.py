# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2020/12/19 5:49 下午
# @Author :Amaris
# @File   :test_alert.py
from time import sleep

from selenium.webdriver import ActionChains

from test_selenium.base import Base


class TestAlert(Base):
    def test_alert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        ele_drag = self.driver.find_element_by_xpath("//*[@id='draggable']")
        ele_drop = self.driver.find_element_by_xpath("//*[@id='droppable']")
        action = ActionChains(self.driver)
        action.drag_and_drop(ele_drag, ele_drop).perform()
        sleep(5)

        self.driver.switch_to.alert.accept()
        print("点击alert 确认")

        sleep(2)

        self.driver.switch_to.default_content()

        self.driver.find_element_by_id("submitBTN").click()



