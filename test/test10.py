#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/18 17:00
# @Author  : wy
# @Site    :
# @File    : test10.py


# 通过用户输入三角形三边长度，并计算三角形的面积
import calendar
import datetime
import re
import time
from functools import reduce
from tkinter import _flatten


def sun_san_jiao_xing():
    a = float(input('输入三角形的第一条边长:'))
    b = float(input('输入三角形的第二条边长:'))
    c = float(input('输入三角形的第三条边长:'))
    if a + b > c and a + c > b and b + c > a:
        print('输入边长可以构成三角形')
        # 计算周长
        s = a + b + c
        print('三角形周长为 %0.2f' % s)

        # 计算面积
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print('三角形面积为 %0.2f' % area)
    else:
        print('输入边长不能构成三角形')


# 圆的面积公式为
def find_yuan_Area(r):
    PI = 3.1415
    print(PI * r ** 2)


# 将摄氏温度转华氏温度
def change_celsius(celsius):
    fahrenheit = (celsius * 1.8) + 32
    print('%0.2f 摄氏温度转为华氏度的温度为 %0.f' % (celsius, fahrenheit))


# x和y变量交换


def change_x_y(x, y):
    temp = x
    x = y
    y = temp
    print('交换后 x 的值为: {}'.format(x))
    print('交换后 y 的值为: {}'.format(y))


#  is_number() 方法来判断字符串是否为数字


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


# 判断奇偶数


def change_jioushu(i):
    if i % 2 == 0:
        print("{0} 是偶数".format(i))
    else:
        print("{0} 是奇数".format(i))


# 判断是否是闰年
# 闰年的判断规则如下：
# （1）若某个年份能被4整除但不能被100整除，则是闰年。
# （2）若某个年份能被400整除，则也是闰年。


def change_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("{0} 是闰年".format(year))
    else:
        print("{0} 不是是闰年".format(year))


# 判断最大的数


def max_num(list):
    print(max(list))


# 判断是否是质数


