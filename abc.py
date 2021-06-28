
import tensorflow as tf
print(tf.__version__)

print("\n\n\n{}\n\n\n".format(tf.test.is_gpu_available(cuda_only=True)))