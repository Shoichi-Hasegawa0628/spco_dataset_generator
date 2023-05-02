#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from __init__ import *
import csv
import os
import shutil
import sys
import roslib.packages

SPCO_DATA_PATH = str(roslib.packages.get_pkg_dir("spco_dataset_generator")) + "/data/output/test/"

place_names = ["living", "kitchen", "bedroom", "bathroom"]
PLACE_WORD_DATA = SPCO_DATA_PATH + "tmp/"

class SpCoNonWordGenerator():
    def __init__(self):
        pass

    # def place_word_generator(self, num):
    #     word = []  # 物体を観測しない場合
    #
    #     for i in range(num):
    #         path = PLACE_WORD_DATA + str(i + 1)
    #         if not os.path.exists(path):
    #             os.makedirs(path)
    #         with open(path + '/Otb.csv', 'a') as f:
    #             for j in range(i + 1):
    #                 writer = csv.writer(f)
    #                 writer.writerow(word)
    #     return

    # # 1ステップづつ交互に
    # def place_word_generator(self, num):
    #     for i in range(num):
    #         path = PLACE_WORD_DATA + str(i + 1)
    #         if not os.path.exists(path):
    #             os.makedirs(path)
    #         fp = open(path + '/Otb.csv', 'a')
    #         for j in range(i + 1):
    #             while j >= len(place_names):
    #                 j = j - len(place_names)
    #             fp.write(place_names[j])
    #             fp.write('\n')
    #         fp.close()
    #     return

    # # living30, kitchen30, bedroom30, bathroom30を挿入する
    # def place_word_generator(self, num):
    #     place_list = []
    #     for i in range(num):
    #         path = PLACE_WORD_DATA + str(i + 1)
    #         if not os.path.exists(path):
    #             os.makedirs(path)
    #
    #         if 0 < i + 1 <= 30:
    #             place_list.append([place_names[0]])
    #
    #         elif 30 < i + 1 <= 60:
    #             place_list.append([place_names[1]])
    #
    #         elif 60 < i + 1 <= 90:
    #             place_list.append([place_names[2]])
    #
    #         else:
    #             place_list.append([place_names[3]])
    #
    #         # CSVファイルに書き込む
    #         with open(path + '/Otb.csv', 'w', newline='') as f:
    #             writer = csv.writer(f)
    #             for row in place_list:
    #                 writer.writerow(row)
    #
    #     return

    # 追加学習 # 孤立語バージョン
    # def place_word_generator(self, num):
    #     place_list = []
    #     for i in range(num):
    #         path = PLACE_WORD_DATA + str(i + 1)
    #         if not os.path.exists(path):
    #             os.makedirs(path)
    #
    #         if 0 < i + 1 <= 30:
    #             place_list.append([place_names[0]])
    #
    #         elif 30 < i + 1 <= 60:
    #             place_list.append([place_names[1]])
    #
    #         elif 60 < i + 1 <= 90:
    #             place_list.append([place_names[2]])
    #
    #         elif 90 < i + 1 <= 120:
    #             place_list.append([place_names[3]])
    #
    #         else:
    #             word = []  # 物体を観測しない場合
    #             place_list.append(word)
    #             # CSVファイルに書き込む
    #             with open(path + '/Otb.csv', 'w', newline='') as f:
    #                 writer = csv.writer(f)
    #                 for row in place_list:
    #                     writer.writerow(row)
    #
    #
    #     return

    # 追加学習 # 文章バージョン
    def place_word_generator(self, num):
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

        word = []  # 物体を観測しない場合
        lists = len(utterance_list)
        for i in range(num):
            utterance_list.append(word)
            path = PLACE_WORD_DATA + str(i + 1 + lists)
            if not os.path.exists(path):
                os.makedirs(path)

            # CSVファイルに書き込む
            with open(path + '/Otb.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                for row in utterance_list:
                    writer.writerow(row)


        return

if __name__ == '__main__':
    spco_non_word_generator = SpCoNonWordGenerator()
    arg1 = int(sys.argv[1])
    spco_non_word_generator.place_word_generator(arg1)
