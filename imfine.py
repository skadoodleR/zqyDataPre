#!/usr/bin/python
# -*- coding: <encoding name> -*-
import pandas as pd
import xlsxwriter
print('郭睿')
EA = xlsxwriter.Workbook('D:/EA.xlsx')

# -------------------------------------------拆分CPA--------------
# CPA = pd.read_excel('C:/Users/GUORUI/Desktop/数据清洗/20190426__数据清洗/20190419_合格证生产地址表.xls')
# EA1 = CPA['cpscdz']
# sheet1 = EA.add_worksheet('CPA')
# print(EA1.isnull().value_counts())
# EA1 = EA1.fillna('NA')
# print(EA1.isnull().value_counts())
# row = 0
# for i in range(0, len(EA1)):
#
#     start = 0
#     num = 0
#     for index in range(0, len(EA1[i])):
#         if '\u9fa5' > EA1[i][index] >= '\u4e00':
#             break
#         else:
#             start += 1
#     if EA1[i][index].isspace() or len(EA1[i][start:]) == 0:
#         continue
#     for indecs in range(start, len(EA1[i])):
#         if EA1[i][indecs] == ',' or EA1[i][indecs] == '，' or EA1[i][indecs] == '、':
#             sheet1.write(row, 0, EA1[i])
#             sheet1.write(row, 1, EA1[i][start:indecs])
#             start = indecs + 1
#             sheet1.write(row, 2, num)
#             row += 1
#             num += 1
#         elif indecs == len(EA1[i]) - 1:
#             sheet1.write(row, 0, EA1[i])
#             sheet1.write(row, 1, EA1[i][start:])
#             sheet1.write(row, 2, num)
#             row += 1

# ----------------------------拆AAD------------------------
# AAD = pd.read_excel('C:/Users/GUORUI/Desktop/数据清洗/公告生产地址.xlsx')
# EA2 = AAD['生产地址']
# sheet2 = EA.add_worksheet('AAD')
# print(EA2.isnull().value_counts())
# EA2 = EA2.fillna('NA')
# print(EA2.isnull().value_counts())
#
# row = 0
# for i in range(0, len(EA2)):
#
#     start = 0
#     num = 0
#     for index in range(0, len(EA2[i])):
#         if '\u9fa5' > EA2[i][index] >= '\u4e00':
#             break
#         else:
#             start += 1
#     if EA2[i][index].isspace() or len(EA2[i][start:]) == 0:
#         continue
#     for indecs in range(start, len(EA2[i])):
#         if EA2[i][indecs] == ',' or EA2[i][indecs] == '，' or EA2[i][indecs] == '、':
#             sheet2.write(row, 0, EA2[i])
#             sheet2.write(row, 1, EA2[i][start:indecs])
#             start = indecs + 1
#             sheet2.write(row, 2, num)
#             row += 1
#             num += 1
#         elif indecs == len(EA2[i]) - 1:
#             sheet2.write(row, 0, EA2[i])
#             sheet2.write(row, 1, EA2[i][start:])
#             sheet2.write(row, 2, num)
#             row += 1

# ----------------------------------拆AEA--------------------
# AEA = pd.read_excel('C:/Users/GUORUI/Desktop/数据清洗/20190426__数据清洗/20190426_公告企业地址表.xls')
# sheet3 = EA.add_worksheet('AEA')
# EA3 = AEA['公告地址信息']
# print(EA3.isnull().value_counts())
#
# row = 0
# for i in range(0, len(EA3)):
#
#     start = 0
#     num = 0
#     for index in range(0, len(EA3[i])):
#         if '\u9fa5' > EA3[i][index] >= '\u4e00':
#             break
#         else:
#             start += 1
#     if EA3[i][index].isspace() or len(EA3[i][start:]) == 0:
#         continue
#     for indecs in range(start, len(EA3[i])):
#         if EA3[i][indecs] == ',' or EA3[i][indecs] == '，' or EA3[i][indecs] == '、':
#             sheet3.write(row, 0, EA3[i])
#             sheet3.write(row, 1, EA3[i][start:indecs])
#             start = indecs + 1
#             sheet3.write(row, 2, num)
#             row += 1
#             num += 1
#         elif indecs == len(EA3[i]) - 1:
#             sheet3.write(row, 0, EA3[i])
#             sheet3.write(row, 1, EA3[i][start:])
#             sheet3.write(row, 2, num)
#             row += 1
#
# EA.close()
print('李欣沂')
