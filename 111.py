#!/usr/bin/python
# -*- coding: <encoding name> -*-
import numpy
import pandas as pd

read = pd.read_excel('C:/Users/GUORUI/Desktop/zzz新建文件夹/全.xlsx')
a1 = read[['yuan','chai','indecs']]
a1.to_excel('C:/Users/GUORUI/Desktop/zzz新建文件夹/yuanchai.xlsx')
a2 = read[['chai','gui']]
a2 = a2.drop_duplicates()
a2.to_excel('C:/Users/GUORUI/Desktop/zzz新建文件夹/chaigui.xlsx')
print('0')