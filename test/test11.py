#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/18 17:00
# @Author  : wy
# @Site    :
# @File    : test10.py
import calendar
import cmath

# 整数的阶乘（英语：factorial）是所有小于及等于该数的正整数的积，0的阶乘为1。即：n!=1×2×3×...×n。
import random
from math import sqrt


def chen_jie(num):
    if num < 0:
        print("小于0的数没有乘阶")
    elif num == 0:
        print("0 的阶乘为 1")
    else:
        sum = 1
        for i in range(1, num + 1):
            sum = sum * i
        print("%d 的阶乘为 %d" % (num, sum))


# 斐波那契数列指的是这样一个数列 0, 1, 1, 2, 3, 5, 8, 13,特别指出：第0项是0，第1项是第一个1。从第三项开始，每一项都等于前两项之和
def fei_bo(num):
    sum = 0
    a = 0
    b = 1
    if num <= 0:
        print("请输入一个正整数。")
    elif num == 1:
        print("斐波那契数列：")
        print(0)
    else:
        print(a, ",", b)
        for i in range(2, num):
            sum = a + b
            a = b
            b = sum
            print(sum, end=" , ")


# 平方根
def ping_fang_gen(num):
    num_sqrt = num ** 0.5
    print('\n %0.3f 的平方根为 %0.3f' % (num, num_sqrt))


# 计算实数和复数平方根
# 导入复数数学模块
def fu_shu_pfg(num):
    num_sqrt = cmath.sqrt(num)
    print('{0} 的平方根为 {1:0.3f}+{2:0.3f}j'.format(num, num_sqrt.real, num_sqrt.imag))


# 三角形面积
def san_jiao_xing_area(a, b, c):
    if a + b <= c:
        print("请输入正常的三角形边长")
    elif a + c <= b:
        print("请输入正常的三角形边长")
    elif b + c <= a:
        print("请输入正常的三角形边长")
    else:
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print('三角形面积为 %0.2f' % area)


# 圆的面积
def yuan_area(r):
    s = 3.142 * (r ** 2)
    print('圆的面积为 %0.6f' % s)


# 猜数(1~100)
def cai_shu(num):
    print('随机生成一个1~100的随机整数')
    a = random.randint(1, 100)
    print(a)
    while num != a:
        if num > a:
            print('输入的数大于生成的数')
        elif num < a:
            print('输入的数小于生成的数')
        num = int(input('请重新输入\n'))
    print('恭喜你猜对了,生成的数是', a)


# 计算华氏温度
def change_celsius(celsius):
    fahrenheit = (celsius * 1.8) + 32
    print('%0.1f 摄氏温度转为华氏温度为 %0.1f ' % (celsius, fahrenheit))


# 交换变量
"""
>>>"{} {}".format("hello", "world")    # 不设置指定位置，按默认顺序
'hello world'
 
>>> "{0} {1}".format("hello", "world")  # 设置指定位置
'hello world'
 
>>> "{1} {0} {1}".format("hello", "world")  # 设置指定位置
'world hello world'
"""


def change_bl(x, y):
    x, y = y, x
    print('交换后 x 的值为: {}'.format(x))
    print('交换后 y 的值为: {}'.format(y))


# 判断字符串是否为数字
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        # 把一个表示数字的字符转换为浮点数返回的函数
        # char转成float
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


# 判断奇数偶数
def is_ji_ou(num):
    if num % 2 == 0:
        print('{}是偶数'.format(num))
    else:
        print('{}是奇数'.format(num))
    print('{}是偶数'.format(num) if num % 2 == 0 else '{}是奇数'.format(num))


# 判断闰年
def is_run_nian(num):
    print('闰年' if (num % 4 == 0 and num % 100 != 0) or num % 400 == 0 else '平年')
    print('闰年' if calendar.isleap(num) else '平年')


# 质数判断
def is_zhi_shu(num):
    if num > 1:
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                print(num, "是合数")
                break
        else:
            print(num, "是质数")
    else:
        print(num, "既不是质数，也不是合数")


# 素数判断
def is_su_shu(lower, upper):
    print(end=" ")


if __name__ == '__main__':
    chen_jie(100)
    fei_bo(10)
    ping_fang_gen(99)
    fu_shu_pfg(-100)
    san_jiao_xing_area(3, 3, 1)
    yuan_area(3)
    # num = int(input('输入一个数字：\n'))
    # cai_shu(num)
    change_celsius(100)
    change_bl(1, 2)
    is_ji_ou(322)
    is_run_nian(1000)
    is_zhi_shu(88)
