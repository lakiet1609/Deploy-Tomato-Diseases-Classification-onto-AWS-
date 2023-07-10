from TomatoDiseases.entity.config_entity import *
import time
import os
import tensorflow as tf

class PrepareCallbacks:
    def __init__(self, config: PrepareCallbacksConfig):
        self.config = config
    
    @property
    def create_tensorboard(self):
        timestamp = time.strftime('%Y-%m-%d-%H-%M-%S')
        running_log_dir = os.path.join(self.config.tensorboard_dir, f'tensorboard_logs_at_{timestamp}')
        return tf.keras.callbacks.TensorBoard(log_dir=running_log_dir)
    
    @property
    def create_checkpoint(self):
        return tf.keras.callbacks.ModelCheckpoint(
            filepath= self.config.checkpoint_filepath,
            save_best_only=True
        )
        
    def get_tensorboard_and_checkpoint(self):
        return [self.create_tensorboard, self.create_checkpoint]
    
    