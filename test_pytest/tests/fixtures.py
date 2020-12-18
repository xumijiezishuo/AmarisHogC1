# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2020/12/16 4:00 下午
# @Author :Amaris
# @File   :fixtures.py
import pytest

from test_pytest.core.calc import Calc


@pytest.fixture(scope="module")
def calc_init():
    # 初始化的操作
    print("setup_class 函数")
    # 返回Calc()，Calc类中有方法如mul等
    return Calc()