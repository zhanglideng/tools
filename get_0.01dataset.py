import os
import shutil

path = ['/input/data/nyu/train/', '/input/data/nyu/val/']
new_path = ['/input/data/nyu/mini_train/', '/input/data/nyu/mini_val/']
for i in new_path:
    if not os.path.exists(i):
        os.makedirs(i)
for i in range(len(path)):
    data_list = os.listdir(path[i])
    length = len(data_list)
    length = length // 100
    for j in range(length):
        shutil.copy(path[i] + data_list[j], new_path[i])
    print('finish the %s copy' % i)



