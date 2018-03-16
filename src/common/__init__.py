from constants import *
from resnet import *
from util import *

# limit memory usage
import tensorflow as tf
from keras.backend.tensorflow_backend import set_session
config = tf.ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = TEST_MEMORY_FRACTION
set_session(tf.Session(config=config))
