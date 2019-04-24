#!/usr/bin/env python3

import os
from PIL import Image

def rotate(image_path, degrees_to_rotate, save_location):
    image_obj = Image.open(image_path)
    rotated_image = image_obj.rotate(degrees_to_rotate)
    rotated_image.save(save_location)

def flip_image(image_path, save_location):
    image_obj = Image.open(image_path)
    rotated_image = image_obj.transpose(Image.FLIP_LEFT_RIGHT)
    rotated_image.save(save_location)

dir_str = 'up'
directory = os.fsencode(dir_str)
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    img_path = dir_str + '/' + filename

    # for angle in range(1, 16) -> "filename-<ANGLE>.jpg"
    for angle in range(1, 16):
        new_img_path = img_path[:-4] + '-' + str(angle) + img_path[-4:]
        rotate(img_path, angle, new_img_path)

    # for angle in range(-15, 0) -> "filename-neg<ANGLE>.jpg"
    for angle in range(-15, 0):
        new_img_path = img_path[:-4] + '-neg' + str(abs(angle)) + img_path[-4:]
        rotate(img_path, angle, new_img_path)

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    img_path = dir_str + '/' + filename
    new_img_path = img_path[:-4] + '-FLIPPED' + img_path[-4:]
    flip_image(img_path, new_img_path)


