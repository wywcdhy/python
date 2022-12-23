#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/16 9:30
# @Author  : wy
# @Site    : 
# @File    : test7.py
if __name__ == '__main__':
   fo = open("runoob.txt", "r", encoding='UTF-8')
   print("文件名为: ", fo.name)

   fo.flush()
   index = 1
   for line_2 in fo.readlines():
       print("第 %d 行 - %s" % (index, line_2))
       index +=1


   print(fo.tell())

   # fo.read(10) 会读取文件中的换行符,换行符也算一个字节
   line = fo.read(10)
   print("读取的字符串: %s" % (line))
   line = fo.readline()
   print("读取第一行 %s" % (line))

   line = fo.readline(5)
   print("读取的字符串为: %s" % (line))
   # 关闭文件
   fo.close()
