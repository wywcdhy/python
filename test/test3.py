#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/8 13:41
# @Author  : wy
# @Site    : 冒泡排序
# @File    : test3.py
# 冒泡排序
data1 = [10, 4, 33, 21, 54, 8, 11, 5]
def sort(data):
    print(data)
    for i in range(len(data)-1):
        for j in range(len(data)-1-i):
            if data[j]>data[j+1]:
                data[j],data[j+1]=data[j+1],data[j]
        print('第{}次排序后：'.format(i+1))
        print(data)

def func(a:int=11,b:str='111'):
    print(a)
    print(b)

if __name__ == '__main__':
    sort(data1)
    func(122,'1111111')