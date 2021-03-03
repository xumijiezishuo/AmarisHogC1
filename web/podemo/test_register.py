# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2020/12/21 6:25 下午
# @Author :Amaris
# @File   :test_register.py
from web.podemo.main_page import MainPage


class TestRegister:
    def setup(self):
        self.main = MainPage()

    def test_register(self):
        # result = self.main.goto_login().goto_register().register()
        result = self.main.goto_register().register()
        assert result

