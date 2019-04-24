#!/usr/bin/env python3

import os
from PIL import Image

def rotate(image_path, degrees_to_rotate, save_location):
    image_obj = Image.open(image_path)
    rotated_image = image_obj.rotate(degrees_to_rotate)
    rotated_image.save(save_location)

dir_str = 'up'
directory = os.fsencode(dir_str)
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    img_path = dir_str + '/' + filename

    # make left images (90 deg)
    left_path = 'left/Left' + filename
    rotate(img_path, 90, left_path)

    # make right images (270 deg)
    right_path = 'right/Right' + filename
    rotate(img_path, 270, right_path)
