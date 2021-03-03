# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2020/12/19 5:18 下午
# @Author :Amaris
# @File   :test_fileup.py
import time

from test_selenium.base import Base


class TestFileup(Base):
    def test_fileup(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element_by_xpath("//*[@id='sttb']/img[1]").click()
        self.driver.find_element_by_id("uploadImg").send_keys("image/褚璇玑.jpeg")
        time.sleep(3)
