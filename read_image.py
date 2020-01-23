#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
import h5py
import os
from PIL import Image

path = '/home/aistudio/work/data/nyu/gth/'
if not os.path.isdir(path):
    os.makedirs(path)

f = h5py.File("/home/aistudio/data/data19783/nyu.mat")
images = f["images"]
images = np.array(images)
# images = images.transpose((0,1,3,2))
images_number = []
for i in range(len(images)):
    print(str(i) + '.bmp')
    images_number.append(images[i])
    a = np.array(images_number[i])
    r = Image.fromarray(a[0]).convert('L')
    g = Image.fromarray(a[1]).convert('L')
    b = Image.fromarray(a[2]).convert('L')
    img = Image.merge("RGB", (r, g, b))
    save_path = path + str(i) + '.bmp'
    img.save(save_path, optimize=True)
