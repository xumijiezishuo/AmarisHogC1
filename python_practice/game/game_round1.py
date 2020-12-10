# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2020/12/10 2:16 下午
# @Author :Amaris
# @File   :game_round1.py

# 快捷键：command+d即复制选中的行或者直接复制当前行
# 快捷键：command+/即注释选中的行或者直接注释当前行，可以再次操作取消注释

"""
一个回合制游戏，每个角色都有hp 和power，hp代表血量，power代表攻击力，
hp的初始值为1000，power的初始值为200。
定义一个fight方法：
my_final_hp = my_hp - enemy_power
enemy_final_hp = enemy_hp - my_power
两个hp进行对比，血量剩余多的人获胜
"""

# 定义fight函数实现游戏逻辑
def fight():
    # 定义4个变量存放数据
    my_hp = 1000
    my_power = 200
    enemy_hp = 1000
    enemy_power = 200

    # 定义最终血量计算方式
    my_final_hp = my_hp - enemy_power
    enemy_final_hp = enemy_hp - my_power

    # 判断输赢
    # if my_final_hp > enemy_final_hp:
    #     print("我赢了")
    # elif my_final_hp == enemy_final_hp:
    #     print("平局")
    # else:
    #     print("我输了")

    # 三目运算等同于下面的if-else,只是语法简洁一些
    print("我赢了") if my_final_hp > enemy_final_hp else print("我输了")


fight()




