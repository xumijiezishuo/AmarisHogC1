# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2020/12/22 12:47 上午
# @Author :Amaris
# @File   :test_appium2.py
'''
录播课2
'''
from appium import webdriver

desired_caps={
  "platformName": "android",
  "deviceName": "emulator-5554",
  "appPackage": "com.xueqiu.android",
  "appActivity": ".view.WelcomeActivityAlias",
    "noReset": True
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)

el2 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
el2.click()
el3 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el3.send_keys("alibaba")
el4 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView[1]")
el4.click()
