from matplotlib import pyplot as plt

import numpy as np
import os
import tensorflow as tf
import json

from .res.slim.nets import inception
from .res.slim.preprocessing import inception_preprocessing
from django.conf import settings

checkpoints_dir = settings.BASE_DIR+"/api/res/train_inception_v1_eye256_logs"
label_dir = settings.BASE_DIR+"/api/res/eye256_photos"

def evaluate(name):
    
    slim = tf.contrib.slim

    image_size = inception.inception_v1.default_image_size    
 
    with tf.Graph().as_default():
        
        image_input = tf.read_file(settings.BASE_DIR+"/media/"+name+"/"+name+"_2.jpg")
        image = tf.image.decode_jpeg(image_input, channels=3)
        processed_image = inception_preprocessing.preprocess_image(image,
                                                            image_size,
                                                            image_size,
                                                            is_training=False)
        processed_images  = tf.expand_dims(processed_image, 0)
        
        with slim.arg_scope(inception.inception_v1_arg_scope()):
            logits, _ = inception.inception_v1(processed_images, num_classes=11, is_training=False)
        probabilities = tf.nn.softmax(logits)
        
        init_fn = slim.assign_from_checkpoint_fn(
            os.path.join(checkpoints_dir, 'model.ckpt-19725'),
            slim.get_model_variables('InceptionV1'))
        
        with tf.Session() as sess:
            init_fn(sess)
            np_image, probabilities = sess.run([image, probabilities])
            probabilities = probabilities[0, 0:]
            sorted_inds = [i[0] for i in sorted(enumerate(-probabilities), key=lambda x:x[1])]
            
        #names = os.listdir("C:\\Users\\multicampus\\Desktop\\project\\s1p2151002\\Back\\Detector\\api\\res\\eye256_photos")
        names = os.listdir(label_dir)

        index = sorted_inds[0]
        data = [names[index], round(probabilities[index],2)]
        
    return data

