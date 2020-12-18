# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2020/12/14 3:41 下午
# @Author :Amaris
# @File   :test_calc.py
import allure
import yaml

from test_pytest.core.calc import Calc
import pytest

# 尽量不要让用例之间有依赖
# 封装
def load_data(path='data.yaml'):
    with open(path) as f:
        data = yaml.safe_load(f)
        print("数据类型是", type(data))
        print("打印keys之前", data[0].keys())
        keys = ",".join(data[0].keys())
        print("打印keys", keys)
        values = [list(d.values()) for d in data]
        data = {'keys': keys, 'values': values}
        return data

# 则函数可以作为参数传入另一个函数，可作初始化操作
# @pytest.fixture
# def calc_init():
#     print("setup_class 函数")
#     return Calc()
@pytest.fixture(scope="module")
def calc_init():
    # 初始化的操作,根据fixture规定范围
    print("setup_class 函数")
    # 返回Calc()，Calc类中有方法如mul等
    return Calc()

# 用例
def test_calc_demo1(calc_init):
    assert calc_init.mul(1, 2) == 2

# 用例
def test_calc_demo2(calc_init):
    assert calc_init.mul(1, 3) == 3

class TestCalc:
    # # 平时推荐使用这个方法,实例方法,存的是实例变量
    # def setup_class(self):
    #     print("使用setup_class")
    #     self.calc = Calc()

    # 使用类级别的方法，同样效果，优先于上面的实例方法执行,即会override实例方法，存的是类变量
    @classmethod
    def setup_class(cls):
        print("setup_class method")
        with open('data.yaml') as f:
            data = yaml.safe_load(f)

            cls.calc = Calc()


    def setup(self):
        pass

    # 记录关键过程、数据，在allure报告中的Suites的测试用例中展示
    @allure.step
    def simple_step(self, step_param1, step_param2=None):
        pass

    # 正常值例子
    @pytest.mark.parametrize('a, b, c', [
        [1, 2, 2],
        [-1, -1, 1],
        [1, -1, -1],
        [1, 0, 0],
        [1, 1.3, 1.3]
    ])
    def test_mul(self, a, b, c):
        # 在测试用例追加截图
        allure.attach.file("/Users/qinchaolan/Pictures/明星/褚璇玑.jpeg",
                           "测试访谈", allure.attachment_type.PNG)
        # 在测试用例追加关键步骤
        self.simple_step(f"{a}{b}{c}")
        assert self.calc.mul(a, b) == c

    # 异常值例子浮点数相乘
    @pytest.mark.parametrize('a, b, c', [

        [1.1, 2.1, 2.31]
    ])
    def test_mul_error(self, a, b, c):
        with pytest.raises(AssertionError):
            assert self.calc.mul(a, b) == c
    #
    # # 正常值例子
    # @pytest.mark.parametrize('i, j, k', [
    #     [-8, -2, 4],
    #     [2.2, 1.1, 2],
    #     [8, 4, 2]
    # ])
    # def test_div(self, i, j, k):
    #     assert self.calc.div(i, j) == k
    # 数据驱动，数据与用例分离,使用到load_data方法,获取参数列表key且用逗号隔开
    @pytest.mark.parametrize(load_data()['keys'], load_data()['values'])
    def test_div(self, i, j, k):
        assert self.calc.div(i, j) == k

    # 异常值例子
    @pytest.mark.parametrize('a, b', [
        [2, 0],
        [0.2, 0],
        [0, 0]
    ])
    def test_div_error(self, a, b):
        with pytest.raises(Exception):
            assert self.calc.div(a, b)

    # 流程示例
    def test_process(self):
        r1 = self.calc.div(1, 2)
        r2 = self.calc.mul(2, 1)
        assert r1 == 2
        assert r2 == 2






'''
# 优化二：初始化考虑，使用到测试类
class TestCalc:
    # 平时推荐使用这个方法
    def setup_class(self):
        print("使用setup_class")
        self.calc = Calc()

    def setup(self):
        pass

    @pytest.mark.parametrize('a, b, c', [
        [1, 2, 2],
        [-1, -1, 1],
        [1, -1, 1]])
    def test_mul(self, a, b, c):
        assert self.calc.mul(a, b) == c

    @pytest.mark.parametrize('i, j, k', [
        [1, 0, 0],
        [0, 1, 0],
        [-1, 1, -1],
        [4, 2, 2],
        [-8, -2, 4],
        ["1", 1, 1]])
    def test_div(self, i, j, k):
        assert self.calc.div(i, j) == k

'''


'''
# 优化一：参数化，初始化的需要复用，共用一些变量放到外面，使用类比较方便，一个参数一行
@pytest.mark.parametrize('a, b, c', [
                        [1, 2, 2], 
                        [-1, -1, 1],
                         [1, -1, 1]])
def test_mul(a, b, c):
    calc = Calc()
    assert calc.mul(a, b) == c
    
'''

