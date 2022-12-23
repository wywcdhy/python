#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/8 15:51
# @Author  : wy
# @Site    : 
# @File    : test5.py
if __name__ == '__main__':

    infoFile = 'E:/userinfo.txt'  # \\或者/

    i = 0
    for i in range(3):
        flag = True
        username = input('please inupt username:').strip()
        passwd = input('please inupt passwd:')
        confirm_passwd = input('please inupt confirm_passwd:')
        with open(infoFile, 'r') as f:
            # f.seek(0)
            for line in f.readlines():
                user, pwd = line.strip().split(',')
                if user == username:
                    print('username is already exist.')
                    i += 1
                    flag = False
                    break
        if flag == True:
            if passwd != confirm_passwd:
                print('passwd is unequall.')
                i += 1
            else:
                print('register success.')
                with open(infoFile, 'a') as f2:
                    f2.write('\n' + username + ',' + passwd)
                break
    else:
        print('over, try next day.')