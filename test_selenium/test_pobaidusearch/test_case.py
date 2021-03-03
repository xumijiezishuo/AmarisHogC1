# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2020/12/19 6:28 下午
# @Author :Amaris
# @File   :test_case.py
from test_selenium.test_pobaidusearch.main import Main


class TestCase:
    def setup(self):
        main = Main()
        main.click_first_link().title()