import scipy.io as scio
import h5py
import numpy as np
import os
import cv2

'''        
depth_index_path = depth_path + str(i) + '.npy'
np.save(depth_index_path, depth)

dataFile = 'C://nyu_depth_v2_labeled.mat'
data = h5py.File(dataFile)
print(data)

np.concatenate((a,b),axis = 1)
'''

path = 'C:\\data\\cut_coco\\train'
save_path = 'D:\\data\\train'
image_list = os.listdir(path)
print(image_list)
count = 0
num = 0
for i in image_list:
    print(path + '\\' + i)
    image = cv2.imread(path + '\\' + i)
    image = np.expand_dims(image, axis=0)
    if count % 5000 == 0:
        data = image
    else:
        data = np.concatenate((data, image), axis=0)
    count += 1
    print("count=%d data.shape=(%d,%d,%d,%d)" % (count, data.shape[0], data.shape[1], data.shape[2], data.shape[3]))
    if count % 5000 == 0:
        np.save(path + '_' + str(count // 5000 - 1) + '.npy', data)
