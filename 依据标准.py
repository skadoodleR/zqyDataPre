#!/usr/bin/python
# -*- coding: <encoding name> -*-
# -------------------------依据标准--------------
# 有欧标 剩下的特殊的都在下面了
import pandas as pd
import numpy as np
import xlsxwriter
import re
write = xlsxwriter.Workbook('D:/大数/规整后/依据标准.xlsx')
sheet1 = write.add_worksheet('依据标准')
print('郭睿')
# ---------------------------methods---------------
def resymbol(str):
    if str == str and str != None:
        str = str.strip()
        for i in range(0,len(str)):
                if str[i].isdigit():
                        str = str[i:]
                        return str
        str = ''

def reversesymbol(str):
    if str == str and str != None:
        for i in range(0,len(str)):
            if str[len(str) - i - 1].isnumeric():
                    return str[:len(str)-i]
        str = ''

def addGB(str):
    if str[0].isdigit():
        return 'GB'+str
    elif str[0] == 'B':
        return 'G'+str
    else:
        return str
# -------------------------- dont have methods-----


M = pd.read_excel('D:/大数/原始值/依据标准.xlsx', usecols=[0])
M = M.sort_values(by='依据标准')
M = M.dropna(axis=0, how='all')
M = M.drop_duplicates()
M = M.reset_index()['依据标准']
indecs = pd.read_excel('D:/大数/index/依据标准.xlsx')
indecs = indecs['indecs']

# # ------------------二分查找--------只运行一次就行
# for i in range(0, len(M)):
#     cur = M[i]
#     first = 0
#     n = len(indecs)
#     last = n - 1
#     while first <= last:
#         mid = (last + first) // 2
#         if str(indecs[mid]) > str(cur):
#             last = mid - 1
#         elif str(indecs[mid]) < str(cur):
#             first = mid + 1
#         else:
#             break
#     indecs.loc[len(indecs)] = cur
# # -------------------------查之前存在的xlsx文件
# indecs.to_excel('D:/大数/index/依据标准.xlsx')

for i in range(0, len(indecs)): 
    sheet1.write(i, 0, indecs[i])
    temp = indecs[i]
    temp = addGB(temp)
    temp = temp.replace('第1','一').replace('第2','二').replace('第3','三').replace('第4','四').replace('第5','五').replace('第6','六').replace('2阶段','二').replace('2实施','').replace('排放','').replace('排放依据标准','').replace('压燃机排污物限值方法','').replace('无NOx和IUPR监测','').replace('实施','')
    temp = temp.replace(' ','').replace('(','').replace(')','').replace('（','').replace('）','').replace('国','').replace('第','').replace('阶段','').replace('～','-').replace('~','-')
    temp = temp.replace('，',',').replace(';',',').replace('；',',').replace('、',',')
    temp = temp.replace('III','Ⅲ').replace('II','Ⅱ').replace('IV','Ⅳ').replace('VI','Ⅵ').replace('I','Ⅰ').replace('V','Ⅴ').replace('Ⅲ','国Ⅲ').replace('Ⅱ','国Ⅱ').replace('Ⅳ','国Ⅳ').replace('Ⅵ','国Ⅵ').replace('Ⅰ','国Ⅰ').replace('Ⅴ','国Ⅴ').replace('三','国Ⅲ').replace('二','国Ⅱ').replace('四','国Ⅳ').replace('六','国Ⅵ').replace('一','国Ⅰ').replace('五','国Ⅴ')
    temp = reversesymbol(temp)
    sheet1.write(i, 1, temp)
write.close()
print('李欣沂')
