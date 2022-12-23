#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/22 17:27
# @Author  : wy
# @Site    :
# @File    : read_file.py
from openpyxl import load_workbook


import pandas

if __name__ == '__main__':
    file_path = 'C:\\Users\\Administrator\\esktop\\d.xlsx'
    xls = pandas.ExcelFile(file_path)
    sheet_names = xls.sheet_names
    print(sheet_names)
