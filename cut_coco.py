import cv2
import os

'''
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

            /home/aistudio/work/data/coco
'''
path = ['/home/aistudio/work/data/coco/train/',
        '/home/aistudio/work/data/coco/val/',
        '/home/aistudio/work/data/coco/test/',
        '/home/aistudio/work/data/coco/unlabeled/']
new_path = ['/home/aistudio/work/data/cut_coco/train/',
            '/home/aistudio/work/data/cut_coco/val/',
            '/home/aistudio/work/data/cut_coco/test/',
            '/home/aistudio/work/data/cut_coco/unlabeled']
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
        height, width, channel = image.shape

        if image.shape[0] >= 400 and image.shape[1] >= 400:
            image = image[:400, :400]
            # image = image[:height//8*8, :width//8*8]
            print(image.shape)
            print(new_path[i] + j)
            cv2.imwrite(new_path[i] + j, image)
