#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Standard Library
from __future__ import unicode_literals
import codecs
import cv2
from cv_bridge import CvBridge, CvBridgeError
import os
import csv

# Third Party
import numpy as np
import rospy
import actionlib
# from sensor_msgs.msg import CompressedImage
# import yolo_ros_msgs.msg as yolo_ros_msgs
import yolov5_ros_msgs.msg as yolov5_ros_msgs
# from yolo_ros_msgs.msg import BoundingBoxes, BoundingBox
from tqdm import tqdm

# Self Modules
from __init__ import *

# from rgiro_spco2_slam.srv import spco_data_object, spco_data_objectResponse


class ObjectFeatureServer():
    def __init__(self):
        self.detect_object_info = []
        self.detect_image = 0
        self.object_list = []
        self.Object_BOO = []
        self.cv_bridge = CvBridge()
        self.frame = 0

        self.client = actionlib.SimpleActionClient("/yolov5_ros/action/detection", yolov5_ros_msgs.DetectionAction)
        self.client.wait_for_server()

        rospy.loginfo("[Service spco_data/object] Ready")

        folders = os.listdir(PLACE_IMAGE_DATA)
        for i in tqdm(range(len(folders))):
            files = os.listdir(PLACE_IMAGE_DATA + "{}/".format(i + 1))
            if not os.path.exists(OBJECT_PRE_FREQUENCY_DATA + "{}/".format(i + 1)):
                os.makedirs(OBJECT_PRE_FREQUENCY_DATA + "{}/".format(i + 1))
            # print(len(files))
            for j in tqdm(range(len(files))):
                self.frame = cv2.imread(PLACE_IMAGE_DATA + "{}/".format(i + 1) + "{}.png".format(j))
                raw_img = self.cv_bridge.cv2_to_compressed_imgmsg(self.frame)
                self.object_server(j + 1, i + 1, raw_img)
        self.averaging_ten_frames()



    def object_server(self, step, folder_index, image):
        # if (os.path.exists(SPCO_DATA_PATH + "/tmp_boo/Object.csv") == True):
        #     with open(SPCO_DATA_PATH + "/tmp_boo/Object.csv", 'r') as f:
        #         reader = csv.reader(f)
        #         self.object_list = [row for row in reader]
            # print("pre_object_list: {}\n".format(self.object_list))

        goal = yolov5_ros_msgs.DetectionGoal(0, image)
        self.client.send_goal_and_wait(goal)
        result = self.client.get_result()

        self.detect_object_info = result.boxes.boxes
        # self.detect_image = result.detect_image
        # print(type(self.detect_object_info))

        if len(self.detect_object_info) == 0:
            # 最初の教示で物体が検出されなかったとき
            self.object_list = [[]]
            self.Object_BOO = [[0] * len(object_dictionary)]
            # self.taking_single_image(trialname, req.step)
            self.save_data(step, folder_index)
            self.object_list = []
            self.Object_BOO = []
            # return spco_data_objectResponse(True)
            return

            # else:
            #     # 最初の教示以降の教示で物体が検出されなかったとき
            #     object_list = []
            #     self.object_list.append(object_list)
            #     self.make_object_boo()
            #     # self.taking_single_image(trialname, req.step)
            #     self.save_data(step, folder_index)
            #     # return spco_data_objectResponse(True)
            #     return

        # self.save_detection_img(step, folder_index, self.detect_image)
        self.extracting_label()
        self.make_object_boo()
        # self.taking_single_image(trialname, req.step)
        self.save_data(step, folder_index)
        self.object_list = []
        self.Object_BOO = []
        # print("object_list: {}\n".format(self.object_list))
        # print("dictionary: {}\n".format(object_dictionary))
        # print("Bag-of-Objects: {}\n".format(self.Object_BOO))
        # return spco_data_objectResponse(True)
        return

    def extracting_label(self):
        object_list = []
        for i in range(len(self.detect_object_info)):
            object_list.append(self.detect_object_info[i].name)
            # print(object_list)
        self.object_list.append(object_list)
        # print(self.object_list)
        return

    def make_object_boo(self):
        # print(self.object_list)
        self.Object_BOO = [[0 for i in range(len(object_dictionary))] for n in range(len(self.object_list))]
        # print(self.Object_BOO)
        for n in range(len(self.object_list)):
            for j in range(len(self.object_list[n])):
                for i in range(len(object_dictionary)):
                    if object_dictionary[i] == self.object_list[n][j]:
                        self.Object_BOO[n][i] = self.Object_BOO[n][i] + 1
        # print(self.Object_BOO)
        return

    # def taking_single_image(self, trialname, step):
    #     img = rospy.wait_for_message('/hsrb/head_rgbd_sensor/rgb/image_rect_color/compressed', CompressedImage,
    #                                  timeout=None)
    #     observed_img = self.cv_bridge.compressed_imgmsg_to_cv2(img)
    #     cv2.imwrite(datafolder + trialname + "/object_image/" + str(step) + ".jpg", observed_img)
    #     return

    def save_detection_img(self, step, folder_index, image):
        # img = rospy.wait_for_message('/yolov5_ros/output/image/compressed', CompressedImage, timeout=15)
        detect_img = self.cv_bridge.compressed_imgmsg_to_cv2(image)
        if not os.path.exists(SPCO_DATA_PATH + "/detect_image/" + "{}/".format(folder_index)):
            os.makedirs(SPCO_DATA_PATH + "/detect_image/" + "{}/".format(folder_index))
        cv2.imwrite(SPCO_DATA_PATH + "/detect_image/" + "{}/".format(folder_index) + str(step) + ".png", detect_img)
        return

    def save_data(self, step, folder_index):
        # 全時刻の観測された物体のリストを保存
        # FilePath = OBJECT_FREQUENCY_DATA + "{}/".format(folder_index) + "Object.csv"
        # with open(FilePath, 'w') as f:
        #     writer = csv.writer(f)
        #     writer.writerows(self.object_list)

        # 教示ごとに観測された物体のリストを保存
        # FilePath = OBJECT_FREQUENCY_DATA + "{}/".format(folder_index) + str(step) + "_Object.csv"
        # with open(FilePath, 'w') as f:
        #     writer = csv.writer(f)
        #     writer.writerows(self.object_list)

        # 教示ごとのBag-Of-Objects特徴量を保存
        FilePath = OBJECT_PRE_FREQUENCY_DATA + "{}/".format(folder_index) + str(step) + "_Object_BOO.csv"
        with open(FilePath, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(self.Object_BOO)

        # 教示ごとの物体の辞書を保存
        # FilePath = OBJECT_FREQUENCY_DATA + "{}/".format(folder_index) + str(step) + "_Object_W_list.csv"
        # with open(FilePath, 'w') as f:
        #     writer = csv.writer(f, lineterminator='\n')
        #     writer.writerow(object_dictionary)
        # return

    def averaging_ten_frames(self):
        # 10フレーム分の平均を取るプログラム
        folders = os.listdir(OBJECT_PRE_FREQUENCY_DATA)
        # print(len(folders))
        sum = 0
        for i in range(len(folders)):
            if not os.path.exists(OBJECT_FREQUENCY_DATA + "{}".format(i + 1)):
                os.makedirs(OBJECT_FREQUENCY_DATA + "{}/".format(i + 1))
            obj_pre_files = os.listdir(OBJECT_PRE_FREQUENCY_DATA + "{}/".format(i + 1))
            # print(len(obj_pre_files))
            for k in range(len(obj_pre_files)):
                data = np.loadtxt(OBJECT_PRE_FREQUENCY_DATA + "{}/".format(i + 1) + "{}_Object_BOO.csv".format(i + 1, k + 1),
                                  delimiter=",")
                sum += data

                # 10フレームになったら平均化し, 平均の特徴量を保存し, sumをリセット
                if (k + 1) % 10 == 0:
                    # print("sum: {}".format(sum))
                    index = (k + 1) / 10
                    # np.savetxt(PLACE_IMG_DATA + 'ft' + str(int(index)) + '.csv', (sum/10), delimiter=",")
                    ave = sum / 10
                    print(ave)
                    ave_true = [int(i) for i in ave]
                    # print(ave_true)
                    with open(OBJECT_FREQUENCY_DATA + "{}/".format(i + 1) + "{}_Object_BOO.csv".format(int(index)), 'w') as f:
                        writer = csv.writer(f)
                        writer.writerow(ave_true)
                    sum = 0



if __name__ == '__main__':
    rospy.init_node('spco2_object_features', anonymous=False)
    srv = ObjectFeatureServer()
    # rospy.spin()
