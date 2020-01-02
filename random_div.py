#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 写一个给数据集划分为训练集,验证集,测试集的code

import os
import shutil

data_path = './data'  # 数据集的目录

train_path = 'train'
val_path = 'val'
test_path = 'test'
if not os.path.isdir(train_path):
    os.makedirs(train_path)
if not os.path.isdir(val_path):
    os.makedirs(val_path)
if not os.path.isdir(test_path):
    os.makedirs(test_path)

train = 0.8
val = 0.1
test = 0.1
data = os.listdir(data_path)
length = len(data)
print('length' + str(length))

train_size = train * length
val_size = val * length
test_size = test * length
print('train_size' + str(train_size))
print('val_size' + str(val_size))
print('test_size' + str(test_size))
train_count = 0
val_count = 0
test_count = 0
for i in range(length):
    if i < train_size:
        shutil.copy('./data/' + data[i], './train/')
        train_count += 1
    elif i < train_size + val_size:
        shutil.copy('./data/' + data[i], './val/')
        val_count += 1
    else:
        shutil.copy('./data/' + data[i], './test/')
        test_count = +1
print('train_count' + str(train_count))
print('val_count' + str(val_count))
print('test_count' + str(test_count))
