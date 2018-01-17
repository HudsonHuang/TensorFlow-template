﻿"""
Function of main.py:

config loader
hprams loader
feature extraction
Call model training and validation
Model Save and Load
Call model validation

载入训练参数
载入指定模型超参数
调用特征提取
调用模型训练和验证
模型保存与载入
调用模型验证
"""

"""A very simple MNIST classifier.
See extensive documentation at
https://www.tensorflow.org/get_started/mnist/beginners
usage: main.py [options] 
options:
    --data_dir=<dir>            Where to get training data [default: ./datasets/MNIST/].
    --base_log_dir=<dir>        Where to save models [default: ./generated/logdir/].
    --model                     Which model to use [default: autoencoder_vae].
    --experiment_name           Name of experiment defines the log path [default: Date-of-now].
    --total_epoch               Max num of training epochs [default: by the model].
    --eval_per_epoch            Model eval per n epoch [default: by the model].
    --save_per_epoch            Model save per n epoch [default: by the model].
    --batch_size                Batch size [default: by the model].
    -h, --help                  Show this help message and exit
"""

import argparse
import sys
import datetime
from tqdm import tqdm
import numpy as np
import os

import tensorflow as tf

from models.model_example import model_example
from models.deep_mnist import deep_mnist
from models.VAE.autoencoder_vae import autoencoder

from preprocessing_util import autoencoder_vae_add_noise
import params 

FLAGS = None

def prepare_params():
    if FLAGS.experiment_name == "default":
        now=datetime.datetime.now()
        FLAGS.experiment_name=now.strftime('%Y%m%d%H%M%S')
    FLAGS.log_dir = FLAGS.base_log_dir+FLAGS.experiment_name+'_'+FLAGS.model+'/'


def main():
    #Avoid tensorboard error on IPython
    tf.reset_default_graph()
    
    # Prepare data
    train_data =  np.load(os.path.join(FLAGS.data_dir, 'train_data.npy'))
    train_labels =  np.load(os.path.join(FLAGS.data_dir, 'train_labels.npy'))
    test_data =  np.load(os.path.join(FLAGS.data_dir, 'test_data.npy'))
    test_labels =  np.load(os.path.join(FLAGS.data_dir, 'test_labels.npy'))
    
    train_set = tf.data.Dataset.from_tensor_slices((train_data, train_labels))
    test_set = tf.data.Dataset.from_tensor_slices((test_data, test_labels))
    
    if FLAGS.model == "autoencoder_vae":
        train_set = train_set.map(autoencoder_vae_add_noise)
        test_set = test_set.map(autoencoder_vae_add_noise)
    
    train_set = train_set.batch(FLAGS.batch_size).repeat(10)
    test_set = test_set.batch(FLAGS.batch_size).repeat(10)
    
    trainIter = train_set.make_initializable_iterator()
    next_examples, next_labels = trainIter.get_next()
    
    testIter = test_set.make_initializable_iterator()
    test_examples, text_labels = testIter.get_next()
    
    # Create the model
    if FLAGS.model == "MLP":
        hp = params.MLP_model_params
        x = tf.placeholder(tf.float32, [None, hp.input_dim])
        y = tf.placeholder(tf.float32, [None, hp.output_dim])
        model = model_example(hp,x ,y)
        
        train_feed_dict={x: batch_xs, y: batch_ys}
        test_feed_dict={x: batch_xs, y: batch_ys}
        train_fetch_list = [model.train_step,model.merged]
        test_fetch_list = [model.accuracy,model.merged]
        
    if FLAGS.model == "Deep_mnist":
        hp = params.Deep_MNIST_model_params
        
        x = tf.placeholder(tf.float32, [None, hp.input_dim])
        y = tf.placeholder(tf.float32, [None, hp.output_dim])
        keep_probe = tf.placeholder(tf.float32)
        
        model = deep_mnist(hp, x ,y, keep_probe)
        
        train_fetch_list = [model.train_step,model.merged]
        test_fetch_list = [model.accuracy,model.merged]
        
    if FLAGS.model == "autoencoder_vae":
        hp = params.autoencoder_vae_model_params
        
        x = tf.placeholder(tf.float32, [None, hp.input_dim])
        x_hat = tf.placeholder(tf.float32, [None, hp.input_dim])
        keep_probe = tf.placeholder(tf.float32)
        
        model = autoencoder(hp, x ,x_hat, keep_probe)
        
        y=x_hat
        train_fetch_list = [model.train_step,model.merged]
        test_fetch_list = [model.loss_mean,model.merged]
    
    #Prepare tensorboard
    merged = tf.summary.merge_all()
    train_writer = tf.summary.FileWriter(FLAGS.log_dir+'/train',model.train_step.graph)
    test_writer = tf.summary.FileWriter(FLAGS.log_dir+'/test')
    print('checkout result with "tensorboard --logdir={}"'.format(FLAGS.log_dir))
    
    
    session_conf = tf.ConfigProto(
        gpu_options=tf.GPUOptions(
            allow_growth=True,
        ),
    )

    #Start tf session
    with tf.Session(config=session_conf) as sess:
        sess.run(tf.global_variables_initializer())
        sess.run(trainIter.initializer)
        sess.run(testIter.initializer)
      
        for epoch in tqdm(range(FLAGS.total_epoch)):
            batch_xs, batch_ys = sess.run([next_examples, next_labels])
            train_feed_dict={x: batch_xs,
                       y: batch_ys,
                       keep_probe: hp.keep_probe}
            _,summary = sess.run(train_fetch_list, feed_dict=train_feed_dict)
            train_writer.add_summary(summary, epoch)
        
            if epoch % FLAGS.eval_per_epoch == 0:
                batch_xs, batch_ys = sess.run([test_examples, text_labels])
                test_feed_dict={x: batch_xs,
                               y: batch_ys,
                               keep_probe: hp.keep_probe_test}
                mertics,summary = sess.run(test_fetch_list, feed_dict=test_feed_dict)
                test_writer.add_summary(summary, epoch)
                
            if epoch % FLAGS.save_per_epoch == 0:
                tf.train.Saver().save(sess, '{}/epoch_{}'.format(FLAGS.log_dir, epoch))

  
if __name__ == '__main__':
    default_hp=params.default_hyper_params
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', type=str, default="./datasets/MNIST/")
    parser.add_argument('--experiment_name', type=str, default="default")
    parser.add_argument('--base_log_dir', type=str, default="./generated/logdir/")
    parser.add_argument('--model', type=str, default="autoencoder_vae")
    parser.add_argument('--total_epoch', type=int, default=default_hp.num_epochs)
    parser.add_argument('--eval_per_epoch', type=int, default=default_hp.eval_per_epoch)
    parser.add_argument('--save_per_epoch', type=int, default=default_hp.save_per_epoch)
    parser.add_argument('--batch_size', type=int, default=default_hp.batch_size)
    FLAGS, unparsed = parser.parse_known_args()
    prepare_params()
    main()