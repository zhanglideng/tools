import cv2
import os

path = ['/input/data/nyu/gth/',
        '/input/data/nyu/test/',
        '/input/data/nyu/test_visual/',
        '/input/data/nyu/train/',
        '/input/data/nyu/val/']
new_path = ['/input/data/nyu/cut_gth/',
            '/input/data/nyu/cut_test/',
            '/input/data/nyu/cut_test_visual/',
            '/input/data/nyu/cut_train/',
            '/input/data/nyu/cut_val/']
count = 0

for i in range(len(path)):
    if not os.path.exists(new_path[i]):
        os.makedirs(new_path[i])
    data_list = os.listdir(path[i])
    for j in data_list:
        count = count + 1
        if count % 500 == 0:
            print('count=' + str(count))
        image = cv2.imread(path[i] + j)
        # print(image.shape)
        # if image.shape[0] >= 400 and image.shape[1] >= 400:
        image = image[8:632, 8:472]
        print(image.shape)
        print(new_path[i] + j)
        cv2.imwrite(new_path[i] + j, image)
