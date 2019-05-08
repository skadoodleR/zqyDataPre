#!/usr/bin/python
# -*- coding: <encoding name> -*-
import numpy as np
import pandas as pd
import xlsxwriter
print('郭睿')
EN = xlsxwriter.Workbook('D:/EN.xlsx')
# ----------------------------------------------读文件---------------------------------------------
# CES = pd.read_excel('C:/Users/GUORUI/Desktop/数据清洗/20190426__数据清洗/20190419_合格证排放标准.xls')
# CPA = pd.read_excel('C:/Users/GUORUI/Desktop/数据清洗/20190426__数据清洗/20190419_合格证生产地址表.xls')
#
#

# -----------------------------拆分AE-----------------------
# AE = pd.read_excel('C:/Users/GUORUI/Desktop/数据清洗/公告企业.xlsx')
# EN3 = AE['ZD_ABSC']
#
# sheet = EN.add_worksheet('AE')
# # 去空值
# print(EN3.isnull().value_counts())
# EN3 = EN3.fillna('空')
# print(EN3.isnull().value_counts())
# row = 0
# for i in range(0, len(EN3)):
# # for i in range(0, 62):
#     # index 循环位置 num 插入行数索引 start 切割字符串的起始位置
#     index = 0
#     start = 0
#     num = 0
#     for index in range(0, len(EN3[i])):
#         EN3[i] = EN3[i].replace(', LTD', '++++')
#         EN3[i] = EN3[i].replace(',LTD', '++++')
#         EN3[i] = EN3[i].replace('，LTD', '++++')
#         EN3[i] = EN3[i].replace('， LTD', '++++')
#         EN3[i] = EN3[i].replace(',Ltd', '++++')
#         EN3[i] = EN3[i].replace(', Ltd', '++++')
#         EN3[i] = EN3[i].replace('， Ltd', '++++')
#         EN3[i] = EN3[i].replace('，Ltd', '++++')
#         if index < len(EN3[i]):
#             if EN3[i][index] == '\r' or EN3[i][index] == '\n':
#                 if EN3[i][start:index].isspace() or len(EN3[i][start:index]) == 0:
#                     p = 0
#                     start = index + 1
#                 else:
#                     EN3[i] = EN3[i].replace('++++', ', LTD')
#                     sheet.write(row, 0, EN3[i])
#                     sheet.write(row, 1, EN3[i][start:index])
#                     start = index + 2
#                     sheet.write(row, 2, num)
#                     row += 1
#                     num += 1
#             if EN3[i][index] == "," or EN3[i][index] == "，" or EN3[i][index] == ";" or EN3[i][index] == "；" \
#                     or EN3[i][index] == "/" or EN3[i][index] == "、":
#                 if EN3[i][start:index].isspace() or len(EN3[i][start:index]) == 0:
#                     p = 0
#                     start = index + 1
#                 else:
#                     EN3[i] = EN3[i].replace('++++', ', LTD')
#                     sheet.write(row, 0, EN3[i])
#                     sheet.write(row, 1, EN3[i][start:index])
#                     start = index + 1
#                     sheet.write(row, 2, num)
#                     row += 1
#                     num += 1
#             elif index == len(EN3[i]) - 1:
#                 if EN3[i][start:index].isspace() or len(EN3[i][start:index]) == 0:
#                     p = 0
#                     start = index + 1
#                 else:
#                     EN3[i] = EN3[i].replace('++++', ', LTD')
#                     sheet.write(row, 0, EN3[i])
#                     sheet.write(row, 1, EN3[i][start:index + 1])
#                     sheet.write(row, 2, num)
#                     row += 1

