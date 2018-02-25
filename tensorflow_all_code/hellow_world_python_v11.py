from __future__ import division, print_function, absolute_import

import tflearn

# Residual blocks
# 32 layers: n=5, 56 layers: n=9, 110 layers: n=18
n = 5

# Data loading
from tflearn.datasets import cifar10
(X, Y), (testX, testY) = cifar10.load_data()
Y = tflearn.data_utils.to_categorical(Y, 10)
testY = tflearn.data_utils.to_categorical(testY, 10)

# Real-time data preprocessing
img_prep = tflearn.ImagePreprocessing()
img_prep.add_featurewise_zero_center(per_channel=True)

# Real-time data augmentation
img_aug = tflearn.ImageAugmentation()
img_aug.add_random_flip_leftright()
img_aug.add_random_crop([32, 32], padding=4)

# Building Residual Network
net = tflearn.input_data(shape=[None, 32, 32, 3], data_preprocessing=img_prep, data_augmentation=img_aug)
net = tflearn.conv_2d(net, 16, 3, regularizer='L2', weight_decay=0.0001)
net = tflearn.residual_block(net, n, 16)
net = tflearn.residual_block(net, 1, 32, downsample=True)
net = tflearn.residual_block(net, n-1, 32)
net = tflearn.residual_block(net, 1, 64, downsample=True)
net = tflearn.residual_block(net, n-1, 64)
net = tflearn.batch_normalization(net)
net = tflearn.activation(net, 'relu')
net = tflearn.global_avg_pool(net)# Regression
net = tflearn.fully_connected(net, 10, activation='softmax')
mom = tflearn.Momentum(0.1, lr_decay=0.1, decay_step=32000, staircase=True)
net = tflearn.regression(net, optimizer=mom,
loss='categorical_crossentropy')# Training
model = tflearn.DNN(net, checkpoint_path='model_resnet_cifar10', max_checkpoints=10, tensorboard_verbose=0, clip_gradients=0.)

model.fit(X, Y, n_epoch=200, validation_set=(testX, testY), snapshot_epoch=False, snapshot_step=500, show_metric=True, batch_size=128, shuffle=True, run_id='resnet_cifar10')
###其中，residual_block实现了shortcut，代码写的十分棒：

def residual_block(incoming, nb_blocks, out_channels, downsample=False, downsample_strides=2, activation='relu', batch_norm=True, bias=True, weights_init='variance_scaling', bias_init='zeros', regularizer='L2', weight_decay=0.0001, trainable=True, restore=True, reuse=False, scope=None, name="ResidualBlock"):
    """
    Residual Block.
    A residual block as described in MSRA's Deep Residual Network paper. Full pre-activation architecture is used here.
    Input: 4-D Tensor [batch, height, width, in_channels].
    Output: 4-D Tensor [batch, new height, new width, nb_filter].
    Arguments: incoming: `Tensor`. Incoming 4-D Layer. nb_blocks: `int`. Number of layer blocks. out_channels: `int`. The number of convolutional filters of the convolution layers. downsample: `bool`. If True, apply downsampling using 'downsample_strides' for strides. downsample_strides: `int`. The strides to use when downsampling. activation: `str` (name) or `function` (returning a `Tensor`). Activation applied to this layer (see tflearn.activations). Default: 'linear'. batch_norm: `bool`. If True, apply batch normalization. bias: `bool`. If True, a bias is used. weights_init: `str` (name) or `Tensor`. Weights initialization. (see tflearn.initializations) Default: 'uniform_scaling'. bias_init: `str` (name) or `tf.Tensor`. Bias initialization. (see tflearn.initializations) Default: 'zeros'. regularizer: `str` (name) or `Tensor`. Add a regularizer to this layer weights (see tflearn.regularizers). Default: None. weight_decay: `float`. Regularizer decay parameter. Default: 0.001. trainable: `bool`. If True, weights will be trainable. restore: `bool`. If True, this layer weights will be restored when loading a model. reuse: `bool`. If True and 'scope' is provided, this layer variables will be reused (shared). scope: `str`. Define this layer scope (optional). A scope can be used to share variables between layers. Note that scope will override name. name: A name for this layer (optional). Default: 'ShallowBottleneck'.
    References: - Deep Residual Learning for Image Recognition. Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun. 2015. - Identity Mappings in Deep Residual Networks. Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun. 2015.
    Links: - [http://arxiv.org/pdf/1512.03385v1.pdf] (http://arxiv.org/pdf/1512.03385v1.pdf) - [Identity Mappings in Deep Residual Networks] (https://arxiv.org/pdf/1603.05027v2.pdf)
    """
    resnet = incoming
    in_channels = incoming.get_shape().as_list()[-1]
    with tf.variable_op_scope([incoming], scope, name, reuse=reuse) as scope:
        name = scope.name #TODO
        for i in range(nb_blocks):
            identity = resnet
            if not downsample:
                downsample_strides = 1
            if batch_norm:
                resnet = tflearn.batch_normalization(resnet)
            resnet = tflearn.activation(resnet, activation)
            resnet = conv_2d(resnet, out_channels, 3, downsample_strides, 'same', 'linear', bias, weights_init, bias_init, regularizer, weight_decay, trainable, restore)
            if batch_norm:
                resnet = tflearn.batch_normalization(resnet)
            resnet = tflearn.activation(resnet, activation)
            resnet = conv_2d(resnet, out_channels, 3, 1, 'same', 'linear', bias, weights_init, bias_init, regularizer, weight_decay, trainable, restore)

            # Downsampling
            if downsample_strides > 1:
                identity = tflearn.avg_pool_2d(identity, 1,downsample_strides)

            # Projection to new dimension
            if in_channels != out_channels:
                ch = (out_channels - in_channels)//2
                identity = tf.pad(identity,[[0, 0], [0, 0], [0, 0], [ch, ch]])
                in_channels = out_channels

            resnet = resnet + identity

    return resnet
