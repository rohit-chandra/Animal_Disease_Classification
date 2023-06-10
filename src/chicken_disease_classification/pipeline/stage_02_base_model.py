from chicken_disease_classification.config.configuration import ConfigurationManager
from chicken_disease_classification.components.base_model import BaseModel
from chicken_disease_classification import logger

STAGE_NAME = "Stage 02: Base Model"

class BaseModelTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        base_model_config = config.get_base_model_config()
        base_model_obj = BaseModel(config = base_model_config)
        base_model_obj.get_base_model()
        base_model_obj.update_base_model()



if __name__ == "__main__":
    try:
        logger.info(f"**********************************************")
        logger.info(f">>>>>> Running {STAGE_NAME} Started <<<<<<\n")
        
        base_model_training_pipeline_obj = BaseModelTrainingPipeline()
        base_model_training_pipeline_obj.main()
        
        logger.info(f">>>>>> Running {STAGE_NAME} Completed <<<<<<\n\n")
    
    except Exception as e:
        logger.exception(f"Error in {STAGE_NAME}: {e}")
        raise e