# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2020/12/10 3:23 下午
# @Author :Amaris
# @File   :error.py

# 代码报错，看报错信息和报错代码行，错误信息可用翻译辅助理解，如果用pytest则主要看E后面的报错信息
def test_error():
    a = 1
    b = "bbbbb"

    print(a + b)

