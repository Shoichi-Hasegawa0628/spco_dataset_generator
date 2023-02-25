#! /usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import os
import shutil
from __init__ import *
import csv

# 教示ごとの物体の辞書を保存
FilePath = SPCO_DATA_PATH + "/Object_W_list.csv"
with open(FilePath, 'w') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(object_dictionary)
