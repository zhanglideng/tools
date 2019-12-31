#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#写一个给数据集划分为训练集,验证集,测试集的code

import os,shutil

data_path='./haze/'#数据集的目录

train_path='/input/ednet/dehaze_data/train/'
validation_path='/input/ednet/dehaze_data/validation/'
test_path='/input/ednet/dehaze_data/test/'
if not os.path.isdir(train_path):
	os.makedirs(train_path)
if not os.path.isdir(validation_path):
	os.makedirs(validation_path)
if not os.path.isdir(test_path):
	os.makedirs(test_path)

train=0.8
validation=0.1
test=0.1
data=os.listdir(data_path)
data.sort(key = lambda x: int(x[:-30]))
print(data)
length=len(data)

print('length:'+str(length))

train_size=train*length
validation_size=validation*length
test_size=test*length
print('train_size:'+str(train_size))
print('validation_size:'+str(validation_size))
print('test_size:'+str(test_size))
train_count = 0
validation_count = 0
test_count = 0
for i in range(length):
	if i % 1000 == 0:
		print(i)
	if i < train_size:
		shutil.copy(data_path+data[i], train_path)
		train_count += 1
	elif i < train_size + validation_size:
		shutil.copy(data_path+data[i], validation_path)
		validation_count += 1
	else:
		shutil.copy(data_path+data[i], test_path)
		test_count += 1
print('train_count' + str(train_count))
print('validation_count' + str(validation_count))
print('test_count' + str(test_count))