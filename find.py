from hashlib import md5
from scipy.misc import imread, imresize, imshow
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
# %matplotlib inline
import time
import numpy as np
import os


def list_content(filepath):
    with os.scandir(filepath) as entries:
        for entry in entries:
            print(entry)


def create_hash(filepath):
    """
    Create a MD5 hash from file
    :param filepath:
    :return: MD% hash
    """
    with open(filepath, 'rb') as file:
        return md5(file.read()).hexdigest()

def read_metadata(filepath):
    pass


os.chdir(r'C:\Users\lucas\Desktop\img_test')
list_content(os.getcwd())

# print('\n')
#
# file_list = os.listdir()
# for i in file_list:
#     print(i)
#
# duplicate = []
# for i in file_list:
#     filehash = create_hash(i)
#     # print('Hash:', filehash)
#     if filehash not in duplicate:
#         duplicate.append(filehash)
#
# print('\n')
# for d in duplicate:
#     print(d)

# duplicates = []
# duplicates_names = []
# hash_keys = dict()
# for index, filename in enumerate(file_list):
#     if os.path.isfile(filename):
#         with open(filename, 'rb') as f:
#             filehash = md5(f.read()).hexdigest()
#         if filehash not in hash_keys:
#             hash_keys[filehash] = index
#         else:
#             duplicates.append((index, hash_keys[filehash]))
#             duplicates_names.append((index, filename))


# for file_indexes in duplicates:
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
