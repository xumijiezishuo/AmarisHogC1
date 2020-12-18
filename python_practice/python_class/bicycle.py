# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2020/12/10 3:43 下午
# @Author :Amaris
# @File   :bicycle.py
"""
写一个Bicycle(自行车)类,有run(骑行)方法,
调用时显示骑行里程km(骑行里程为传入的数字):
再写一个电动自行车类EBicycle继承自Bicycle,
添加电池电量valume属性通过，参数传入, 同时有两个方法：
1. fill_charge(vol) 用来充电, vol 为电量
2. run(km) 方法用于骑行,每骑行10km消耗电量1度,
当电量消耗尽时调用Bicycle的run方法骑行，
通过传入的骑行里程数，显示骑行结果
"""
# 自行车类
class Bicycle:
    def run(self, km):
        print(f"一共用脚骑行了{km}公里，累死了")

# 电动自行车类
# 继承：把父类名称放在类名后面的小括号中
class Ebicycle(Bicycle):
    # 属性需要传参定义，可以直接放到构造函数中
    def __init__(self, valume):
        self.valume = valume

    # 充电方法
    def fill_charge(self, vol):
        # 充电后的电量 = 本身的电量 + 充电电量
        self.valume = self.valume + vol
        print(f"充了{vol}度电,现在的电量为{self.valume}度")

    # 骑行方法
    def run(self, km):
        # 获取目前电量所能电动骑行的最大里程数
        power_km = self.valume * 10
        print(f"目前电量所能电动骑行的最大里程数为：{power_km}")
        if power_km >= km:
            # 电量不够了，在电用完之后，还得用脚骑行
            print(f"我使用电瓶电量骑行了{km}公里")
        else:
            # 当电量消耗尽时调用Bicycle的run方法骑行
            print(f"我使用电瓶电量骑行了{power_km}公里")
            # 非继承调用
            # bike = Biycle()
            # bike.run(km - power_km)
            # 继承调用，用super()相当于实例化操作，可以去调用父类的方法和属性，不推荐多继承
            super().run(km-power_km)


# bike = Bicycle()
# bike.run(10)
ebike = Ebicycle(10)
ebike.fill_charge(3)
ebike.run(150)
