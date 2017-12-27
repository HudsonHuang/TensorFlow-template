﻿"""
Function of main.py:

config loader
json loader

Call feature extraction
Call model training and validation
Model Save and Load
Call model validation

载入训练参数
载入指定模型超参数的json

调用特征提取
调用模型训练和验证
模型保存与载入
调用模型验证

This example was modified from official site of Tensorflow.
"""
"""A very simple MNIST classifier.
See extensive documentation at
https://www.tensorflow.org/get_started/mnist/beginners
"""
#from __future__ import absolute_import
#from __future__ import division
#from __future__ import print_function

import argparse
import sys
import datetime

from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf

from models.model_example import model_example
import params 

#debug
import sys

def print_all(module_):
  modulelist = dir(module_)
  length = len(modulelist)
  for i in range(0,length,1):
    print(getattr(module_,modulelist[i]))


FLAGS = None
#arch = 1

def prepare_params():
  if FLAGS.experiment_name == "default":
      now=datetime.datetime.now()
      FLAGS.experiment_name=now.strftime('%Y%m%d%H%M%S')
  FLAGS.log_dir = FLAGS.base_log_dir+FLAGS.experiment_name+'/'


def main():
  
  # params
  prepare_params()
    
  # Prepare data
  mnist = input_data.read_data_sets(FLAGS.data_dir, one_hot=True)
  
  # Create the model
  if FLAGS.arch_name == "MLP":
      model = model_example(params.MLP_model_params)

  #Make tf.summary for tensorboard
  merged = tf.summary.merge_all()
  train_writer = tf.summary.FileWriter(FLAGS.log_dir,model.train_step.graph)  

  #Start tf session
  sess = tf.InteractiveSession()
  tf.global_variables_initializer().run()
  
  
  # Train
  for epoch in range(FLAGS.total_epoch):
    batch_xs, batch_ys = mnist.train.next_batch(FLAGS.batch_size)
    summary = sess.run(model.train_step, feed_dict={model.x: batch_xs, model.y_: batch_ys})
    
    # Log
#    train_writer.add_summary(summary, steps)
    
    # Evaluate model
    if epoch % FLAGS.eval_per_epoch == 0:
          correct_prediction = tf.equal(tf.argmax(model.y, 1), tf.argmax(model.y_, 1))
          accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
          print(sess.run(accuracy, feed_dict={model.x: mnist.test.images,
                                              model.y_: mnist.test.labels}))
    
    # Save model
    if epoch % FLAGS.save_per_epoch == 0:
                tf.train.Saver().save(sess, '{}/epoch_{}'.format(FLAGS.log_dir, epoch))
   
  print('checkout result with "tensorboard --logdir={}"'.format(FLAGS.log_dir))
  
  
if __name__ == '__main__':
  default_hp=params.default_hyper_params
  parser = argparse.ArgumentParser()
  parser.add_argument('--data_dir', type=str, default="./datasets/MNIST_data/")
  parser.add_argument('--experiment_name', type=str, default="default")
  parser.add_argument('--base_log_dir', type=str, default="./generated/logdir/")
  parser.add_argument('--arch_name', type=str, default="MLP")
  parser.add_argument('--total_epoch', type=int, default=default_hp.num_epochs)
  parser.add_argument('--eval_per_epoch', type=int, default=default_hp.eval_per_epoch)
  parser.add_argument('--save_per_epoch', type=int, default=default_hp.save_per_epoch)
  parser.add_argument('--batch_size', type=int, default=default_hp.batch_size)
  FLAGS, unparsed = parser.parse_known_args()
  main()
#  tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)