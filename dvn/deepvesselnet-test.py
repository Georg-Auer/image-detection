# git clone https://github.com/giesekow/deepvesselnet.git
#tf_upgrade_v2.py --intree ~/code/old --outtree ~/code/new

# pip install --upgrade keras
# pip install --upgrade numpy
# pip install --upgrade sklearn
# pip install --upgrade tensorflow

# pip install --upgrade SimpleITK

# install as described
# https://github.com/giesekow/deepvesselnet

from dvn import FCN
import numpy as np
import dvn.misc as ms
import dvn.losses as ls

# import tensorflow.compat.v1 as tf
# tf.disable_v2_behavior() 

dim = 2
net = FCN(cross_hair=True, dim=dim)
net.compile(loss=ls.weighted_categorical_crossentropy_with_fpr())
N = (10, 1,) +(64,)*dim
X = np.random.random(N)
Y = np.random.randint(2, size=N)
Y = np.squeeze(Y)
Y = ms.to_one_hot(Y)
Y = np.transpose(Y, axes=[0,dim+1] + list(range(1,dim+1)))
print('Testing FCN Network')
print('Data Information => ', 'volume size:', X.shape, ' labels:',np.unique(Y))
net.fit(x=X, y=Y, epochs=30, batch_size=2, shuffle=True)
