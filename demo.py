#! /usr/bin/env python
# -*- coding:utf-8 -*-

# 编辑器：pychram
# 解释器版本：python3.6.5
# 需要使用到的第三方库：uiautomator2、adb、安卓模拟器、京东app

import time
import uiautomator2 as u2
"""
	在手机或者模拟器安装好的情况下，并且手机安装了京东app且京东app出现在屏幕上。运行代码即可自动点击京东app。
"""

fmt = "%Y-%m-%d %H:%M:%S"

# d 控制器
d = u2.connect("127.0.0.1:7555")

# d(text="网易云音乐").click()
fmt = "%Y-%m-%d %H:%M:%S"

# 准时抢单 10：00
time_target = time.strptime("2018-11-11 22:00:00", fmt)

print("两钟之后秒点击京东：")
time.sleep(2)
print("点击京东")
d(text="京东").click()

print("等待购物车栏目出现")
if d(resourceId="com.jingdong.app.mall:id/bo7", className="android.widget.ImageView", instance=3).wait(10):
    print("点击购物车")
    d(resourceId="com.jingdong.app.mall:id/bo7", className="android.widget.ImageView", instance=3).click()

# 点击去结算
print("现在的时间是：" + time.strftime(fmt, time.localtime()) + "两秒钟之后点击去结算：")
now_time = time.localtime()
diff = (time_target.tm_hour - now_time.tm_hour ) * 60 * 60 + (time_target.tm_min - now_time.tm_min) * 60 + time_target.tm_min - now_time.tm_sec

# print(diff)
time.sleep(2)
print("点击去结算:(现在时间是)" + time.strftime(fmt, time.localtime()))
d(resourceId="com.jd.lib.cart:id/cart_settle_accounts_but").click()

print("提交订单我们就不点了！")
# 点击付款
# d(resourceId="com.jd.lib.settlement:id/settle_view_money").click()


