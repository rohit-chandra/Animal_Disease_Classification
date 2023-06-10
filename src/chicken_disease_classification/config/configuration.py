from chicken_disease_classification.constants import *
from chicken_disease_classification.utils.common import read_yaml, create_directories
from chicken_disease_classification.entity.config_entity import (DataIngestionConfig, BaseModelConfig, CallbacksConfig, TrainingConfig, EvaluationConfig)
import os
from pathlib import Path

class ConfigurationManager:
    def __init__(
        self, 
        config_file_path: Path = CONFIG_FILE_PATH,
        params_file_path: Path = PARAMS_FILE_PATH
    ):
        self.config_file_path = read_yaml(config_file_path)
        self.params_file_path = read_yaml(params_file_path)
        
        # create directory -> "articfacts"; artifacts_root is present in config.yaml
        create_directories([self.config_file_path.artifacts_root])
    
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        # data_ingestion variable is present in config.yaml
        config = self.config_file_path.data_ingestion
        
        # create sub folder "data_ingestion" in "artifacts" folder
        create_directories([config.root_dir])
        
        # return DataIngestionConfig object
        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_url = config.source_url,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir
        )
        
        return data_ingestion_config
    
    
    def get_base_model_config(self) -> BaseModelConfig:
        
        base_model_config = self.config_file_path.base_model
        # create a sub directory in artifacts -> "base_model"
        create_directories([base_model_config.root_dir])
        
        # create obj of BaseModelConfig class
        base_model_config_obj = BaseModelConfig(
            root_dir = Path(base_model_config.root_dir),
            base_model_path = Path(base_model_config.base_model_path),
            updated_base_model_path = Path(base_model_config.updated_base_model_path),
            params_image_size = self.params_file_path.IMAGE_SIZE,
            params_learning_rate = self.params_file_path.LEARNING_RATE,
            params_include_top = self.params_file_path.INCLUDE_TOP,
            params_weights = self.params_file_path.WEIGHTS,
            params_classes = self.params_file_path.CLASSES
        )
        
        return base_model_config_obj
    
    
    def get_callback_config(self) -> CallbacksConfig:
        
        callbacks_config = self.config_file_path.callbacks
        
        model_ckpt_dir = os.path.dirname(callbacks_config.model_checkpoint_dir)
        # create 2 sub directories in artifacts -> model_checkpoint_dir and tensorboard_root_log_dir
        create_directories([Path(model_ckpt_dir) , Path(callbacks_config.tensorboard_root_log_dir)])
        
        # create obj of BaseModelConfig class
        callbacks_config_obj = CallbacksConfig(
            root_dir = Path(callbacks_config.root_dir),
            tensorboard_root_log_dir = Path(callbacks_config.tensorboard_root_log_dir),
            model_checkpoint_dir = Path(callbacks_config.model_checkpoint_dir)
        )
        
        return callbacks_config_obj
    
    
    
    def get_training_config(self) -> TrainingConfig:
        training = self.config_file_path.training
        base_model = self.config_file_path.base_model
        params = self.params_file_path
        training_data = os.path.join(self.config_file_path.data_ingestion.unzip_dir, "Chicken-fecal-images")
        
        # create root directory for training
        create_directories([Path(training.root_dir)])
        
        training_config_obj = TrainingConfig(
            root_dir = Path(training.root_dir),
            trained_model_dir = Path(training.trained_model_dir),
            updated_base_model_dir = Path(base_model.updated_base_model_path),
            training_data = Path(training_data),
            params_epochs = params.EPOCHS,
            params_batch_size = params.BATCH_SIZE,
            params_is_augmentation = params.AUGMENTATION,
            params_image_size = params.IMAGE_SIZE
        )
        
        return training_config_obj
    
    
    
    def get_validation_config(self) -> EvaluationConfig:
        
        # create obj of EvaluationConfig class
        eval_config_obj = EvaluationConfig(
            model_path = Path("artifacts/training/model.h5"),
            training_data_path = Path("artifacts/data_ingestion/Chicken-fecal-images"),
            all_params = self.params_file_path,
            params_image_size = self.params_file_path.IMAGE_SIZE,
            params_batch_size = self.params_file_path.BATCH_SIZE
        )
        
        return eval_config_obj
    
    