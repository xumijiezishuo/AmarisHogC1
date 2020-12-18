# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2020/12/14 11:35 上午
# @Author :Amaris
# @File   :xuzhu.py
'''
定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
加入模块化改造:即每个类放到单独的文件中，一个文件最好只有一个类，可以进行引用
'''
from python_practice.python_task.tonglao import TongLao


class XuZhu(TongLao):
    def read(self):
        print("罪过罪过")
