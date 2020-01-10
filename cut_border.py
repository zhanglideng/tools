import cv2
import os

"""
最终运行得到
高最小值为624 （640，8-632）
宽最小值为464 （480，8-472）
"""

path = '/input/data/nyu/gth/'
image_list = os.listdir(path)
num = len(image_list)

n = 10
min_height = 99999
min_width = 99999
for name in image_list:
    image = cv2.imread(path + name)
    flag = True
    while flag:
        flag = False
        height, width, channel = image.shape
        # print(height)
        # print(width)
        for i in range(height - n):
            # print(i)
            if (image[i:i + n, 0, :] == 255).all() or (image[i:i + n, width - 1, :] == 255).all():
                image = image[:, 1:width - 1, :]
                flag = True
                break
        for i in range(width - n):
            # print(i)
            if (image[0, i:i + n, :] == 255).all() or (image[height - 1, i:i + n, :] == 255).all():
                image = image[1:height - 1, :, :]
                flag = True
                break
    print(image.shape)
    min_height = min_height if height > min_height else height
    min_width = min_width if width > min_width else width
print(min_height)
print(min_width)



