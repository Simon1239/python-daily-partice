# coding:utf-8

"""
eval()函数中必须是字符串数字
"""

# x = 3
# y = 5
# print(eval('''x*y'''))

# input()函数输出的是字符串
x = eval(input("输入第一个数："))
y = eval(input("输入第二个数："))
print(x**y)