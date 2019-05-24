#!/usr/bin/python
# -*- coding: <encoding name> -*-
import numpy
import pandas as pd
import re
import xlsxwriter
print('郭睿')

write = xlsxwriter.Workbook('D:/new拆分.xlsx')
sheet = write.add_worksheet('name')
AE = pd.read_excel('C:/Users/GUORUI/Desktop/数据清洗/公告企业.xlsx')
EN3 = AE['ZD_ABSC']
EN3 = EN3.dropna(axis=0, how='all')
EN3 = EN3.drop_duplicates()
EN3 = EN3.reset_index()['ZD_ABSC']
row = 0

for i in range(0,len(EN3)):
    temp = EN3[i]
    temp = temp.replace('（','(').replace('）',')')
    temp = re.sub('\d\\/\d','',temp)
    temp = re.sub('N\\/A','',temp)
    temp = temp.replace('NA','')
    temp = re.sub('\\(\d\d.*?\\)','',temp)
    # temp = re.sub('R.*?\d.*\\,',',',temp)
    temp = re.sub('A\\/.*?\\:','',temp)
    temp = re.sub('\\([A-Z]+?[0-9]\\)','',temp)
    temp = re.sub('BOSCH\\(.*?\\)','BOSCH',temp)
    temp = re.sub('\\(对应.*?\\)','',temp)
    temp = re.sub('\\(\d.*?\\)','',temp)
    temp = re.sub('\\(.*?[A-Z]\\,[A-Z].*?\\)','',temp)
    temp = re.sub('\\(.*?3C证书.*?\\)','',temp)
    temp = re.sub('\\(.*?CCC证书.*?\\)','',temp)
    temp = re.sub('\\(软.*?\\)','',temp)
    temp = re.sub('\\(硬.*?\\)','',temp)
    
    temp = temp.replace(', LTD', '￥￥￥').replace(',LTD', '￥￥￥').replace('，LTD', '￥￥￥').replace('， LTD', '￥￥￥').replace(',Ltd', '￥￥￥').replace(', Ltd', '￥￥￥').replace('， Ltd', '￥￥￥').replace('，Ltd', '￥￥￥')
    temp = temp.replace('，',',').replace(';',',').replace('；',',').replace('/',',').replace('\n',',').replace('、',',').replace('+',',')
    if temp != None and ','in temp:
        print(i)
        result = temp.split(',')
        result = list(map(str,result))
        index = 0
        for j in range(0, len(result)):
            if len(result[j]) > 1 and not result[j].isspace():
                sheet.write(row,0,EN3[i])
                sheet.write(row,1,result[j].replace('￥￥￥', ', LTD'))
                sheet.write(row,2,index)
                row +=1
                index +=1

write.close()
print('lxy')