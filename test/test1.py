#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/8 10:27
# @Author  : wy
# @Site    : 
# @File    : test1.py

# 实现1-100奇数求和，至少3种方式。
if __name__ == '__main__':
    s = 0
    for i in range(1, 101):
        if i % 2 != 0:
            s += i
    print(s)
    print(sum([i for i in range(1, 101) if i % 2 != 0]))
    print()
    # 姿势二：filter+lambda 生成列表,然后求和列表里的值
    print(sum(list(filter(lambda x: x % 2 == 1, range(1, 101)))))
    print('-----------------------------')
    print(sum(filter(lambda i: i % 2 == 1, range(1, 101))))
    print('-----------------------------')

    # 姿势三：if
    print(sum([x for x in range(1, 101) if x % 2 == 1]))

    # 姿势四：reduce迭代方法 x+y
    import functools
    print(functools.reduce(lambda x, y: x+y, range(1, 101, 2)))

    # 姿势五：so easy 等差数列
    print(sum(range(1, 101, 2)))


    for i in range(5):
        print(i)