import os

path = '/data/nyu/shallow_nyu/'
path_list = os.listdir(path)
print(path_list)

for i in path_list:
    a = path + i
    name_list = os.listdir(a)
    for j in name_list:
        b = float(j[-8:-4])
