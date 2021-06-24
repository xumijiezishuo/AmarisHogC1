# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2021/6/23 4:11 下午
# @Author :Amaris
# @File   :test_appium_luzhi.py

# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
# 需要安装appium-python-client客户端
from appium import webdriver

caps = {}
caps["platformName"] = "Android"
caps["deviceName"] = "qiyeweixin"
caps["appPackage"] = "com.tencent.wework"
caps["appActivity"] = ".launch.LaunchSplashActivity"
caps["noReset"] = "True"

# 与server建立连接，固定写法，IP可根据实际配置，实际上是创建了一个session
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(10)

el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.TextView")
el1.click()
el2 = driver.find_element_by_id("com.tencent.wework:id/hci")
el2.click()
el3 = driver.find_element_by_id("com.tencent.wework:id/g5f")
el3.click()
el3.send_keys("测试")

driver.quit()