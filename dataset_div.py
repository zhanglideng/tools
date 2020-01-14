#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 写一个给数据集划分为训练集,验证集,测试集的code
import os
import shutil

data_path = '/input/data/cut_ntire_2018/hazy/'  # 数据集的目录

train_path = '/input/data/ntire_2018/train/'
val_path = '/input/data/ntire_2018/val/'
test_path = '/input/data/ntire_2018/test/'
if not os.path.isdir(train_path):
    os.makedirs(train_path)
if not os.path.isdir(val_path):
    os.makedirs(val_path)
if not os.path.isdir(test_path):
    os.makedirs(test_path)

train = 0.8
validation = 0.1
test = 0.1
data = os.listdir(data_path)
data.sort(key=lambda x: int(x[:-4]))
print(data)
length = len(data)

print('length:' + str(length))

train_size = train * length
validation_size = validation * length
test_size = test * length
print('train_size:' + str(train_size))
print('validation_size:' + str(validation_size))
print('test_size:' + str(test_size))
train_count = 0
validation_count = 0
test_count = 0
for i in range(length):
    if i % 1000 == 0:
        print(i)
    if i < train_size:
        shutil.copy(data_path + data[i], train_path)
        train_count += 1
    elif i < train_size + validation_size:
        shutil.copy(data_path + data[i], val_path)
        validation_count += 1
    else:
        shutil.copy(data_path + data[i], test_path)
        test_count += 1
print('train_count' + str(train_count))
print('validation_count' + str(validation_count))
print('test_count' + str(test_count))
