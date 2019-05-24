#!/usr/bin/python
# -*- coding: <encoding name> -*-
import numpy
import pandas as pd
import re
import xlsxwriter
print('郭睿')

read1 = pd.read_excel('D:/new规整.xlsx')
read2 = pd.read_excel('D:/28万手动.xlsx')
write = xlsxwriter.Workbook('D:/处理1.xlsx',{'nan_inf_to_errors': True})
sheet = write.add_worksheet('en')
chai = read1['chai']
yuan1 = read1['yuan']
yuan2 = read2['yuan']
gui = read2['gui']
index1 = read1['indecs']
index2 = read2['indecs']
for i in range(0,50):
    for g in range(0,len(index2)):
        if yuan1[i] == yuan2[g]:
            if index1[i] == index2[g]:
                print(i)
                sheet.write(i,0,yuan1[i])
                sheet.write(i,1,chai[i])
                sheet.write(i,2,gui[g])
                sheet.write(i,3,index1[i])
            break
write.close()
