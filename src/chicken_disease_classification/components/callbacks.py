import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
import time
from chicken_disease_classification.entity.config_entity import  CallbacksConfig


class Callbacks:
    
    def __init__(self, config: CallbacksConfig):
        self.config = config
    
    
    @property
    def _create_tensorboard_callbacks(self):
        """create timestamp folder save all the logs in that folder
        """
        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        tensorboard_log_dir = os.path.join(self.config.tensorboard_root_log_dir, f"tensorborad_logs_at_{timestamp}")
        
        return tf.keras.callbacks.TensorBoard(log_dir = tensorboard_log_dir)
    
    
    @property
    def _create_ckpt_callbacks(self):
        return tf.keras.callbacks.ModelCheckpoint(
            filepath = self.config.model_checkpoint_dir,
            save_best_only = True
        )
    
    
    def get_tensorboard_ckpt_callbacks(self):
        return [self._create_tensorboard_callbacks, self._create_ckpt_callbacks]
        