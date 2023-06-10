from chicken_disease_classification.config.configuration import ConfigurationManager
from chicken_disease_classification.components.callbacks import Callbacks
from chicken_disease_classification.components.training import Training
from chicken_disease_classification import logger


STAGE_NAME = "Stage 03: Training"



class ModelTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        callbacks_config = config.get_callback_config()
        callbacks = Callbacks(config = callbacks_config)
        callback_list = callbacks.get_tensorboard_ckpt_callbacks()
        
        training_config = config.get_training_config()
        training_obj = Training(config = training_config)
        training_obj.get_base_model()
        # Scale, train test split
        training_obj.train_valid_generator()
        # start training
        training_obj.train(callbacks_lst = callback_list)



if __name__ == "__main__":
    try:
        logger.info(f"**********************************************")
        logger.info(f">>>>>> Running {STAGE_NAME} Started <<<<<<\n")
        
        model_training_pipeline_obj = ModelTrainingPipeline()
        model_training_pipeline_obj.main()
        
        logger.info(f">>>>>> Running {STAGE_NAME} Completed <<<<<<\n\n")
    
    except Exception as e:
        logger.exception(f"Error in {STAGE_NAME}: {e}")
        raise e