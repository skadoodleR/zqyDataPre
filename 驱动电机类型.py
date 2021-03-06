#!/usr/bin/python
# -*- coding: <encoding name> -*-
# --------------------------驱动电机类型---------------
import pandas as pd
import numpy as np
import xlsxwriter
import re

write = xlsxwriter.Workbook('D:/大数5/规整后/驱动电机类型.xlsx')
sheet1 = write.add_worksheet('驱动电机类型')
print('郭睿')
# ---------------------------methods---------------
def resymbol(str):
    if str == str and str != None:
        str = str.strip()
        for i in range(0,len(str)):
                if str[i].isdigit() or str[i].isalpha():
                        str = str[i:]
                        return str
        str = ''


def reversesymbol(str):
    if str == str and str != None:
        for i in range(0,len(str)):
            if str[len(str) - i - 1].isdigit() or str[len(str) - i - 1].isalpha():
                    return str[:len(str)-i]
        str = ''
# -------------------------- dont have methods-----


M = pd.read_excel('D:/大数5/驱动电机类型.xlsx', usecols=[0],header = 0)
M = M.sort_values(by='DDQCQDLX')
M = M.dropna(axis=0, how='all')
M = M.drop_duplicates()
M = M.reset_index()['DDQCQDLX']
# indecs = pd.DataFrame(columns=['index', 'indecs'])
# indecs = indecs['indecs']
# indecs.loc[0] = '-'
indecs = pd.read_excel('D:/大数5/index/驱动电机类型.xlsx')
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
# indecs.to_excel('D:/大数5/index/驱动电机类型.xlsx')

for i in range(0, len(indecs)): 
    sheet1.write(i, 0, indecs[i])
    temp = indecs[i]
    temp = re.sub('\\(.*?\\)','',temp)
    temp = re.sub('\\（.*?\\）','',temp)
    temp = re.sub('前.*?\\:','',temp)
    temp = re.sub('后.*?\\:','',temp)
    temp = re.sub('电.*?\\:','',temp)
    temp = re.sub('前.*?\\：','',temp)
    temp = re.sub('后.*?\\：','',temp)
    temp = temp.replace('≥','').replace('，',',').replace(';',',').replace('；',',').replace(' ','').replace('/',',').replace('、',',').replace('+',',').replace(',,',',')
    temp = resymbol(temp)
    temp = reversesymbol(temp)
    sheet1.write(i, 1, temp)
write.close()
print('李欣沂')
