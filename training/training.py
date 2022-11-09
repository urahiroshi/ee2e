#!/usr/bin/env pipenv run python

import tensorflow as tf
import numpy as np
import yaml

with open('./get-training-table/table.yaml') as file:
  table = yaml.safe_load(file)
  training_inputs = np.array([row[:-1] for row in table]) / 1000.0
  training_outputs = np.array([row[-1] for row in table])

model = tf.keras.models.Sequential([
  tf.keras.layers.Dense(4, activation=tf.nn.relu),
  tf.keras.layers.Dense(2, activation=tf.nn.softmax),
])

model.compile(
  optimizer='sgd',
  loss='binary_crossentropy',
  metrics=['accuracy']
)

model.fit(training_inputs, training_outputs, epochs=5)