# --------------------------拆分AC--------------------------------
# sheet2 = EN.add_worksheet('AC')
# AC = pd.read_excel('C:/Users/GUORUI/Desktop/数据清洗/20190426__数据清洗/20190426_底企型拆分映射表.xls')
# EN1 = AC['底盘企业']
# PRE = AC['底企型']
# print(EN1.isnull().value_counts())
# EN1 = EN1.fillna(' ')
# for i in range(0, len(PRE)):
#     if EN1[i] == ' ':
#         EN1[i] = PRE[i]
# print(EN1.isnull().value_counts())
# for i in range(0, len(PRE)):
#     sheet2.write(i, 0, PRE[i])
#     sheet2.write(i, 1, EN1[i])

# ----------------------------拆分AAC--------------------------------
# sheet3 = EN.add_worksheet('AAC')
# AAC = pd.read_excel('C:/Users/GUORUI/Desktop/数据清洗/公告底企型.xlsx')
# EN2 = AAC['底企型1']
# for i in range(0, len(EN2)):
#     sheet3.write(i, 0, EN2[i])
#     # # EN2[i] = ' '.join(EN2[i].split())
#     # # temparr = EN2[i].split(' ')
#     # # eid = EN2[i].replace(temparr[len(temparr) - 1], '')
#     # # eid = eid.replace(temparr[len(temparr) - 2], '')
#     # # sheet3.write(i, 2, temparr[len(temparr) - 2])
#     # # sheet3.write(i, 3, temparr[len(temparr) - 1])
#     # # sheet3.write(i, 1, eid)
#     finish = 0
#     for index in range(0, len(EN2[i])):
#         # if EN2[i][index].isupper() or EN2[i][index].islower() or EN2[i][index].isdigit() or EN2[i][index].isspace():
#         if'\u9fa5' > EN2[i][index] >= '\u4e00':
#             break
#         else:
#             finish += 1
#     sheet3.write(i, 4, finish)
#     eid = EN2[i][:finish]
#     stringid = ' '.join(EN2[i].split())
#     temparr = stringid.split(' ')
#     sheet3.write(i, 1, eid)
#     sheet3.write(i, 3, temparr[len(temparr) - 1])
#     stringid = stringid.replace(temparr[len(temparr) - 1], '')
#     for index in range(0, len(stringid)):
#         if '\u9fa5' > stringid[index] >= '\u4e00':
#             sheet3.write(i, 2, stringid[index-1:])

# ----------------------------拆分CPE--------------------------
# sheet4 = EN.add_worksheet('CPE')
# CPE = pd.read_excel('C:/Users/GUORUI/Desktop/数据清洗/20190426__数据清洗/20190419_合格证生产企业.xls')
# EN4 = CPE['clscdwmc']
# print(EN4.isnull().value_counts())
# EN4 = EN4.fillna('N/A')
# print(EN4.isnull().value_counts())
# row = 0
# for i in range(0, len(EN4)):
#     index = 0
#     start = 0
#     for index in range(0, len(EN4[i])):
#         if EN4[i][index].isdigit() or EN4[i][index] == '，' or EN4[i][index] == '.' or EN4[i][index] == ',':
#             if start == index:
#                 start += 1
#     if len(EN4[i][start:len(EN4[i])]) > 1:
#         sheet4.write(row, 0, EN4[i])
#         sheet4.write(row, 1, EN4[i][start:len(EN4[i])])
#         row += 1

# ---------------------------------拆分CME----------------------------
# sheet5 = EN.add_worksheet('CME')
# CME = pd.read_excel('C:/Users/GUORUI/Desktop/数据清洗/20190426__数据清洗/20190419_合格证制造企业.xls')
# EN5 = CME['clzzqymc']
# row = 0
# for i in range(0, len(EN5)):
#     num = 0
#     numz = 0
#     for index in range(0, len(EN5[i])):
#         if EN5[i][index].isupper() or EN5[i][index].islower():
#             num += 1
#         elif EN5[i][index].isdigit() or EN5[i][index].isspace():
#             continue
#         else:
#             numz += 1
#     if num < 5 and numz > 4:
#         sheet5.write(row, 0, EN5[i])
#         sheet5.write(row, 1, EN5[i])
#         row += 1
#
# EN.close()
print('李欣沂')


