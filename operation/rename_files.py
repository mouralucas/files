import os
from hashlib import md5
import exifread

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
    try:
        with open(filepath, 'rb') as file:
            return md5(file.read()).hexdigest()
    except FileNotFoundError:
        print(f"Error: File not found - {filepath}")
    except Exception as e:
        print(f"An error occurred: {e}")


def read_metadata(file_path):
    # Open the image file for reading in binary mode
    with open(file_path, 'rb') as f:
        # Read the metadata using exifread
        tags = exifread.process_file(f)

    # Extract and return the relevant metadata
    metadata = {
        'Origin': tags.get('Image Make', None),  # Extracting origin information
        'GPS': {
            'Latitude': tags.get('GPS GPSLatitude', None),
            'Longitude': tags.get('GPS GPSLongitude', None),
        }
    }
    return metadata
