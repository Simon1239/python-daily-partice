# coding:utf-8

import math

action = math.pow((1+0.01),365)
inaction = math.pow((1-0.01),365)

print(f"学习积累后：{action:.2f},消极倦怠后：{inaction:.2f}")

action = math.pow((1+0.01),3)
inaction = math.pow((1-0.01),2)
result = math.pow((action*inaction),(365/5))

print(f"一年后知识储备变为：{result:.2f}")