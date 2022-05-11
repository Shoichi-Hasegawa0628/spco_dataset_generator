#! /usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import os
import shutil
from __init__ import *
import csv


# folders = os.listdir(PLACE_IMG_PRE_DATA)

# for i in range(len(folders)):
#     csv_files = os.listdir(PLACE_IMG_PRE_DATA + "{}/".format(i + 1))
#     for j in range(len(csv_files)):
#         shutil.copyfile(PLACE_IMG_PRE_DATA + "{}/".format(i + 1) + "ft{}.csv".format(j + 1),
#                         PLACE_IMG_DATA + "ft{}.csv".format((j + 1) + 6*i + 150)) # 0, 30, 60, 90, 120, 150

# for i in range(len(folders)):
#     img_files = os.listdir(PLACE_IMG_PRE_DATA + "{}/".format(i + 1))
#     for j in range(len(img_files)):
#         shutil.copyfile(PLACE_IMG_PRE_DATA + "{}/".format(i + 1) + "{}.png".format(j),
#                         PLACE_IMG_DATA + "{}.png".format((j + 1) + 6*i + 0)) # 0, 30, 60, 90, 120, 150


# folders = os.listdir(OBJECT_PRE_FREQUENCY_DATA)
#
# for i in range(len(folders)):
#     csv_files = os.listdir(OBJECT_PRE_FREQUENCY_DATA + "{}/".format(i + 1))
#     for j in range(len(csv_files)):
#         shutil.copyfile(OBJECT_PRE_FREQUENCY_DATA + "{}/".format(i + 1) + "{}_Object_BOO.csv".format(j + 1),
#                         OBJECT_FREQUENCY_DATA + "{}_Object_BOO.csv".format((j + 1) + 6*i + 150)) # 0, 30, 60, 90, 120, 150


# with open("/root/HSR/catkin_ws/src/spco_dataset_generator/data/output/test/sentence.csv", 'r') as f:
#     reader = csv.reader(f)
#     object_list = [row for row in reader]
# print(object_list)

# # 教示ごとの物体の辞書を保存
# FilePath = OBJECT_FREQUENCY_DATA + "Object_W_list.csv"
# with open(FilePath, 'w') as f:
#     writer = csv.writer(f, lineterminator='\n')
#     writer.writerow(object_dictionary)







