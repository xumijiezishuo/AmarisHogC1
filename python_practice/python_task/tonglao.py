# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2020/12/14 11:03 上午
# @Author :Amaris
# @File   :tonglao.py
'''
作业2
定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，

see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“师弟是我的！”，如果传入“丁春秋”，打印“叛徒！我杀了你”

fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。

定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
加入模块化改造
'''
class TongLao():

    # 需要传入的参数，使用构造函数
    def __init__(self, tl_hp, tl_power):
        self.tl_hp = tl_hp
        self.tl_power = tl_power

    def see_people(self, name):
        if name == "WYZ":
            print("师弟！！！!!")
        elif name == "李秋水":
            print("师弟是我的！")
        elif name == "丁春秋":
            print("叛徒，我杀了你")

    def fight_zms(self, enmy_hp, enmy_power):
        self.tl_hp = self.tl_hp/2
        self.tl_power = self.tl_power*10

        tl_hp_final = self.tl_hp-enmy_power
        enmy_hp_final = enmy_hp-self.tl_power

        if tl_hp_final > enmy_hp_final:
            print("我赢了")
        elif tl_hp_final < enmy_hp_final:
            print("我输了")
        elif tl_hp_final == enmy_hp_final:
            print("平局")





tonglao = TongLao(100, 10)
tonglao.fight_zms(200, 10)


