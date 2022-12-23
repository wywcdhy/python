#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/8 11:27
# @Author  : wy
# @Site    : 猜数游戏
# @File    : test2.py
import random

if __name__ == '__main__':
    nub = random.randint(1, 101)
    n = 1
    while n > 0:
        print(nub)
        guess_nu = int(input("输入你猜的数值:"))
        if guess_nu > nub:
            print("你输入的数值大于要猜的数")
        elif guess_nu < nub:
            print("你输入的数值小于要猜的数")
        else:
            print("恭喜你猜对了")
            choose = input('是否继续游戏？（是y）：')
            if choose.lower() != 'y':
                n = 0
                break
            else:
                nub = random.randint(1, 101)
