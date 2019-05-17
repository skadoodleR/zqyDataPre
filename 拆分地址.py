#!/usr/bin/python
# -*- coding: <encoding name> -*-
import numpy
import pandas as pd
import xlsxwriter
import difflib
print('郭睿')

# ---------------------------------methods------------
def resymbol(str):
    if str == str and str != None:
        str = str.strip()
        for i in range(0,len(str)):
                if str[i].isalpha():
                        str = str[i:]
                        return str
        str = ''
def string_similar(s1, s2):
    return difflib.SequenceMatcher(None, s1, s2).quick_ratio()

# def find(str):
#         for i in range(len(length)):
#                 if shi[i] == str:
#                         return sheng[i]

# ----------------------------------------------------


write = xlsxwriter.Workbook('D:/拆分地址.xlsx')
sheet1 = write.add_worksheet('拆分')
province = pd.read_excel('C:/Users/GUORUI/Desktop/数据清洗/行政区划.xlsx', usecols=[1])
province = province.drop_duplicates()
province = province.reset_index()['省']
# city = pd.read_excel('C:/Users/GUORUI/Desktop/数据清洗/行政区划.xlsx', usecols=[2])
# city = city.drop_duplicates()
# city = city.reset_index()['市']
# district = pd.read_excel('C:/Users/GUORUI/Desktop/数据清洗/行政区划.xlsx', usecols=[3])
# district = district.drop_duplicates()
# district = district.dropna(axis=0, how='all')
# district = district.reset_index()['区县']
addr = pd.read_excel('D:/REA.xlsx', usecols=[1])
addr = addr['adr']
addr = addr.fillna('空')
mapi = pd.read_excel('C:/Users/GUORUI/Desktop/数据清洗/行政区划.xlsx')
mapi = mapi[['省','市','区县']]
district = mapi['区县'].fillna('空')
presheng = mapi['省']
preshi = mapi['市']
mapi = mapi.drop_duplicates()
sheng = mapi['省']
shi = mapi['市']
sheng = sheng.reset_index()['省']
shi = shi.reset_index()['市']
#
for i in range(0, len(addr)):
        a = 0
        b = 0
        temp = addr[i]
        sheet1.write(i, 0, temp)
        temp = temp.replace('中国', '').replace('中华人民共和国', '').replace('.','').replace('、','').replace(',','').replace('。','').replace('·','').replace('・','')
        temp = resymbol(temp)
        straight = ''
        sheet1.write(i, 1, temp)
        for j in range(0, len(province)):
                c = province[j]
                sub = temp[0:min(2,len(addr[i]))]
                if string_similar(sub, c[0:3]) > 0.76:
                        sheet1.write(i, 2, c)
                        a = 1
                        straight = c
                        temp = temp[2:]
                        break
        for j in range(0, len(shi)):
                c = shi[j]
                sub = temp[0:min(3,len(addr[i]))]
                if string_similar(sub, c[0:2]) > 0.76:
                        sheet1.write(i, 3, c)
                        newprovince = sheng[j]
                        b = 1
                        temp = temp[2:]
                        sheet1.write(i,2,newprovince)
                        break       
        for j in range(0, len(district)):
                sub = temp[0:min(3,len(addr[i]))]
                c = district[j]
                if string_similar(sub, c[0:2]) > 0.76:
                        sheet1.write(i, 4, c)
                        if b == 0:
                                sheet1.write(i, 3, preshi[j])
                        if a == 0:
                                sheet1.write(i, 2, presheng[j])
                        break
        if straight == '北京市' or straight == '天津市' or straight == '上海市' or straight == '重庆市':
                sheet1.write(i, 3, straight)
write.close()
print('李欣沂')
