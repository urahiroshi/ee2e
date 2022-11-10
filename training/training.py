#!/usr/bin/env pipenv run python

import tensorflow as tf
import numpy as np
import yaml

def separate_plus_and_minus(original):
  result = []
  for v in original:
    result.append(v if v >= 0 else 0)
  for v in original:
    result.append(0 if v >= 0 else -v)
  return result

with open('./get-training-table/table.yaml') as file:
  table = yaml.safe_load(file)
  training_inputs_good = np.array(
    [separate_plus_and_minus(row[0]) for row in table]
  ) / 1000.0
  training_inputs_bad = np.array(
    [separate_plus_and_minus(row[1]) for row in table]
  ) / 1000.0
  training_labels = np.array([[1.0, 0.0] for _ in table])

input_good = tf.keras.layers.Input(shape=(8))
input_bad = tf.keras.layers.Input(shape=(8))
shared_dence_1 = tf.keras.layers.Dense(4, activation=tf.nn.relu)
shared_dence_2 = tf.keras.layers.Dense(3, activation=tf.nn.relu)
shared_dence_out = tf.keras.layers.Dense(1, activation=tf.nn.sigmoid)

good_1 = shared_dence_1(input_good)
bad_1 = shared_dence_1(input_bad)
good_2 = shared_dence_2(good_1)
bad_2 = shared_dence_2(bad_1)
good_out = shared_dence_out(good_2)
bad_out = shared_dence_out(bad_2)

merged = tf.keras.layers.concatenate([good_out, bad_out], axis=-1)
predictions = tf.keras.layers.Dense(2, activation=tf.nn.softmax)(merged)

model = tf.keras.models.Model(inputs=[input_good, input_bad], outputs=predictions)

model.compile(
  optimizer='sgd',
  loss='binary_crossentropy',
  metrics=['accuracy']
)

model.fit([training_inputs_good, training_inputs_bad], training_labels, epochs=5)
