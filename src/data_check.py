#! /usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import os
import shutil
from __init__ import *
import csv

# path = "/root/HSR/catkin_ws/src/spco_dataset_generator/data"
#
# step = 90
# OT = []
# for s in range(step):
#     for line in open(path + "/tmp_boo/" + str(s + 1) + "_Object_BOO.csv", 'r'):
#         # for line in open( datasetfolder + datasetname + 'img/ft' + str(s+1) + '.csv', 'r'):
#         itemList = line[:].split(',')
#     OT.append([float(itemList[i]) for i in range(len(object_dictionary))])
#
# # print(OT)
# # print(len(OT))
# # print(OT[0])
# sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# for i in range(len(OT)):
#     sum = [x + y for (x, y) in zip(OT[i], sum)]
#
# print(sum)
#
# with open(path + "/Object_W_list.csv", 'r') as f:
#     reader = csv.reader(f)
#     Object_W_list = [row for row in reader]
#
# print(Object_W_list[0])


stop_words = [","]
W_list = []
a = [","]

for i in range(len(a)):
    if ((a[i] in stop_words) == True):
        print("A")
        continue
    print(a[i])

print(W_list)



# print(a[0].split(","))
