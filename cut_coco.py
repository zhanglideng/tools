import cv2
import os

path = 'C:\\data\\coco\\test'
new_path = 'C:\\data\\cut_coco\\test'
print(path)
print(new_path)
count = 0

data_list = os.listdir(path)
for j in data_list:
    # print(j)

    # if count % 500 == 0:
    #    print('count=' + str(count))
    print(path + '\\' + j)
    image = cv2.imread(path + '\\' + j)
    height, width, channel = image.shape

    if image.shape[0] >= 400 and image.shape[1] >= 400:
        image = image[:400, :400]
        count = count + 1
        # image = image[:height//8*8, :width//8*8]
        # print(image.shape)
        # print(new_path + '\\' + j)
        cv2.imwrite(new_path + '\\' + j, image)

print(count)
