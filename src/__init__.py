#!/usr/bin/env python
# -*- coding: utf-8 -*-
import roslib.packages

SPCO_DATA_PATH = str(roslib.packages.get_pkg_dir("spco_dataset_generator")) + "/data/output/test/"

PLACE_IMAGE_DATA = SPCO_DATA_PATH + "image/"
PLACE_IMG_DATA = SPCO_DATA_PATH + "img/"
PLACE_WORD_DATA = SPCO_DATA_PATH + "tmp/"
POSITION_DATA = SPCO_DATA_PATH
OBJECT_FREQUENCY_DATA = SPCO_DATA_PATH + "tmp_boo/"

place_names = ["living", "bedroom", "kitchen"]
robot_poses = [[0, 0], [1, 1], [2, 2]]
object_dictionary = ["plate", "bowl", "pitcher_base", "banana",
                      "apple", "orange", "cracker_box", "pudding_box",
                      "chips_bag", "coffee", "muscat", "fruits_juice",
                      "pig_doll", "sheep_doll", "penguin_doll", "airplane_toy",
                      "car_toy", "truck_toy", "tooth_paste", "towel",
                      "cup", "treatments", "sponge", "bath_slipper"]