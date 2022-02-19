#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import shutil
import numpy as np

word = []
for i in range(80):
    FilePath = '/root/HSR/tmp/Otb_{}.csv'.format(i)
    with open(FilePath, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(word)
    shutil.copyfile('/root/HSR/tmp/Otb_{}.csv'.format(i), '/root/HSR/tmp/Otb_{}.csv'.format(i+1))