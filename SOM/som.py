from __future__ import absolute_import, division, print_function, unicode_literals

import numpy as np         
import pandas as pd 
import cv2                 
import os          
import skimage as sk       
import scipy
import skimage 
import random
import os
import pathlib
import tensorflow as tf
import IPython.display as display
import numpy as np
import matplotlib.pyplot as plt
import cv2

from minisom import MiniSom
from random import shuffle
from tqdm import tqdm  
from skimage.transform import resize
from scipy import ndarray
from skimage import transform
from skimage import util
from PIL import Image
from tensorflow.keras.preprocessing.image import ImageDataGenerator

print(tf.__version__)


# Create variables with path
TRAIN_PATH = pathlib.Path('./chest_xray/train/')
TEST_PATH = pathlib.Path('./chest_xray/test/')
VAL_PATH = pathlib.Path('./chest_xray/val')

train_count = len(list(TRAIN_PATH.glob('*/*.jpeg')))
test_count = len(list(TEST_PATH.glob('*/*.jpeg')))
val_count = len(list(VAL_PATH.glob('*/*.jpeg')))
train_count, test_count, val_count

normal_files = list(TRAIN_PATH.glob('NORMAL/*'))
pneumonia_files = list(TRAIN_PATH.glob('PNEUMONIA/*'))

normal_img = cv2.imread(str(normal_files[2]))
pneumonia_img = cv2.imread(str(pneumonia_files[2]))

CLASS_NAMES = np.array([item.name for item in TRAIN_PATH.glob('*')])
CLASS_NAMES

def get_label(file_path):
    # convert the path to a list of path components
    parts = tf.strings.split(file_path, '/')
    # The second to last is the class-directory
    return parts[-2] == CLASS_NAMES

def decode_img(img):
    # convert the compressed string to a 3D uint8 tensor
    img = tf.image.decode_jpeg(img, channels=3)
    # Use `convert_image_dtype` to convert to floats in the [0,1] range.
    img = tf.image.convert_image_dtype(img, tf.float32)
    # resize the image to the desired size.
    return tf.image.resize(img, [IMG_WIDTH, IMG_HEIGHT])

def process_path(file_path):
    label = get_label(file_path)
    # load the raw data from the file as a string
    img = tf.io.read_file(file_path)
    img = decode_img(img)
    return img, label

def show_batch(image_batch, label_batch):
    plt.figure(figsize=(10,10))
    for n in range(25):
        ax = plt.subplot(5,5,n+1)
        plt.imshow(image_batch[n])
        plt.title(CLASS_NAMES[label_batch[n]==1][0].title())
        plt.axis('off')

"""## Data generators"""

def train_generator(image_size, batch_size=32):
    datagen = ImageDataGenerator(
            rescale=1./255,
            rotation_range=8,
            width_shift_range=25,
            height_shift_range=25,
            zoom_range=(0.95, 1.1),
            brightness_range=(0.8,1.2),
            shear_range=10,
            fill_mode = "constant",
            horizontal_flip=True,
            vertical_flip=False,
            cval=0
        )
    data_generator = datagen.flow_from_directory(
        TRAIN_PATH,
        target_size=(image_size, image_size),
        batch_size=batch_size,
        class_mode='binary'
        )
    return data_generator

def validation_generator(image_size, batch_size=32):
    datagen = ImageDataGenerator(rescale=1./255)
    data_generator = datagen.flow_from_directory(
        VAL_PATH,
        target_size=(image_size, image_size),
        batch_size=batch_size,
        class_mode='binary'
        )
    return data_generator

def test_generator(image_size, batch_size=32, shuffle=False):
    datagen = ImageDataGenerator(rescale=1./255)
    data_generator = datagen.flow_from_directory(
        TEST_PATH,
        target_size=(image_size, image_size),
        batch_size=batch_size,
        shuffle=shuffle,
        class_mode='binary'
        )
    return data_generator

IMG_HEIGHT = 224
IMG_WIDTH = 224

train_data_generator = train_generator(IMG_HEIGHT)
test_data_generator = test_generator(IMG_HEIGHT)
val_data_generator = validation_generator(IMG_HEIGHT)

som = MiniSom(2, 2, 2, sigma=1,
              learning_rate=0.2, 
              neighborhood_function='triangle')


print("Setting weights")
som.pca_weights_init(tf.convert_to_tensor(train_data_generator))

# som.random_weights_init(pixels)

# som.pca_weights_init(train_data_generator)
print("Training...")
som.train_random(tf.convert_to_tensor(train_data_generator), 200, verbose=True)  # random training
print("\n...ready!")
