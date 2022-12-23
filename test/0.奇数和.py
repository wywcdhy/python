#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/3 22:34
# @公众号  : 全栈测试笔记
# @Blog    : http://www.cnblogs.com/UncleYong
# @Gitee   : https://gitee.com/UncleYong
# @QQ交流群 : 652122175


# 实现1-100奇数求和，至少3种方式。

# 姿势一：循环
total = 0
for i in range(1, 101):
    if i%2!=0:
        total = total + i
print(total)

# 姿势二：filter+lambda
print(sum(list(filter(lambda x: x%2==1, range(1, 101)))))

# 姿势三：if
print(sum([x for x in range(1, 101) if x%2==1]))

# 姿势四：reduce
import functools
print(functools.reduce(lambda x,y:x+y, range(1,101,2)))

# 姿势五：so easy
print(sum(range(1, 101, 2)))