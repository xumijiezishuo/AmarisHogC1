# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2020/12/19 4:30 下午
# @Author :Amaris
# @File   :test_javascript.py
from time import sleep

import pytest

from test_selenium.base import Base


class TestJavascript(Base):
    @pytest.mark.skip
    def test_js_scroll(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_id("kw").send_keys("selenium测试")
        ele = self.driver.execute_script("return document.getElementById('su')")
        ele.click()
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        self.driver.find_element_by_xpath("//*[@id='page']/div/a[10]").click()
        sleep(3)

        # for code in [
        #     'return document.title', 'return JSON.stringify(performance.timing)'
        # ]:
        #     print(self.driver.execute_script(code))

        print(self.driver.execute_script('return document.title', 'return JSON.stringify(performance.timing)'))

    def test_datetime(self):
        self.driver.get("https://www.12306.cn/index/")
        ele_date = self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")
        self.driver.execute_script("document.getElementById('train_date').value='2020-12-30'")
        # 有无sleep会导致显示最终的取值是设置的值还是12306原本的值
        # sleep(3)
        print(self.driver.execute_script("return document.getElementById('train_date').value"))
