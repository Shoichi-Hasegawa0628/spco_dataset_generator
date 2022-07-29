#! /usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import os
import shutil
from __init__ import *
import csv


# folders = os.listdir(PLACE_IMG_PRE_DATA)

## 特徴量
# for i in range(len(folders)):
#     csv_files = os.listdir(PLACE_IMG_PRE_DATA + "{}/".format(i + 1))
#     for j in range(len(csv_files)):
#         shutil.copyfile(PLACE_IMG_PRE_DATA + "{}/".format(i + 1) + "ft{}.csv".format(j + 1),
#                         PLACE_IMG_DATA + "ft{}.csv".format((j + 1) + 6*i + 36)) # 0, 18, 36を後ろに書く

## 画像
# for i in range(len(folders)):
#     img_files = os.listdir(PLACE_IMG_PRE_DATA + "{}/".format(i + 1))
#     for j in range(len(img_files)):
#         shutil.copyfile(PLACE_IMG_PRE_DATA + "{}/".format(i + 1) + "{}.png".format(j),
#                         PLACE_IMG_DATA + "{}.png".format((j + 1) + 60*i + 360)) # 0, 180, 360を後ろに書く


folders = os.listdir(OBJECT_PRE_FREQUENCY_DATA)

for i in range(len(folders)):
    csv_files = os.listdir(OBJECT_PRE_FREQUENCY_DATA + "{}/".format(i + 1))
    for j in range(len(csv_files)):
        shutil.copyfile(OBJECT_PRE_FREQUENCY_DATA + "{}/".format(i + 1) + "{}_Object_BOO.csv".format(j + 1),
                        OBJECT_FREQUENCY_DATA + "{}_Object_BOO.csv".format((j + 1) + 6*i + 36)) # 0, 18, 36


# with open("/root/HSR/catkin_ws/src/spco_dataset_generator/data/output/test/sentence.csv", 'r') as f:
#     reader = csv.reader(f)
#     object_list = [row for row in reader]
# print(object_list)

# # 教示ごとの物体の辞書を保存
# FilePath = OBJECT_FREQUENCY_DATA + "Object_W_list.csv"
# with open(FilePath, 'w') as f:
#     writer = csv.writer(f, lineterminator='\n')
#     writer.writerow(object_dictionary)





