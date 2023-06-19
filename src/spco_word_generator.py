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
        self.place_sentence_generator()


    # 1セル発話文から複数セル発話文に変換
    def place_sentence_generator(self):
        utterance_list = []
        with open("/root/HSR/catkin_ws/src/spco_dataset_generator/data/output/test/sentence.csv", 'r') as f:
            reader = csv.reader(f)
            list = [row for row in reader]

        for i in range(len(list)):
            r = list[i][0].replace(',', '') # コンマを削除
            s = r.replace('.', '') # ピリオドを削除
            t = s.split()
            utterance_list.append(t)



        FilePath = "/root/HSR/catkin_ws/src/spco_dataset_generator/data/output/test/sentence_spco.csv"
        with open(FilePath, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(utterance_list)

        print(utterance_list)
        for i in range(len(utterance_list)):
            path = PLACE_WORD_DATA + str(i + 1)
            if not os.path.exists(path):
                os.makedirs(path)
            for j in range(i + 1):
                with open(path + '/Otb.csv', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow(utterance_list[j])
        return




    # # ロボットの位置生成器
    # def robot_position_generator(self, num):
    #     with open(POSITION_DATA + '/pose.csv', 'a') as f:
    #         for i in range(num):
    #             #print(i)
    #             while i >= len(robot_poses):
    #                 i = i - len(robot_poses)
    #             writer = csv.writer(f)
    #             writer.writerows([robot_poses[i]])
    #     return
    #
    # # 物体の頻度数生成器
    # # 指定した物体をカウントする
    # def object_frequency_generator(self, num):
    #     word = []  # 物体を観測しない場合
    #
    #     for i in range(num):
    #         ## 物体の単語辞書
    #         with open(OBJECT_FREQUENCY_DATA + '{}_Object_W_list.csv'.format(i + 1), 'w') as f:
    #             writer = csv.writer(f, lineterminator='\n')
    #             writer.writerow(object_dictionary)
    #
    #         ## 観測した物体
    #         with open(OBJECT_FREQUENCY_DATA + '{}_Object.csv'.format(i + 1), 'a') as f:
    #             for j in range(i + 1):
    #                 writer = csv.writer(f)
    #                 writer.writerow(word)
    #
    #         # 全物体の観測
    #         if i + 1 == num:
    #             shutil.copyfile(OBJECT_FREQUENCY_DATA + '{}_Object.csv'.format(i + 1),
    #                             OBJECT_FREQUENCY_DATA + 'Object.csv')
    #
    #         ## BoO
    #         with open(OBJECT_FREQUENCY_DATA + '{}_Object_BOO.csv'.format(i + 1), 'a') as f:
    #             for j in range(i + 1):
    #                 writer = csv.writer(f)
    #                 writer.writerow([0] * len(object_dictionary))
    #     return


if __name__ == '__main__':
    spco_data_generator = SpCoDataGenerator()
