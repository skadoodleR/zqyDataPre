#!/usr/bin/python
# -*- coding: <encoding name> -*-
import numpy
import pandas as pd
import xlsxwriter
print('郭睿')
# ----------------------------还原规整好的企业名称用分隔符--------------
data = pd.read_excel('D:/拆分后企业地址.xlsx')
write = xlsxwriter.Workbook('D:/最终地址名单.xlsx',{'nan_inf_to_errors': True})
sheet = write.add_worksheet('RN')
en = data['二']
index = data['叁']
pre = data['一']
row = 0
strstr = ''
for i in range(0, len(index)-1):
    if index[i] == 0:
        strstr = en[i]
        if index[i + 1] != 0:
            continue
        sheet.write(row, 0, pre[i])
        if strstr == None:
            strstr = '空'
        sheet.write(row, 1, strstr)
        row += 1
        strstr = ''
        continue
    else:
        if index[i + 1] == 0:
            if en[i] == None:
                sheet.write(row, 0, pre[i - 1])
                sheet.write(row, 1, strstr)
                row += 1
                strstr = ''
            else:
                strstr = str(strstr) + '+' + str(en[i])
                sheet.write(row, 0, pre[i - 1])
                sheet.write(row, 1, strstr)
                row += 1
                strstr = ''
        if en[i] == None:
            continue
        else:
            strstr = str(strstr) + '+' + str(en[i])

write.close()
print('李欣沂')