# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2020/12/16 4:01 下午
# @Author :Amaris
# @File   :test_fixture_demo.py

from test_pytest.tests.fixtures import calc_init

# 用例
def test_calc_demo1(calc_init):
    assert calc_init.mul(1, 2) == 2

# 用例
def test_calc_demo2(calc_init):
    assert calc_init.mul(1, 3) == 3

# 用例，类似有些需要登陆有些不需要登陆使用
def test_calc_demo3():
    assert 1 == 1