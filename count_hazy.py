import os

path = '/input/data/shallow_nyu/'
path_list = os.listdir(path)
print(path_list)

count = [0] * 12
for i in path_list:
    a = path + i
    name_list = os.listdir(a)
    for j in name_list:
        b = int(float(j[-8:-4]) * 10 - 5)
        print(b)
        count[b] += 1
print(count)
