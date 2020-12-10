# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2020/12/10 2:16 下午
# @Author :Amaris
# @File   :game_round_fun.py

# 快捷键：command（ctrl）+d即复制选中的行或者直接复制当前行
# 快捷键：command（ctrl）+/即注释选中的行或者直接注释当前行，可以再次操作取消注释
# 快捷键：option（alt）+enter即导包快捷键


"""
一个回合制游戏，每个角色都有hp 和power，hp代表血量，power代表攻击力，
hp的初始值为1000，power的初始值为200。
定义一个fight方法：
my_final_hp = my_hp - enemy_power
enemy_final_hp = enemy_hp - my_power
两个hp进行对比，血量剩余多的人获胜
"""

# 定义fight函数实现游戏逻辑
import random


def fight(enemy_hp, enemy_power):
    # 定义4个变量存放数据
    my_hp = 1000
    my_power = 200

    # 打印敌人的血量和攻击力
    print(f"敌人的血量为{enemy_hp}，敌人的攻击力为{enemy_power}")

    # 加入循环，让游戏可以进行多轮
    while True:
        # 定义最终血量计算方式
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power

        print(f"我的剩余血量为{my_hp}")
        print(f"敌人的剩余血量为{enemy_hp}")

        # 判断谁的血量小于等于0
        if my_hp <= 0:
            # 打印我和敌人的剩余血量
            print(f"我的剩余血量为{my_hp}")
            print(f"敌人的剩余血量为{enemy_hp}")
            print("我输了")
            # 满足条件跳出循环
            break
        elif enemy_hp <= 0:
            print(f"我的剩余血量为{my_hp}")
            print(f"敌人的剩余血量为{enemy_hp}")
            print("我赢了")
            # 满足条件跳出循环
            break



# if __name__ == "__main__":表示当在当前文件运行时就运行它，如果当前文件被用于导包时就不运行它。
if __name__ == "__main__":
    # 利用列表推导式生成hp
    hp = [x for x in range(990, 1010)]
    # print(hp)
    # print(type(hp))
    #让敌人的hp从hp列表中随机挑选一个值
    enemy_hp = random.choice(hp)
    # print(enemy_hp)

    # 敌人的攻击力用randint方法生成随机整数
    enemy_power = random.randint(190, 210)
    # print(enemy_power)

    # 调用函数，传入敌人的hp和power
    fight(enemy_hp, enemy_power)





