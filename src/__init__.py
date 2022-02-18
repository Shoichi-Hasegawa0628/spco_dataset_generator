#!/usr/bin/env python
# -*- coding: utf-8 -*-
import roslib.packages

SPCO_DATA_PATH = str(roslib.packages.get_pkg_dir("spco_dataset_generator")) + "/data/output/test/"

PLACE_IMG_DATA = SPCO_DATA_PATH + "img/"
PLACE_WORD_DATA = SPCO_DATA_PATH + "tmp/"
POSITION_DATA = SPCO_DATA_PATH
OBJECT_FREQUENCY_DATA = SPCO_DATA_PATH + "tmp_boo/"

place_names = ["living", "bedroom", "kitchen"]
robot_poses = [[0, 0], [1, 1], [2, 2]]