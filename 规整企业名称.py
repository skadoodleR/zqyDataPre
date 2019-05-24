#!/usr/bin/python
# -*- coding: <encoding name> -*-
import pandas as pd
import xlsxwriter
import re
print('郭睿')
rn = xlsxwriter.Workbook('D:/RN.xlsx',{'nan_inf_to_errors': True})
# -------------------methods-----------------------------


def resymbol(str):
    if str == str and str != None:
        str = str.strip()
        for i in range(0,len(str)-1):
                if str[i].isalpha() or (str[i] == '3' and str[i+1] == 'M'):
                        str = str[i:]
                        return str
        str = ''

def reversesymbol(str):
    if str == str and str != None:
        for i in range(0,len(str)):
            if str[len(str) - i - 1].isalpha():
                    return str[:len(str)-i]
        str = ''

def rebrackets(str):
    if str == str and str != None:
        start = 0
        end = 0
        weight = 0
        for i in range(0, len(str)):
            if str[i] == '(':
                start = i
            elif str[i] == ')' and i > start:
                end = i
                break
        if end == 0:
            return str
        for index in range(start + 1, end - 1):
            if ischinese(str[index]) : 
                weight += 1
        if weight * 4 < (end - start - 1):
            str = str.replace(str[start:end + 1], '')
        return str


def regcompany(str):
    if str != None and len(str) > 2:
        if str[len(str) - 1] == "公":
            str = str + "司"
        return str


def ischinese(str):
    if '\u9fa5' > str >= '\u4e00':
        return True
    else:
        return False
# ---------------------------------规整EN--------------------------


pre = pd.read_excel('D:/rest整合.xlsx')
pen = pre['yuan']
en = pre['chai']
nm = pre['indecs']
sheet1 = rn.add_worksheet('RN')
for i in range(0, len(en)):
    a = pen[i]
    b = en[i]
    if a == a:
        sheet1.write(i, 0, a)
        sheet1.write(i,1,b)
        b = resymbol(b)
        # b = rebrackets(b)
        # b = rebrackets(b)
        b = regcompany(b)
        if b != None and b[0:5] == '对应负荷指':
            b = ''
        b = resymbol(b)
        if b != None and b[0] == 'R' and (b[1] == '1' or b[1] == '2'):
            b = b[3:]
        b = resymbol(b)
        if b != None and b[0].isupper() and b[1] == ':':
            b = b[2:]
        if b != None and b[0] =='M' and b[1] == 'C':
            b = ''
        if b != None and len(b) > 3 and (b[0] == '寸' or b[0] == '吋' or b[0] == '前' or b[0] == '后'):
            if b[3] == '盘':
                b = b[5:]
            else:
                b = b[2:]
        # if b != None and b[0] == 'Z' and b[1] == 3:
        #     b = ''
        if b != None and len(b) > 2 and b[0] == '座':
            b = b[2:]
        if b != None and len(b) > 2 and b[0].isupper() and b[1] == ':':
            b = b[2:]
        if b != None and len(b) > 2 and b[0] == '配' and b[1] == '置':
            b = b[3:]
        if b != None and len(b) > 2 and b[0] == 'L' and b[1] == 'T':
            b = b[7:]
        if b != None and len(b) > 2 and b[0] == 'P' and b[1] == 'R':
            b = b[2:]
        if b != None and len(b) > 2 and b[0] == '两' and b[1] == '侧':
            b = b[3:]
        if b != None and len(b) > 2 and b[0] == 'C' and b[1] == '证':
            b = b[5:]
        if b != None and len(b) > 2 and b[0] == 'C' and b[1].isspace() and b[2] == '8':
            b = b[7:]
        if b != None and len(b) > 2 and b[0] == 'A' and (b[1] == '(' or ischinese(b[1])):
            b = b[1:]
        if b != None and len(b) > 2 and b[0] == 'A' and b[1] == '：':
            b = b[2:]
        if b != None and len(b) > 2 and b[0] == 'B' and b[1] == '：':
            b = b[2:]
        if b != None and len(b) > 2 and b[0] == 'C' and b[1] == '：':
            b = b[2:]
        if b != None and len(b) > 2 and b[0] == '第' and(b[1] == '一' or b[1] == '二')and b[2] == '组':
            b = b[4:]
        if b != None and len(b) > 2 and b[0] == '第' and b[1] == '二' and b[2] == '轴':
            b = b[4:]
        if b != None and len(b) > 2 and b[0:2] == 'ZR1' :
            b = b[4:]
        if b != None and len(b) > 2 and b[0:1] == 'Z3' :
            b = ''
        if b != None and len(b) > 2 and (b[0:2] == 'YC4' or b[0:2] == 'YC6' ):
            b = b[9:]
        if b != None and len(b) > 2 and b[0] == '胎' :
            b = b[2:]
        if b != None:
            b = b.replace('（','(').replace('）',')')
        b = resymbol(b)
        b = reversesymbol(b)
        sheet1.write(i, 2, b)
        sheet1.write(i,3,0)
rn.close()
print('李欣沂')
