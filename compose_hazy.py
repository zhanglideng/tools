#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
import h5py
import os
from PIL import Image
import sys
import math
import random
import cv2
import gc

train_path = '/input/data/nyu/train/'
val_path = '/input/data/nyu/val/'
test_path = '/input/data/nyu/test/'


def Guidedfilter(im, p, r, eps):
    mean_I = cv2.boxFilter(im, cv2.CV_64F, (r, r))
    mean_p = cv2.boxFilter(p, cv2.CV_64F, (r, r))
    mean_Ip = cv2.boxFilter(im * p, cv2.CV_64F, (r, r))
    cov_Ip = mean_Ip - mean_I * mean_p
    mean_II = cv2.boxFilter(im * im, cv2.CV_64F, (r, r))
    var_I = mean_II - mean_I * mean_I
    a = cov_Ip / (var_I + eps)
    b = mean_p - a * mean_I
    mean_a = cv2.boxFilter(a, cv2.CV_64F, (r, r))
    mean_b = cv2.boxFilter(b, cv2.CV_64F, (r, r))
    q = mean_a * im + mean_b
    return q


if __name__ == '__main__':
    sigma = 1  # 高斯噪声的方差
    color_shift = 0 # 合成无偏差的有雾图
    haze_num = 20  # 无雾图生成几张有雾图
    f = h5py.File('/input/data/nyu/nyu_depth_v2_labeled.mat')
    '''
    depth_path = '/input/data/nyu/depth/'
    if not os.path.exists(depth_path):
        os.makedirs(depth_path)
    '''
    depths = f['depths']
    images = f['images']
    print(depths.shape)
    print(images.shape)
    depths = np.array(depths)
    # m = depths.max()
    # depths = depths / m
    images = np.array(images)
    length = depths.shape[0]
    for i in range(length):
        if i < length * 0.8 - 1:
            path = train_path
        elif i <= length * 0.9 - 1:
            path = val_path
        else:
            path = test_path
        if not os.path.exists(path):
            os.makedirs(path)
        depth = depths[i]
        m = depth.max()
        depth = depth / m
        image = images[i]
        print('dealing:' + str(i) + '.png')
        image_gray = image[0] * 0.299 + image[1] * 0.587 + image[2] * 0.114
        depth = Guidedfilter(image_gray, depth, 14, 0.0001)
        # depth_index_path = depth_path + str(i) + '.npy'
        # np.save(depth_index_path, depth)
        for rand in range(haze_num):
            image_out = np.zeros((3, depth.shape[0], depth.shape[1]))
            noise = np.random.randn(depth.shape[0], depth.shape[1]) * sigma
            fog_A = round(random.uniform(0.5 + color_shift, 1 - color_shift), 2)
            fog_A_R = round(fog_A + random.uniform(-1, 1) * color_shift, 2)
            fog_A_G = round(fog_A + random.uniform(-1, 1) * color_shift, 2)
            fog_A_B = round(fog_A + random.uniform(-1, 1) * color_shift, 2)
            fog_density = round(random.uniform(0.8, 2.0), 2)
            t = np.exp(-1 * fog_density * depth)
            image_out[0] = image[0] * t + 255 * fog_A_R * (1 - t) + noise
            image_out[1] = image[1] * t + 255 * fog_A_G * (1 - t) + noise
            image_out[2] = image[2] * t + 255 * fog_A_B * (1 - t) + noise
            image_path = path + str(
                i) + '_a=[' + '%.02f' % fog_A_R + ',' + '%.02f' % fog_A_G + ',' + '%.02f' % fog_A_B + ']_b=' + '%.02f' % fog_density + '.png'
            image_out = np.swapaxes(image_out, 0, 2)
            image_out = np.swapaxes(image_out, 0, 1)
            image_out = Image.fromarray(image_out.astype('uint8')).convert('RGB')
            image_out.save(image_path, 'PNG', optimize=True)
