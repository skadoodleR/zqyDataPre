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
import difflib
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

# EN = xlsxwriter.Workbook('D:/demo.xlsx')
# a = pd.read_excel('C:/Users/GUORUI/Desktop/1.xls')
# sheet = EN.get_worksheet_by_name('1')
# print(sheet)
#
# rb = xlrd.open_workbook('C:/Users/GUORUI/Desktop/1.xls')
# ws = rb.get_sheet(0)
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
# print(c)
# for i in range(0,len(c)):
#     if c[i] == '\r':
#         print(1)
#     if c[i] == '\n':
#         print(2)
# a = float('NaN')
# print(a == a)
a = ['......123456公  ','123456公(1438/ppp)123','123456  ','123456有限公司  ']

def regcompany(cname):
    cname = cname.strip()
    if cname[len(cname) - 1] == "公":
        cname = cname + "司"
    return cname
def ischinese(str):
    if '\u9fa5' > str >= '\u4e00':
        return True
    else:
        return False

def resymbol(str):
    str = str.strip()
    for i in range(0,len(str)-1):
        if str[i].isalpha() or str[i].isdigit():
            str = str[i:]
            break
    return str
def rebrackets(str):
    str = str.strip()
    start = 0
    end = 0
    weight = 0
    for i in range(0,len(str)):
        if str[i] == '(':
            start = i
        elif str[i] == ')' and i > start:
            end = i
            break
    if end == 0:
        return str
    for index in range(start+1,end-1):
        if str[index].isalpha():
            weight += 1
    if weight*2 < (end - start - 1):
        str = str.replace(str[start:end+1], '')
    return str


# a = ['100','98']
# a =list(map(int, a))
# a = '123(123456)'
# print(re.sub('\\(.*?\\)','',a))
# print('' == None)
def reversesymbol(str):
    if str == str and str != None:
        for i in range(0,len(str)):
            if str[len(str) - i - 1].isdigit():
                    return str[:len(str)-i]
        str = ''

a = 'a中,,文,,:5'
# # print('OO'.isdigit())
# print(re.sub('文.*?\\:','',a))
# print(re.sub(',,*?','','1,,,,,,2,,,,,3,33'))

# print('Ⅱ'.isnumeric())


# def string_similar(s1, s2):
#     return difflib.SequenceMatcher(None, s1, s2).quick_ratio()


# print(string_similar('州经济区', '通州'))

# a = '123456'
# a = a[2:]
# a = a[2:]
# print(a)
# temp = '配置1：360,配置2：320'
# temp = re.sub('配.*?\\：','',temp)
# print(temp)
str = '1820sadewwec:5165124512c'
# print(re.sub(r'[^\x00-\x7f]', ' ', str)
print(re.sub('\d.*?c','',str))