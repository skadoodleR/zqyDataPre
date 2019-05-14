#!/usr/bin/python
# -*- coding: <encoding name> -*-
# --------------------------外廓长---------------
import pandas as pd
import numpy as np
import xlsxwriter
import re

write = xlsxwriter.Workbook('D:/大数/规整后/外廓长.xlsx')
sheet1 = write.add_worksheet('外廓长')
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
        if str == str and str != None and len(str) > 1:
                if str[len(str) - 1].isdigit():
                        return str
                else:
                        return str[:len(str) - 1]
# -------------------------- dont have methods-----


M = pd.read_excel('D:/大数/原始值/外廓长.xlsx', usecols=[0])
M = M.sort_values(by='长')
M = M.dropna(axis=0, how='all')
M = M.drop_duplicates()
M = M.reset_index()['长']
# indecs = pd.DataFrame(columns=['index', 'indecs'])
# indecs = indecs['indecs']
# indecs.loc[0] = '-'
indecs = pd.read_excel('D:/大数/index/外廓长.xlsx')
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
# indecs.to_excel('D:/大数/index/外廓长.xlsx')

for i in range(0, len(indecs)): 
    sheet1.write(i, 0, indecs[i])
    temp = indecs[i]
    temp = resymbol(temp)
    temp = reversesymbol(temp)
    if temp != None and ',' in temp:
        temp = temp.replace('(选装前号牌架','').replace(';',',').replace('；',',').replace('-',',').replace('),',',').replace(',,',',').replace(')(',',').replace('(',',').replace(')',',').replace('ABS,','').replace('ECU,','').replace(',运动版保险杠','').replace(',加提桶机构','').replace(',含前伸','').replace(',含尾梯','').replace(',带喷水架','')
        print(i)
        result = temp.split(',')
        result = list(map(float,result))
        sheet1.write(i, 1, temp)
        sheet1.write(i, 2, max(result))
        sheet1.write(i, 3, min(result))
    else:
        temp = resymbol(temp)
        sheet1.write(i, 1, temp)
        sheet1.write(i, 2, temp)
        sheet1.write(i, 3, temp)
write.close()
print('李欣沂')
