#!/usr/bin/python
# -*- coding: <encoding name> -*-
# --------------------------工况法里程---------------
import pandas as pd
import numpy as np
import xlsxwriter
import re

write = xlsxwriter.Workbook('D:/大数5/规整后/条件B试验燃油消耗量.xlsx')
sheet1 = write.add_worksheet('条件B试验燃油消耗量')
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
            if str[len(str) - i - 1].isdigit():
                    return str[:len(str)-i]
        str = ''
# -------------------------- dont have methods-----


M = pd.read_excel('D:/大数5/条件B试验燃油消耗量.xlsx', usecols=[0],header = 0)
M = M.sort_values(by='TJBRLXHL')
M = M.dropna(axis=0, how='all')
M = M.drop_duplicates()
M = M.reset_index()['TJBRLXHL']
# indecs = pd.DataFrame(columns=['index', 'indecs'])
# indecs = indecs['indecs']
# indecs.loc[0] = '-'
indecs = pd.read_excel('D:/大数5/index/条件B试验燃油消耗量.xlsx')
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
# indecs.to_excel('D:/大数5/index/条件B试验燃油消耗量.xlsx')

for i in range(0, len(indecs)): 
    sheet1.write(i, 0, indecs[i])
    temp = indecs[i]
    temp = re.sub('\\(.*?\\)','',temp)
    temp = re.sub('\\（.*?\\）','',temp)
    temp = re.sub('\\(.*?\\）','',temp)
    temp = temp.replace('≥','').replace('，',',').replace(';',',').replace('；',',').replace(' ','')
    temp = resymbol(temp)
    temp = reversesymbol(temp)
    if temp != None and ',' in temp:
        sheet1.write(i, 1, temp)
        result = temp.split(',')
        result = list(map(float,result))
        sheet1.write(i, 2, max(result))
        sheet1.write(i, 3, min(result))
    else:
        temp = resymbol(temp)
        sheet1.write(i, 1, temp)
        sheet1.write(i, 2, temp)
        sheet1.write(i, 3, temp)
write.close()
print('李欣沂')
