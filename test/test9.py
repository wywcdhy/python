#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/18 14:24
# @Author  : wy
# @Site    :
# @File    : test9.py
from urllib.request import Request
from urllib.parse import urlencode
from urllib.request import urlopen
import ssl
import urllib
import zlib
from datetime import date

now = date.today()
print(now)
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
birthday = date(1964, 7, 31)
age = now - birthday
print(age.days)
s = b'witch which has which witches wrist watch'
print(len(s))
t = zlib.compress(s)
print(len(t))

# # 处理get请求，不传data，则为get请求
#
#
# url = 'https://sso.zjtcn.com/login.jsp'
# data = {"userName": "hezhenliang", "userPwd": "HE123456"}
# req_data = urlencode(data)  # 将字典类型的请求数据转变为url编码
# res = urlopen(url + '?' + req_data)  # 通过urlopen方法访问拼接好的url
# res = res.read().decode()  # read()方法是读取返回数据内容，decode是转换返回数据的bytes格式为str
#
# print(res)
# 处理post请求,如果传了data，则为post请求

# 如果网站的SSL证书是经过CA认证，就需要单独处理SSL证书，让程序忽略SSL证书验证错误，即可正常访问
context = ssl._create_unverified_context()  # 忽略安全
url = "https://www.baidu.com"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE"}

# url 作为Request()方法的参数，构造并返回一个Request对象
request = urllib.request.Request(url, headers=headers)

# Request对象作为urlopen()方法的参数，发送给服务器并接收响应
# 在urlopen()方法里 指明添加 context 参数
response = urllib.request.urlopen(request, context=context).read()
print(response.decode("utf-8"))
