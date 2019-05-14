#!/usr/bin/python
# -*- coding: <encoding name> -*-
# --------------------------发动机型号---------------
import pandas as pd
import numpy as np
import xlsxwriter
write = xlsxwriter.Workbook('D:/大数/规整后/M型号.xlsx')
sheet1 = write.add_worksheet('M型号')
print('郭睿')
# ---------------------------methods---------------
# L到ml要手动转换
def resymbol(str):
    if str == str and str != None:
        str = str.strip()
        for i in range(0,len(str)):
                if str[i].isdigit() or str[i].isalpha():
                        str = str[i:]
                        return str
        str = ''

def reversesymbol(str):
        if str == str and str != None and len(str) > 1:
                if str[len(str) - 1].isdigit() or str[len(str) - 1].isalpha() or str[len(str) - 1] == ')':
                        return str
                else:
                        return str[:len(str) - 1]
# -------------------------- dont have methods-----


M = pd.read_excel('D:/大数/原始值/M型号.xlsx', usecols=[0])
M = M.sort_values(by='M发动机')
M = M.dropna(axis=0, how='all')
M = M.drop_duplicates()
M = M.reset_index()['M发动机']
indecs = pd.read_excel('D:/大数/index/M发动机.xlsx')
indecs = indecs['indecs']

# # ------------------二分查找--------
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
# indecs.to_excel('D:/大数/index/M发动机.xlsx')

for i in range(0, len(indecs)): 
    sheet1.write(i, 0, indecs[i])
    temp = indecs[i]
    temp = temp.replace(',','=').replace(';','=').replace('；','=').replace('\n','=')
    temp = reversesymbol(temp)
    temp = resymbol(temp)
    sheet1.write(i, 1, temp)
write.close()
print('李欣沂')