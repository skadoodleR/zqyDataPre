#!/usr/bin/python
# -*- coding: <encoding name> -*-
import numpy
import pandas as pd
import xlsxwriter
print('郭睿')
# ----------------------------还原规整好的企业名称用分隔符--------------
data = pd.read_excel('C:/Users/GUORUI/Desktop/zzz新建文件夹/28万手动.xlsx')
write = xlsxwriter.Workbook('D:/最终企业名单3.0.xlsx',{'nan_inf_to_errors': True})
sheet = write.add_worksheet('RN')
en = data['gui']
index = data['indecs']
pre = data['yuan']
row = 0
strstr = ''
for i in range(0, len(index)-1):
    if index[i] == 0:
        strstr = en[i]
        if index[i + 1] != 0:
            continue
        sheet.write(row, 0, pre[i])
        strstr = str(strstr).replace('None','')
        strstr = str(strstr).replace('nan','')
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
                strstr = str(strstr).replace('None+','')
                strstr = str(strstr).replace('nan+','')
                sheet.write(row, 0, pre[i - 1])
                strstr = str(strstr).replace('+None','')
                strstr = str(strstr).replace('+nan','')
                sheet.write(row, 1, strstr)
                row += 1
                strstr = ''
        if en[i] == None:
            continue
        else:
            strstr = str(strstr) + '+' + str(en[i])

write.close()
print('李欣沂')