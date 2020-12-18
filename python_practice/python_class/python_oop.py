# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2020/12/10 3:43 下午
# @Author :Amaris
# @File   :python_oop.py

# 创建类（图纸设计）-创建类的实例（建样板房子）-实现功能（用途）
# 不写构造函数时，会隐形自动创建。无论构造方法还是实例方法至少有一个参数，可以是self也可以是其他参数
# self表示类对象本身,类对象只能调用自己本身的类变量和类方法

# 面向对象 类、类属性、类方法
class House:
    # 静态属性->类变量（类之中，方法之外）
    door = "red"
    floor = "white"

    # 构造函数，在类实例化的时候直接执行,所实例化2个对象就执行了2次构造方法即执行了2次 print(self.door)
    def __init__(self):
        # 在方法当中调用类变量需要加上self
        print(f"构造方法中调用类变量door:{self.door}")
        # 实例变量，类当中，方法当中，以"self.变量名"方法去定义
        self.kitchen = "cook"



    # 动态方法
    def sleep(self):
        # 普通变量：在类当中，方法当中，前面没有self
        bed = "席梦思"
        # 定义实力例变量
        self.table = "桌子可以放东西"
        print(f"在房子里可以躺在{bed}床上睡觉")

    def cook(self):
        # 调用实例变量
        print(f"动态方法中调用在构造方法定义的实例变量kitchen：{self.kitchen}")
        print(f"动态方法中调用在动态方法定义的实例变量table：{self.table}")
        print("在房子里可以做饭吃")



# 把类实例化 类实例化生成对象
# 北欧风房子
north_house = House()
# 中式风房子
china_house = House()

# 调用类属性
# 类名调用类属性
# print(House.door)
# 类名修改类属性
# print(f"修改前的House.door是：{House.door}")
House.door = "white"

# print(f"修改后的House.door是：{House.door}")

# 实例对象调用类属性
# print(f"修改前的House.door是：{House.door}")
# print(f"修改前的north_house.door是：{north_house.door}")
# print(f"修改前的china_house.door是：{china_house.door}")
# 修改对象属性，作用域仅为当前对象
north_house.door = "black"

# print(f"修改后的House.door是：{House.door}")
# print(f"修改后的north_house.door是：{north_house.door}")
# print(f"修改后的china_house.door是：{china_house.door}")

# 实力对象调用方法中的实例变量
# print(north_house.kitchen)
# print(china_house.kitchen)

# 没有调sleep方法时，直接调用table属性会报错，因为那时table还没有被声明
north_house.sleep()
print(north_house.table)


# north_house.sleep()
# north_house.cook()







