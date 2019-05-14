#!/usr/bin/python
# -*- coding: <encoding name> -*-
import pandas as pd
import numpy as np
import xlsxwriter
EA = xlsxwriter.Workbook('D:/REA.xlsx')
# ------------------------menthods--------------
def resymbol(str):
    if str == str and str != None:
        str = str.strip()
        for i in range(0,len(str)):
                if str[i].isalpha():
                        str = str[i:]
                        return str
        str = ''
# 

def reversesymbol(str):
        if str == str and str != None and len(str) > 1:
                if str[len(str) - 1].isalpha() or str[len(str) - 1].isdigit():
                        return str
                else:
                        return str[:len(str) - 1]
def realpha(str):
    if str == str and str != None:
        str = str.strip()
        for i in range(0, len(str)):
            if str[i].isupper() or str[i].islower():
                str = str[i:]
                return str
        str = ''

def ischinese(str):
    if '\u9fa5' > str >= '\u4e00':
        return True
    else:
        return False

def rebrackets(str):
    if str == str and str != None:
        start = 0
        end = 0
        for i in range(0,len(str)):
            if str[i] == '(' or str[i] == '（':
                start = i
            elif (str[i] == ')' or str[i] == '）') and start < i:
                end = i
                break
        if end - start == 0:
            return str
        str = str.replace(str[start:end+1], '')
        return str
# --------------------------规整EA-----------
pre = pd.read_excel('D:/拆分后企业地址.xlsx')
pea = pre['一']
ea = pre['二']
sheet1 = EA.add_worksheet('RA')
for i in range(0, len(ea)):
    a = pea[i]
    b = ea[i]
    sheet1.write(i, 0, a)
    b = resymbol(b)
    b = rebrackets(b)
    b = reversesymbol(b)
    if b == None or len(b) < 3:
        continue
    for g in range(0,len(b)-2):
        #下面这些 都是识别指定汉字 然后读到下一个汉字在截取字符串替换
        if g+1 < len(b) and ((b[g] == '邮' and b[g+1] == '编') or (b[g] == '传' and b[g+1] == '真') or (b[g] == '电' and b[g+1] == '话') or (b[g] == '网' and b[g+1] == '址') or (b[g] == '查' and b[g+1] == '询') or (b[g] == '邮' and b[g+1] == '政') or (b[g] == '编' and b[g+1] == '码') or (b[g] == '公' and b[g+1] == '司') or (b[g] == '网' and b[g+1] == '站') or (b[g] == '0' and b[g+1] == '3')  or (b[g] == '销' and b[g+1] == '售')):
            vaper = g
            for v in range(g+2,len(b) - 1):
                if ischinese(b[v]):
                    vaper = v
            if vaper == g:
                vaper = len(b)
            b = b.replace(b[g:vaper-1],'') 
    for g in range(0,len(b)-2):
        #下面这些 都是识别指定汉字 然后读到下一个汉字在截取字符串替换
        if g+1 < len(b) and ((b[g] == '邮' and b[g+1] == '编') or (b[g] == '传' and b[g+1] == '真') or (b[g] == '电' and b[g+1] == '话') or (b[g] == '网' and b[g+1] == '址') or (b[g] == '查' and b[g+1] == '询') or (b[g] == '邮' and b[g+1] == '政') or (b[g] == '编' and b[g+1] == '码') or (b[g] == '公' and b[g+1] == '司') or (b[g] == '网' and b[g+1] == '站') or (b[g] == '0' and b[g+1] == '3')  or (b[g] == '销' and b[g+1] == '售')):
            vaper = g
            for v in range(g+2,len(b) - 1):
                if ischinese(b[v]):
                    vaper = v
            if vaper == g:
                vaper = len(b) + 1
            b = b.replace(b[g:vaper-1],'')        
    sheet1.write(i, 1, b)

EA.close()
print('李欣沂')