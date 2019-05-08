#!/usr/bin/python
# -*- coding: <encoding name> -*-
import numpy as np
import pandas as pd
import os
import xlrd
import xlwt
import openpyxl
import xlsxwriter
import xlwings as xw
from string import digits
import re
print('郭睿')

# a = 1
# b = 1
# book = openpyxl.Workbook()
# sheet = book._add_sheet('case1')
# sheet.write(a+2, b+5, 5)
# book.save('D:/demo1.xlsx')

# app = xw.App(visible=True, add_book=False)
# wb = app.books.add()
# wb = app.books.open()
# wb.save('D:/EN.xlsx')
# wb.sheets['sheet1'].range(2, 2).value = '222'
# wb.sheets['sheet1'].range(3, 2).value = '222'
# wb.sheets['sheet1'].range(4, 2).value = '222'
# wb.sheets['sheet1'].range(5, 2).value = '222'
# wb.save()
# wb.close()
# # app.quit()
# a = ['3\n1', 'lxy my l', 'lxy my d']
# # a[0] = ' '.join(a[0].split())
# # remove_digits = a[0].maketrans('', '', digits)
# # b = a[0].translate(remove_digits)
# if a[0][1] == '\n':
#     print('lxy my princess')
# print("lxy my princess")

EN = xlsxwriter.Workbook('D:/demo.xlsx')
AE = pd.read_excel('C:/Users/GUORUI/Desktop/数据清洗/公告企业.xlsx')
EN3 = AE['ZD_ABSC']
c = EN3[59]
# b = '   33456   789'
# d = '123'
# e = '135'
# for i in range(0, len(b)):
#     if b[i].isspace():
#         print(b)
#     else:
#         break
# print(b.find(d))
# print(b.find(e))
# g = b.replace(d, e)
# print(g)
# print(c)
# print(len(c))
# for i in range(0, len(c)-1):
#     print(c[i])
# print(c)
# for i in range(0,len(c)):
#     if c[i].isdigit() or c[i].isupper() or c[i].islower() or c[i].isspace():
#         print(1)
# s = ''
# for i in range(0x4e00, 0x9fa5):
#     s += chr(i)
# print(s)
# print(c)
# Obj = re.search(r'\r\n', c, re.M | re.I)
#
# print(Obj.group())
# p = 0
# print(len(c))
# for i in range(0, len(c)):
#     if c[i] == '\r':
#         if c[i+1] == '\n':
#             print('lxy')
# a = '12345678'
# for i in range(0,len(a)-1):
#     print(a[i])
print(c)
for i in range(0,len(c)):
    if c[i] == '\r':
        print(1)
    if c[i] == '\n':
        print(2)