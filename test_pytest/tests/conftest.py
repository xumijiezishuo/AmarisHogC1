# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2020/12/16 4:00 下午
# @Author :Amaris
# @File   :fixtures.py
import pytest

from test_pytest.core.calc import Calc
# 有了conftest文件会自动加载fixture，比如test_fixture_demo中的文件可以不导包
# tests下可分多个子包，每个子包下都有conftest文件，用于功能数据准备、维护管理数据，前置条件,跨多个类的
# 优先使用setup_class，特殊情况用fixture
# pytest.ini是用来
@pytest.fixture(scope="module")
def calc_init():
    # 初始化的操作
    print("setup_class 函数")
    # 返回Calc()，Calc类中有方法如mul等
    return Calc()