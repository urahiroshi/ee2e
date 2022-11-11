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

def get_formatted_data(file_path):
  with open(file_path) as file:
    table = yaml.safe_load(file)
    good = np.array(
      [separate_plus_and_minus(row[0]) for row in table]
    ) / 2000.0
    bad = np.array(
      [separate_plus_and_minus(row[1]) for row in table]
    ) / 2000.0
    good_bad = np.concatenate([good, bad])
    bad_good = np.concatenate([bad, good])
    labels = np.concatenate([
      np.array([[1.0, 0.0] for _ in table]),
      np.array([[0.0, 1.0] for _ in table]),
    ])
    return [good_bad, bad_good, labels]

training_good_bad, training_bad_good, training_labels = get_formatted_data(
  './get-training-table/table.yaml'
)
input_good_bad = tf.keras.layers.Input(shape=(8))
input_bad_good = tf.keras.layers.Input(shape=(8))
shared_dence_1 = tf.keras.layers.Dense(4, activation=tf.nn.relu)
# shared_dence_2 = tf.keras.layers.Dense(2, activation=tf.nn.relu)
shared_dence_out = tf.keras.layers.Dense(1, activation=tf.nn.sigmoid)

good_bad_1 = shared_dence_1(input_good_bad)
bad_good_1 = shared_dence_1(input_bad_good)
# good_bad_2 = shared_dence_2(good_bad_1)
# bad_good_2 = shared_dence_2(bad_good_1)
good_bad_out = shared_dence_out(good_bad_1)
bad_good_out = shared_dence_out(bad_good_1)

merged = tf.keras.layers.concatenate([good_bad_out, bad_good_out], axis=-1)
predictions = tf.keras.layers.Dense(2, activation=tf.nn.softmax, use_bias=False)(merged)

model = tf.keras.models.Model(inputs=[input_good_bad, input_bad_good], outputs=predictions)

model.compile(
  optimizer=tf.keras.optimizers.Adam(learning_rate=0.01),
  loss='binary_crossentropy',
  metrics=['accuracy']
)

model.fit([training_good_bad, training_bad_good], training_labels, epochs=300)

test_good_bad, test_bad_good, test_labels = get_formatted_data(
  './get-test-table/test-table.yaml'
)
model.evaluate([test_good_bad, test_bad_good], test_labels)
