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
        # self.place_word_generator(int(get_key))
        # self.robot_position_generator(int(get_key))
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
        # 計算量を削減するためBOOを事前計算
        # 今回(IREX-Robocup-2022)は出現頻度が固定なので, 場所ごとの設定から事前に計算することができる
        boo_for_spaces = [
            [int(object in objects_in_spaces[label_spaces[i % 3]]) for object in object_dictionary]
            for i in range(3)
        ]

        for i in range(num):

            ## 物体の単語辞書
            with open(OBJECT_FREQUENCY_DATA + '{}_Object_W_list.csv'.format(i + 1), 'w') as f:
                writer = csv.writer(f, lineterminator='\n')
                writer.writerow(object_dictionary)

            ## 観測した物体
            with open(OBJECT_FREQUENCY_DATA + '{}_Object.csv'.format(i + 1), 'w') as f:
                for j in range(i + 1):
                    writer = csv.writer(f)
                    writer.writerow(objects_in_spaces[label_spaces[j % 3]])

            # 全物体の観測画像化
            ## BOO の書き出し
            with open(OBJECT_FREQUENCY_DATA + '{}_Object_BOO.csv'.format(i + 1), 'w') as f:
                for j in range(i+1):
                    writer = csv.writer(f)
                    writer.writerow(boo_for_spaces[j % 3])
        return


if __name__ == '__main__':
    ## IREX-ROBOCUP2022 に向けたデータセット読み込み用コード
    ## 各場所に対応した物体のラベルをここで明示 (IREX2022本番)
    label_spaces = ["living", "bedroom", "kitchen"]      
    objects_in_spaces = {
        label_spaces[0] : ["pudding_box", "cracker_box", "fruits_juice", "coffee"],
        label_spaces[1] : ["pig_doll" , "sheep_doll", "truck_toy", "airplane_toy", "treatments"],
        label_spaces[2] : ["plate", "banana", "orange", "towel", "pitcher_base", "bath_slipper", "cup"]
    }
    
    spco_data_generator = SpCoDataGenerator()

    # def make_object_boo(self):
    #     # print(self.object_list)
    #     self.Object_BOO = [[0 for i in range(len(object_dictionary))] for n in range(len(self.object_list))]
    #     # print(self.Object_BOO)
    #     for n in range(len(self.object_list)):
    #         for j in range(len(self.object_list[n])):
    #             for i in range(len(object_dictionary)):
    #                 if object_dictionary[i] == self.object_list[n][j]:
    #                     self.Object_BOO[n][i] = self.Object_BOO[n][i] + 1
    #     # print(self.Object_BOO)
    #     return