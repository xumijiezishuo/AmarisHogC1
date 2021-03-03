# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2020/12/21 10:54 上午
# @Author :Amaris
# @File   :test_register.py
from test_selenium.test_po.page.main import Main


class TestRegister:
    def setup(self):
        self.main = Main()

    def test_register(self):
        # assert self.main.goto_login().goto_register().register()
        assert self.main.goto_register().register()


