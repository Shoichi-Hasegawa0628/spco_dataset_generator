#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __init__ import *
import csv
import os
import shutil


class SpCoDataGenerator():
    def __init__(self):
        self.set_param()

    def set_param(self):
        get_key = input("Please input the number of data\n")
        print("The number of data is {}\n".format(get_key))
        self.place_word_generator(int(get_key))
        self.robot_position_generator(int(get_key))
        self.object_frequency_generator(int(get_key))

    # 場所の単語生成器
    def place_word_generator(self, num):
        for i in range(num):
            path = PLACE_WORD_DATA + str(i + 1)
            if not os.path.exists(path):
                os.makedirs(path)
            fp = open(path + '/Otb.csv', 'a')
            for j in range(i + 1):
                while j >= len(place_names):
                    j = j - len(place_names)
                fp.write(place_names[j])
                fp.write('\n')
            fp.close()
        return

    # ロボットの位置生成器
    def robot_position_generator(self, num):
        with open(POSITION_DATA + '/pose.csv', 'a') as f:
            for i in range(num):
                #print(i)
                while i >= len(robot_poses):
                    i = i - len(robot_poses)
                writer = csv.writer(f)
                writer.writerows([robot_poses[i]])
        return

    # 物体の頻度数生成器
    def object_frequency_generator(self, num):
        word = []  # 物体を観測しない場合

        for i in range(num):
            ## 物体の単語辞書
            with open(OBJECT_FREQUENCY_DATA + '{}_Object_W_list.csv'.format(i + 1), 'w') as f:
                writer = csv.writer(f, lineterminator='\n')
                writer.writerow(object_dictionary)

            ## 観測した物体
            with open(OBJECT_FREQUENCY_DATA + '{}_Object.csv'.format(i + 1), 'a') as f:
                for j in range(i + 1):
                    writer = csv.writer(f)
                    writer.writerow(word)

            # 全物体の観測
            if i + 1 == num:
                shutil.copyfile(OBJECT_FREQUENCY_DATA + '{}_Object.csv'.format(i + 1),
                                OBJECT_FREQUENCY_DATA + 'Object.csv')

            ## BoO
            with open(OBJECT_FREQUENCY_DATA + '{}_Object_BOO.csv'.format(i + 1), 'a') as f:
                for j in range(i + 1):
                    writer = csv.writer(f)
                    writer.writerow([0] * len(object_dictionary))
        return


if __name__ == '__main__':
    spco_data_generator = SpCoDataGenerator()
