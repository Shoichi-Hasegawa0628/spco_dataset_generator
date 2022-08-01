#! /usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import subprocess
import os
import spco2_placescnn as places365
import numpy as np
import csv
from __init__ import *
from tqdm import tqdm


class ImageFeatureServer():

    def image_server(self):
        folders = os.listdir(PLACE_IMAGE_DATA)
        for i in tqdm(range(len(folders))):
            files = os.listdir(PLACE_IMAGE_DATA + "{}/".format(i + 1))
            if not os.path.exists(PLACE_IMG_PRE_DATA + "{}".format(i + 1)):
                os.makedirs(PLACE_IMG_PRE_DATA + "{}/".format(i + 1))
            for j in tqdm(range(len(files))):
                self.frame = cv2.imread(PLACE_IMAGE_DATA + "{}".format(i + 1) + "/{}.png".format(j))

                convert_img = places365.Image.fromarray(self.frame)  # convert into PIL
                input_img = places365.V(self.tf(convert_img).unsqueeze(0))
                logit = self.model.forward(input_img)
                h_x = places365.F.softmax(logit, 1).data.squeeze()

                # save image feature
                fp = open(PLACE_IMG_PRE_DATA + "{}/".format(i + 1) + 'ft_pre_{}_'.format(i + 1) + str(j + 1) + '.csv', 'a')
                h_x_numpy = h_x.to('cpu').detach().numpy().copy()
                fp.write(','.join(map(str, h_x_numpy)))
                fp.write('\n')
                fp.close()
                # print("save new feature")
                probs, idx = h_x.sort(0, True)
                probs = probs.numpy()
                idx = idx.numpy()


            # 10フレーム分の平均を取るプログラム
            if not os.path.exists(PLACE_IMG_DATA + "{}".format(i + 1)):
                os.makedirs(PLACE_IMG_DATA + "{}/".format(i + 1))
            sum = 0
            img_pre_files = os.listdir(PLACE_IMG_PRE_DATA + "{}/".format(i + 1))
            for k in range(len(img_pre_files)):
                data = np.loadtxt(PLACE_IMG_PRE_DATA + "{}/".format(i + 1) + "ft_pre_{}_{}.csv".format(i + 1, k + 1), delimiter=",")
                sum += data

                # 10フレームになったら平均化し, 平均の特徴量を保存し, sumをリセット
                if (k + 1) % 10 == 0:
                    # print("sum: {}".format(sum))
                    index = (k + 1) / 10
                    # np.savetxt(PLACE_IMG_DATA + 'ft' + str(int(index)) + '.csv', (sum/10), delimiter=",")

                    with open(PLACE_IMG_DATA + "{}/".format(i + 1) + 'ft' + str(int(index)) + '.csv', 'w') as f:
                        writer = csv.writer(f)
                        writer.writerow(sum/10)
                    sum = 0




    def load_network_model(self):
        # load the labels
        self.classes, self.labels_IO, self.labels_attribute, self.W_attribute = places365.load_labels()

        # load the model
        self.model = places365.load_model()

        # load the transformer
        self.tf = places365.returnTF()  # image transformer

        # get the softmax weight
        self.params = list(self.model.parameters())
        self.weight_softmax = self.params[-2].data.numpy()
        self.weight_softmax[self.weight_softmax < 0] = 0

        return (True)

    def __init__(self):
        self.image_save = True  # rospy.get_param('~image_save')#true

        if self.load_network_model() == False:
            print("error")

        self.frame = []
        self.image_server()


if __name__ == "__main__":
    srv = ImageFeatureServer()
