# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2020/12/10 3:43 下午
# @Author :Amaris
# @File   :game_oop.py

class Game:
    def __init__(self, my_hp, enemy_hp):
        self.my_hp = my_hp
        self.my_power = 200
        self.enemy_hp = enemy_hp
        self.enemy_power = 199

    def figit(self):
        # 加入循环，让游戏可以进行多轮
        while True:
            # 定义最终血量计算方式
            self.my_hp = self.my_hp - self.enemy_power
            self.enemy_hp = self.enemy_hp - self.my_power

            # print(f"我的剩余血量为{self.my_hp}")
            # print(f"敌人的剩余血量为{self.enemy_hp}")

            # 判断谁的血量小于等于0
            if self.my_hp <= 0:
                # 打印我和敌人的剩余血量
                print(f"我的剩余血量为{self.my_hp}")
                print(f"敌人的剩余血量为{self.enemy_hp}")
                print("我输了")
                # 满足条件跳出循环
                break
            elif self.enemy_hp <= 0:
                print(f"我的剩余血量为{self.my_hp}")
                print(f"敌人的剩余血量为{self.enemy_hp}")
                print("我赢了")
                # 满足条件跳出循环
                break

    def rest(self, time_num):
        print(f"太累了，休息{time_num}分钟")

game = Game(1000, 200)
game.rest(10)
print(game.enemy_hp)