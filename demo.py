#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 15:04:58 2022

@author: Ahmad Darkhalil
"""
from vis_modified_all import *
import os

json_files_path = 'epick_visor/GroundTruth-SparseAnnotations/annotations/train'
output_directory ='../EPIC_DATA/segmentations_all'
output_resolution= (854,480)
is_overlay=False
rgb_frames = 'epick_visor/GroundTruth-SparseAnnotations/rgb_frames/P02'
generate_video=False
sides = ["left", "right"]
types = ["object", "hand"]

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

for side in sides:
    for type in types:
        folder_of_jsons_to_masks(json_files_path, output_directory, side, type, is_overlay=is_overlay,rgb_frames=rgb_frames,output_resolution=output_resolution,generate_video=generate_video)

folder_of_jsons_to_masks(json_files_path, output_directory, "both", "hand", is_overlay=is_overlay,rgb_frames=rgb_frames,output_resolution=output_resolution,generate_video=generate_video)


