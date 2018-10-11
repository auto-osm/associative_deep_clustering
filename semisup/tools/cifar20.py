from __future__ import division
from __future__ import print_function

import os
from semisup.tools import data_dirs
from six.moves import cPickle
import sys
import numpy as np

# this file is based on mnist.py

DATADIR = data_dirs.cifar20
NUM_LABELS = 20
IMAGE_SHAPE = [32, 32, 3]

def get_data(name):
  # get all (images, labels)
  if name == 'train' or name == 'unlabeled':
    images, labels = extract_cifar(os.path.join(DATADIR, "train"),
                         label_key="coarse_labels")
  elif name == 'test':
    images, labels = extract_cifar(os.path.join(DATADIR, "test"),
                         label_key="coarse_labels")

  print(images.__class__)
  print(images.shape)
  print(labels.__class__)
  print(labels.shape)
  print(images.min())
  print(images.max())
  print(labels.min())
  print(labels.max())
  exit(1)
  return images, labels

def extract_cifar(path, label_key):
  # https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/keras/datasets/cifar.py

  with open(path, 'rb') as f:
      if sys.version_info < (3,):
          d = cPickle.load(f)
      else:
          d = cPickle.load(f, encoding='bytes')
          # decode utf8
          d_decoded = {}
          for k, v in d.items():
              d_decoded[k.decode('utf8')] = v
          d = d_decoded
  data = d['data']
  labels = d[label_key]

  data = data.reshape(data.shape[0], 3, 32, 32)
  data = data.transpose(0, 2, 3, 1) # channels last like in mnist.py
  labels = np.array(labels)
  return data, labels

# Dataset specific augmentation parameters.
augmentation_params = dict()
augmentation_params['max_crop_percentage'] = 0.2
augmentation_params['brightness_max_delta'] = 0.5
augmentation_params['noise_std'] = 0.05
augmentation_params['flip'] = True # our change
augmentation_params['max_rotate_angle'] = 15
