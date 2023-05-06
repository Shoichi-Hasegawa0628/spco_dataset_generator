#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from problog.program import PrologString
from problog import get_evaluatable
import os
import csv

path = "/root/HSR/catkin_ws/src/spco_dataset_generator/data"

class LogicalInferenceDataGenerator():
    def __init__(self):
        pass

    def generator(self):
        object_list = self.read_data()
        # object_list = ['plate', 'bowl', 'pitcher_base', 'cracker_box', 'pudding_box','chips_bag', 'coffee', 'muscat', 'fruits_juice', 'pig_doll','sheep_doll', 'penguin_doll', 'treatments', 'sponge', 'bath_slipper']

        for l in range(len(object_list)):
            # 推論モデルの読み込み
            object_name = object_list[l]
            TXT_DATA = path + "/commonsense/logical_inference.txt"
            f = open(TXT_DATA, 'r')
            reasoning_data = f.readlines()
            Query = "query(exist({}, Y)).\n".format(object_name)
            reasoning_data.append(Query)
            reasoning_data = '\n'.join(reasoning_data)

            # 論理推論の実行
            p = PrologString(reasoning_data)

            # 推論結果の出力
            result = get_evaluatable().create_from(p).evaluate()
            # print("ProbLog result of reasoning\n")
            print(result)
            # print("****************************************************************\n")

            # 推論した場所の単語と確率を辞書型に格納
            pre_prob = list(result.values())  # 場所の確率

            place_name_list = ["living", "kitchen", "bedroom", "bathroom"]
            place_name_probs = [0, 0, 0, 0]
            count = 0  # 場所の単語 (場所の単語が最高で7文字なのでこのコードで動作可能)
            ct = 1
            for key in result.keys():
                key_goal = len(str(key))
                # place_name = str(key)[key_goal - 7: key_goal - 1]
                if ct == 1:
                    place_name = str(key)[key_goal - 7: key_goal - 1]
                elif ct == 2:
                    place_name = str(key)[key_goal - 8: key_goal - 1]
                elif ct == 3:
                    place_name = str(key)[key_goal - 8: key_goal - 1]
                else:
                    place_name = str(key)[key_goal - 9: key_goal - 1]
                # elif ct == 5:
                #     place_name = str(key)[key_goal - 9: key_goal - 1]
                # else:
                #     place_name = str(key)[key_goal - 11: key_goal - 1]
                print(place_name)
                # ct += 1

                if place_name.find(',') is not None:
                    place_name = place_name[place_name.find(',') + 1:]

                j = place_name_list.index(place_name)
                place_name_probs[j] = pre_prob[count]
                count += 1
                ct += 1

            # print(place_name_probs)
            place_name_probs = [float(i) / sum(place_name_probs) for i in place_name_probs]  # 正規化
            print(place_name_probs)

            # SpCoSLAM側の単語の辞書に合わせる処理
            with open(
                    path + '/spco/W_list.csv',
                    'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    pass
                place_name_list_s = row
            place_name_list_s.pop(-1)
            place_name_list_s = [a for a in place_name_list_s if a != '']

            problog_probs_r = [0 for i in range(len(place_name_list_s))]  # 場所概念の単語数に合わせた表現 (Prior)
            for j in range(len(place_name_list_s)):
                if ((place_name_list_s[j] in place_name_list) == True):
                    a = place_name_list.index(place_name_list_s[j])
                    problog_probs_r[j] = place_name_probs[a]
                else:
                    problog_probs_r[j] = 0

            # self.save_data(place_name_probs)
            self.save_data(problog_probs_r, object_name)



    def save_data(self, prob, object_name):
        # 推論結果をtxtでまとめて保存
        FilePath = path + "/result/logical_inference_result/{}".format(object_name)
        if not os.path.exists(FilePath):
            os.makedirs(FilePath)

        # csvファイルで1行目に保存
        with open(FilePath + "/logical_inference_result.csv", 'w') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerow(prob)

    def read_data(self):
        # 物体の単語辞書
        with open(path + '/Object_W_list.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                pass
            object_name_list = row

        return object_name_list

if __name__ == '__main__':
    logical_generator = LogicalInferenceDataGenerator()
    logical_generator.generator()
