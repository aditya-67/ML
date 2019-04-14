import numpy as np
import tflearn
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
import tensorflow as tf
import os

lr = 1e-3
img_size = 100
MODEL_NAME_SIX = 'dogsvscats-model-6-conv'.format(lr,'6conv-CNN')

def init():
	tf.reset_default_graph()
	convnet = input_data(shape=[None, img_size, img_size, 1], name='input')

	convnet = conv_2d(convnet, 32, 2, activation='relu')
	convnet = max_pool_2d(convnet, 2)

	convnet = conv_2d(convnet, 64, 2, activation='relu')
	convnet = max_pool_2d(convnet, 2)

	convnet = conv_2d(convnet, 32, 2, activation='relu')
	convnet = max_pool_2d(convnet, 2)

	convnet = conv_2d(convnet, 64, 2, activation='relu')
	convnet = max_pool_2d(convnet, 2)

	convnet = conv_2d(convnet, 32, 2, activation='relu')
	convnet = max_pool_2d(convnet, 2)

	convnet = conv_2d(convnet, 64, 2, activation='relu')
	convnet = max_pool_2d(convnet, 2)

	convnet = fully_connected(convnet, 1024, activation='relu')
	convnet = dropout(convnet, 0.8)

	convnet = fully_connected(convnet, 2, activation='softmax')
	convnet = regression(convnet, optimizer='adam', learning_rate=lr, loss='categorical_crossentropy', name='targets')

	model = tflearn.DNN(convnet)

	if os.path.exists('{}.meta'.format(MODEL_NAME_SIX)):
		model.load(MODEL_NAME_SIX)
		print('model loaded!')

	graph = tf.get_default_graph()

	return model,graph