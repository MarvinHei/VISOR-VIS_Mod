#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 15:04:58 2022

@author: Ahmad Darkhalil
"""
from vis_modified import *
import os

json_files_path = 'epick_visor/GroundTruth-SparseAnnotations/annotations/train'
output_directory ='../EPIC_DATA/segmentations'
output_resolution= (854,480)
is_overlay=False
rgb_frames = 'epick_visor/GroundTruth-SparseAnnotations/rgb_frames/P02'
generate_video=False
side = "left"
type = "object"

folder_of_jsons_to_masks(json_files_path, output_directory, side, type, is_overlay=is_overlay,rgb_frames=rgb_frames,output_resolution=output_resolution,generate_video=generate_video)
