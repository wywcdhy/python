#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/8 15:40
# @Author  : wy
# @Site    : 
# @File    : test4.py
import sys
if __name__ == '__main__':

    f = open('yesterday.txt', 'r', encoding='utf-8')
    f2 = open('yesterday_bak.txt', 'w', encoding='utf-8')

    find_str = sys.argv[1]
    replace_str = sys.argv[2]
    for line in f:
        if find_str in line:
            line = line.replace(find_str, replace_str)
        f2.write(line)
    f.close()
    f2.close()