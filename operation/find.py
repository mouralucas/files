# from hashlib import md5
# from scipy.misc import imread, imresize, imshow
# import matplotlib.pyplot as plt
# import matplotlib.gridspec as gridspec
# # %matplotlib inline
# import time
# import numpy as np
from open_files import list_files, listdir, list_files_recursive
from rename_files import create_hash
import os

# os.chdir(r'D:\System\Documents\mega\Imagens\Eu, Família e Amigos')
os.chdir(r'D:\System\Documents\mega\Imagens\Eu, Família e Amigos\2019')
# os.chdir(r'D:\System\Documents\mega\Imagens\Tatuagens')
# os.chdir(r'C:\Users\lucas\Desktop\img_test')
file_list, directories = list_files_recursive(os.getcwd())

# os.chdir(r'C:\Users\lucas\Desktop\img_test')
# list_content(os.getcwd())

# print('\n')
#
# file_list = os.listdir()
# for i in file_list:
#     print(i)
#


duplicate = {}
for i in file_list:
    filehash = create_hash(i)
    print('Hash:', filehash)
    if filehash not in duplicate:
        duplicate[filehash] = [i]
    else:
        duplicate[filehash].append(i)


file = open('Itens duplicados.txt', 'w')
# print('\n')
for d in duplicate:
    if len(duplicate[d]) > 1:
        file.write('\n')
        for i in duplicate[d]:
            file.write(i + '\n')
            print(i)
        print('\n')
file.close()

# for file_indexes in duplicate:
#     try:
#
#         plt.subplot(121), plt.imshow(imread(file_list[file_indexes[1]]))
#         plt.title(file_indexes[1]), plt.xticks([]), plt.yticks([])
#
#         plt.subplot(122), plt.imshow(imread(file_list[file_indexes[0]]))
#         plt.title(str(file_indexes[0]) + ' duplicate'), plt.xticks([]), plt.yticks([])
#         plt.show()
#
#     except OSError as e:
#         continue
