import os
import shutil

path = ['/input/data/nyu/transmission/']
l = 22

for i in range(len(path)):
    data_list = os.listdir(path[i])
    length = len(data_list)
    for j in range(length):
        name = '0' * (l - len(data_list[j])) + data_list[j]
        shutil.move(path[i] + data_list[j], path[i] + name)
