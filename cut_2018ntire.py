path = ['/input/data/ntire_2018/hazy/', '/input/data/ntire_2018/GT/']
cut_path = ['/input/data/cut_ntire_2018/hazy/', '/input/data/cut_ntire_2018/GT/']
'''
01_indoor_GT.jpg
01_indoor_hazy.jpg

01_outdoor_GT.jpg
01_outdoor_hazy.jpg
624 464 
400*400
'''
for i in range(len(path)):
    if not os.path.exists(cut_path[i]):
        os.makedirs(cut_path[i])
    data_list = os.listdir(path[i])
    data_list.sort(key=lambda x: int(x[:2]))
