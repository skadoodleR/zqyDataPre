#!/usr/bin/python
# -*- coding: <encoding name> -*-
import numpy
import pandas as pd
import xlsxwriter
import re

# ---------- methods------
def resymbol(str):
    if str == str and str != None:
        str = str.strip()
        for i in range(0,len(str)-1):
                if str[i].isalpha() or '3M' in str:
                        str = str[i:]
                        return str
        str = ''
def reversesymbol(str):
    if str == str and str != None:
        for i in range(0,len(str)):
            if str[len(str) - i - 1].isalpha() or str[len(str) - i - 1] == ')':
                    return str[:len(str)-i]
        str = ''

write = xlsxwriter.Workbook('D:/new规整.xlsx',{'nan_inf_to_errors': True})
sheet = write.add_worksheet('name')
print('郭睿')
data = pd.read_excel('D:/new拆分.xlsx')
pre = data['原']
chai = data['拆']
index = data['indecs']

for i in range(0,len(pre)):
    temp = chai[i]
    temp = temp.replace('：',':')
    sheet.write(i,0,pre[i])
    sheet.write(i,1,temp)
    sheet.write(i,3,index[i])
    sheet.write(i,4,i)
    temp = reversesymbol(resymbol(temp))
    temp = re.sub('配置.*?\\:','',str(temp))
    temp = re.sub('.*?R.*?\\(','',temp)
    temp = re.sub('[A-Z].*?\\:','',temp)
    temp = re.sub('.*?P\\:','',temp)
    temp = re.sub('.*?PR','',temp)
    temp = re.sub('\\(.*?胎\\)','',temp)
    temp = temp.replace('座:','')
    temp = re.sub('BOSCH公司\\(.*','BOSCH',temp)
    temp = re.sub('.*?为BOSCH','BOSCH',temp)
    temp = re.sub('.*?为DENSO','DENSO',temp)
    temp = re.sub('DELPHI\\(.*','DELPHI',temp)
    temp = re.sub('DENSO\\(.*','DENSO',temp)
    temp = re.sub('HELLA\\(.*?','HELLA',temp)
    temp = re.sub('R.*?\\)','',temp)
    temp = re.sub('Y.*?\\)','',temp)
    temp = re.sub('A.*?\\)','',temp)
    temp = re.sub('C.*?\\)','',temp)
    temp = re.sub('L.*?\\)','',temp)
    temp = re.sub('M.*?\\)','',temp)
    temp = re.sub('C.*?F','',temp)
    temp = re.sub('EDC.*?','',temp)
    temp = re.sub('ISF .*?','',temp)
    # temp = re.sub('.*?[A-Z]\\(','',temp)
    temp = temp.replace('R20','').replace('R22.5(','').replace('R22.5','').replace('前','').replace('后','')
    print(i)
    temp = resymbol(temp)
    sheet.write(i,2,temp)

write.close()
print('lxy')
    
