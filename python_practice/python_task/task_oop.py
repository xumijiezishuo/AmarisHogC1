# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2020/12/14 11:37 上午
# @Author :Amaris
# @File   :task_oop.py
'''
作业1
用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个。
'''
class Animal:
    colour = "black"
    weight = 1

    def run(self):
        print("动物可以跑")
    def eat(self):
        print("动物可以吃")

chiken = Animal()

chiken.run()
chiken.colour = "red"

print(f"鸡是一种动物，颜色为{chiken.colour}")

class Peole:
    sex = "男"
    age = 20

    def walk(self):
        print("可以走路")
    def cook(self):
        print("可以烹饪")
    def speak(self):
        print("可以谈话")


print(Peole.sex)

class Computer:
    size = "15寸"
    weight = 2

    def playmovie(self):
        print("播放视频")

    def read(self):
        print("阅览网页")

mac = Computer()

mac.size = "14寸"
print(mac.size)
print(Computer.size)

class Clothes:
    size = "s"
    colour = "red"

    def wear(self):
        print("衣服可以穿")

    def wash(self):
        print("衣服可以洗")


jacket = Clothes()
jacket.wear()

class Package:
    size = "s"
    colour = "red"

    def storage(self, kg):
        print(f"包可以存放{kg}kg的东西")


knapsack = Package()
knapsack.storage(10)
