#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/8 16:56
# @Author  : wy
# @Site    : 
# @File    : test6.py
def check_str_len(s: str, l: int):
    '''
    检查字符串长度
    :param s:
    :param l:
    :return:符合条件返回True,否则返回False
    '''
    if len(s) == l and s.isdecimal():
        return True
    else:
        return False


def login(userinfo):
    a=0
    while a<1:
        print('1-登录  2-注册  3-退出'.center(30,'*'))
        choice = input()
        if choice == '1':
            account = input('账号:')
            passwd = input('密码:')
            if account in userinfo:
                if userinfo[account][0] ==passwd:
                    print('登录成功')
                else:
                    print('密码错误')
            else:
                print('账号不存在')
        elif choice =='2':
            account = input('账号:')
            passwd = input('密码:')
            name = input('姓名:')
            phone = input('手机号:')
            if account in userinfo:
                print('账号已经存在')
            else:
                if check_str_len(passwd,6):
                    if check_str_len(phone,11):
                        userinfo[account]=[passwd,name,phone]
                        print('注册成功')
                        print(userinfo)
                    else:
                        print('手机号不合法')
                else:
                    print('密码不合法')
        elif choice == '3':
            a=1
            break
        else:
            print('选择错误')

if __name__ == '__main__':
    userinfo = {'user1': ['123456', '张三', '13471350511'], 'user2': ['123456', '李四', '13471350512']}
    login(userinfo)