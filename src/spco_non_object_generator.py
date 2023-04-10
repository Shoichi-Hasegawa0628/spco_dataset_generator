#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __init__ import *
import csv
import os
import shutil


class SpCoNonObjectGenerator():
    def __init__(self):
        self.object_frequency_generator(120)

    # 物体の頻度数生成器
    def object_frequency_generator(self, num):

        for i in range(num):
            ## BoO
            with open(OBJECT_FREQUENCY_DATA + '{}_Object_BOO.csv'.format(i + 1), 'w') as f:
                writer = csv.writer(f)
                writer.writerow([0] * 16) # JCMSI用
        return


if __name__ == '__main__':
    spco_data_generator = SpCoNonObjectGenerator()