def zhi_shu(num):
    for n in range(1, num + 1):
        if n > 1:
            for i in range(2, n // 2):
                if (n % i) == 0:
                    print(i, "乘以", n // i, "=", n, "不是质数")
                    break
            else:
                print(n)


def change_list():
    list1 = ['["aa","bb","cc","dd"]', '["aa","bb","cc","dd"]']
    n2 = str(list1)
    print(n2)
    str1 = n2.replace(
        "[",
        '').replace(
        "]",
        '').replace(
        "\"",
        '').replace(
        " ",
        '').replace(
        "\'",
        '')
    print(str1)
    str2 = str1.split(',')
    print(str2)


# 整数的阶乘（英语：factorial）是所有小于及等于该数的正整数的积，0的阶乘为1。即：n!=1×2×3×...×n


def zheng_shu_factorial(num):
    if num < 0:
        print("抱歉，负数没有阶乘")
    elif num == 0:
        print("0 的阶乘为 1")
    else:
        for i in (1, num + 1):
            factorial = factorial * i
        print("%d 的阶乘为 %d" % (num, factorial))


# 乘法表


def cheng_fa_biao(num):
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            print('{}x{}={}\t'.format(j, i, i * j), end='')
        print()


# 斐波那契数列指的是这样一个数列 0, 1, 1, 2, 3, 5, 8, 13


def nterms(num):
    print('输出长度为 %d 的斐波那契数列' % num)
    n1 = 0
    n2 = 1
    index = 2
    if num == 1:
        print(n1)
    elif num == 2:
        print(n2)
    else:
        print(n1, ",", n2, end=" , ")
        while index < num:
            s = n1 + n2
            if index + 1 == num:
                print(s)
            else:
                print(s, end=" , ")
            n1 = n2
            n2 = s
            index += 1


# 阿姆斯特朗数


def amslts(nub):
    for num in range(1, nub + 1):
        sum = 0
        n = len(str(num))
        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** n
            temp //= 10

        if num == sum:
            print(num)


# 十进制数转化成其他进制


def change_dec(nub):
    print("十进制数为：", nub)
    print("转换为二进制为：", bin(nub))
    print("转换为八进制为：", oct(nub))
    print("转换为十六进制为：", hex(nub))


# ASCII码转换


def change_ACCII(ch, nub: int):
    print(ch + "的ASCII码为", ord(ch))
    print(nub, "对应的字符为", chr(nub))


# 最大公约数
def hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if (x % i == 0) and (y % i == 0):
            hcf = i

    print(hcf)


# 最小公倍数


def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while (True):
        if greater % x == 0 and greater % y == 0:
            print(x, "和", y, "的最小公倍数为", greater)
            break
        else:
            greater += 1


# 生成日历


def date_rl(yy, mm):
    print(calendar.month(yy, mm))


# 递归的方式来生成斐波那契数列
def recur_fibo(n):
    """递归函数
    输出斐波那契数列"""
    if n <= 1:
        return n
    else:
        return (recur_fibo(n - 1) + recur_fibo(n - 2))


# 写入文件
def write_file_txt():
    with open("test.txt", "wt") as out_file:
        out_file.write("该文本会写入到文件中\n看到我了吧！")

    # Read a file
    with open("test.txt", "rt") as in_file:
        text = in_file.read()

    print(text)


# 判断字符串
def sudo_str(str):
    print("判断所有字符都是数字或者字母", str.isalnum())
    print("判断所有字符都是字母", str.isalpha())
    print("判断所有字符都是数字", str.isdigit())
    print("判断所有字符都是小写", str.islower())
    print("判断所有字符都是大写", str.isupper())  # 判断所有字符都是大写
    print("判断所有单词都是首字母大写，像标题", str.istitle())  # 判断所有单词都是首字母大写，像标题
    print("判断所有字符都是空白字符、\t、\n、\r", str.isspace())  # 判断所有字符都是空白字符、\t、\n、\r

# 大小字符串转化


def change_str(str):
    print(str.upper())  # 把所有字符中的小写字母转换成大写字母
    print(str.lower())  # 把所有字符中的大写字母转换成小写字母
    print(str.capitalize())  # 把第一个字母转化为大写字母，其余小写
    print(str.title())  # 把每个单词的第一个字母转化为大写，其余小写

# 查询每个月的天数,并且输出当月第一天是星期几0~6


def calendar_month_days(year, month):
    monthRange = calendar.monthrange(year, month)
    print(monthRange)
    # 输出每个月的天数
    print(calendar.mdays)

# 查询昨天的日期


def getYesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    print(yesterday)


# 约瑟夫生者死者小游戏
def ysf():
    people = {}
    for x in range(1, 31):
        people[x] = 1
    check = 0
    i = 1
    j = 0
    while i <= 31:
        if i == 31:
            i = 1
        elif j == 15:
            break
        else:
            if people[i] == 0:
                i += 1
                continue
            else:
                check += 1
                if check == 9:
                    people[i] = 0
                    check = 0
                    print("{}号下船了".format(i))
                    j += 1
                else:
                    i += 1
                    continue


def bu_yu():
    fish = 1
    while True:
        total, enough = fish, True
        for _ in range(5):
            if (total - 1) % 5 == 0:
                total = (total - 1) // 5 * 4
            else:
                enough = False
                break
        if enough:
            print(f'总共有{fish}条鱼')
            break
        fish += 1


def miao_biao():
    print('按下回车开始计时，按下 Ctrl + C 停止计时。')
    while True:

        input("")  # 如果是 python 2.x 版本请使用 raw_input()
        starttime = time.time()
        print('开始')
        try:
            while True:
                print('计时: ', round(time.time() - starttime, 0), '秒', end="\r")
                time.sleep(1)
        except KeyboardInterrupt:
            print('结束')
            endtime = time.time()
            print('总共的时间为:', round(endtime - starttime, 2), 'secs')
            break


# 定义立方和的函数
def sumOfSeries(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i ** 3

    print(sum)

# 求数组元素的和


def sum_list(list):
    print(reduce(lambda x, y: x + y, list))


# 列表倒叙
def Reverse(lst):
    print([ele for ele in reversed(lst)])
    lst.reverse()
    print(lst)
    print(lst[::-1])

# 判定数字字符是否在列表中


def list_set(str, list):
    if str in list:
        print("存在")
    else:
        print('不存在')

# 判断列表中元素个数


def countX(list, x):
    print(list.count(x))

# 定义一个数字列表，并计算列表元素之和


def sumOfList(list):
    total = 0
    ele = 0
    for ele in range(0, len(list)):
        total = total + list[ele]
    print("列表元素之和为: ", total)

    while (ele < len(list)):
        total = total + list[ele]
        ele += 1
    print("列表元素之和为: ", total)
    total = sumOfList1(list, len(list))
    print("列表元素之和为: ", total)


def sumOfList1(list, size):
    if (size == 0):
        return 0
    else:
        return list[size - 1] + sumOfList1(list, size - 1)

#  移除字符串中的指定位置字符


def remove_str(str, index):
    # 输出原始字符串
    print("原始字符串为 : " + str)
    s = len(str)
    new_str = ""
    if s < index:
        print('请输入正确的字符位置,目前字符长度为:', s)

    else:
        new_str = ""
        for i in range(0, s):
            if i != index:
                new_str = new_str + str[i]

        print("字符串移除后为 : ", new_str)
        print("字符串移除后为 : ", (str[:index] + str[index + 1:]))
# 判断字符串是否存在子字符串


def check_str(string, sub_str):
    if sub_str in string:
        print('存在')
    else:
        print('不存在')
# 正则匹配url


def Find(string):
    # findall() 查找匹配正则表达式的字符串
    url = re.findall('https?://(?:[-\\w.]|(?:%[\\da-fA-F]{2}))+', string)

    print(url)

# 字符串翻转


def reversed_str(str):
    print(str[::-1])
    print(''.join(reversed(str)))
    print(reduce(lambda x, y: y + x, str))

# 对字符串切片及翻转


def rotate(input, d):
    Lfirst = input[0: d]
    Lsecond = input[d:]
    Rfirst = input[0: len(input) - d]
    Rsecond = input[len(input) - d:]
    y = input[:d:-1]
    print(y)
    print("头部切片翻转 : ", (Lsecond + Lfirst))
    print("尾部切片翻转 : ", (Rsecond + Rfirst))

# 按键(key)或值(value)对字典进行排序


def dictionary(key_value):
    print("按键(key)排序:")
    for i in sorted(key_value):
        print((i, key_value[i]), end=" ")
    print("按值(value)排序:")
    print(sorted(key_value.items(), key=lambda kv: (kv[1], kv[0])))

# 移除字典点键值(key/value)对


def remove_dictionary(dict, key):
    # 输出原始的字典
    print("字典移除前 : " + str(dict))

    # 使用 del 移除 Zhihu
    del dict[key]

    # 输出移除后的字典
    print("字典移除后 : " + str(dict))
    # 使用 pop() 移除没有的 key 不会发生异常，我们可以自定义提示信息
    removed_value = dict.pop('Baidu', '没有该键(key)')

# 合并字典


def Merge(dict1, dict2):
    print(dict2.update(dict1))


def Merge_1(dict1, dict2):
    res = {**dict1, **dict2}
    print(res)


if __name__ == '__main__':
    # sun_san_jiao_xing()
    # find_yuan_Area(1)
    # list = (1, 2, 3, 45, 65, 67)
    # print(max(list))
    # amslts(5000)
    # zhi_shu(91)
    # change_list()
    # change_dec(1001)
    # change_ACCII('a', 13)
    # lcm(45, 100)
    # date_rl(1950, 6)
    # sudo_str("1ssdsdd")
    # calendar_month_days(2021,8)
    # getYesterday()
    # ysf()
    # bu_yu()
    # miao_biao()
    # sumOfSeries(8)
    list = [1, 3, 11, 7, 9, 34]
    print(reduce(lambda x, y: x * y, list))
    Reverse(list)
    countX(list, 9)
    sumOfList(list)
    remove_str("12321dweqe", 5)
    check_str('1232dddaaswe', '232d')
    string = 'hyl ekil ylemertxe ma i'
    # Find(string)
    # reversed_str(string)
    # print(reduce(lambda x, y: x + y, list))
    rotate(string, 2)
    key_value = {2: 56, 1: 2, 5: 12, 4: 24, 6: 18, 3: 323}
    dictionary(key_value)
    lis = [{"name": "Taobao", "age": 100},
           {"name": "Runoob", "age": 7},
           {"name": "Google", "age": 100},
           {"name": "Wiki", "age": 200}]
