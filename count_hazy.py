import os

train_path = '/input/data/nyu/train/'
val_path = '/input/data/nyu/val/'
test_path = '/input/data/nyu/test/'
path_list = [train_path, val_path, test_path]
print(path_list)

count = [0] * 12
for i in path_list:
    name_list = os.listdir(i)
    for j in name_list:
        b = float(j[-8:-4])
        # print(b)
        b = int(b * 10 - 8)
        # print(b)
        count[b] += 1
        # break
print(count)
