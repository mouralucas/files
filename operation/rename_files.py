import os
from hashlib import md5
# from scipy.misc import imread, imresize, imshow
# import matplotlib.pyplot as plt
# import matplotlib.gridspec as gridspec
# # %matplotlib inline
# import time
# import numpy as np


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