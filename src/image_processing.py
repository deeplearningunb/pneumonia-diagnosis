from __future__ import absolute_import, division, print_function, unicode_literals
from PIL import Image

import numpy as np
import tensorflow as tf


def get_label(file_path, class_names):
    # convert the path to a list of path components
    parts = tf.strings.split(file_path, '/')
    # The second to last is the class-directory
    return parts[-2] == class_names


def decode_img(img, img_width=224, img_height=224):
    print("Using default values: width {}, height {}".format(img_width, img_height))
    # convert the compressed string to a 3D uint8 tensor
    img = tf.image.decode_jpeg(img, channels=3)
    # Use `convert_image_dtype` to convert to floats in the [0,1] range.
    img = tf.image.convert_image_dtype(img, tf.float32)
    # resize the image to the desired size.
    return tf.image.resize(img, [img_width, img_height])


def process_path(file_path, class_names, img_width, img_height):
    label = get_label(file_path, class_names)
    # load the raw data from the file as a string
    img = tf.io.read_file(file_path)
    img = decode_img(img, img_width, img_height)
    return img, label


if __name__ == '__main__':
    pass
