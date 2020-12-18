# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2020/12/16 6:51 下午
# @Author :Amaris
# @File   :test_order.py
import pytest


class TestPytest(object):

    @pytest.mark.run(order=-1)
    def test_two(self):
        print("test_two")

    @pytest.mark.run(order=-3)
    def test_one(self):
        print("test_one")

    @pytest.mark.run(order=1)
    def test_three(self):
        print("test_three")