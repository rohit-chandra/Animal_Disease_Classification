from chicken_disease_classification import logger
from chicken_disease_classification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from chicken_disease_classification.pipeline.stage_02_base_model import BaseModelTrainingPipeline

STAGE_NAME = "Stage 01: Data Ingestion"

try:
        logger.info(f">>>>>> Running {STAGE_NAME} Started <<<<<<\n")
        
        data_ingestion_training_pipeline_obj = DataIngestionTrainingPipeline()
        data_ingestion_training_pipeline_obj.main()
        
        logger.info(f">>>>>> Running {STAGE_NAME} Completed <<<<<<\n\n")
    
except Exception as e:
        logger.exception(f"Error in {STAGE_NAME}: {e}")
        raise e



STAGE_NAME = "Stage 02: Base Model"

try:
        logger.info(f"**********************************************")
        logger.info(f">>>>>> Running {STAGE_NAME} Started <<<<<<\n")
        
        base_model_training_pipeline_obj = BaseModelTrainingPipeline()
        base_model_training_pipeline_obj.main()
        
        logger.info(f">>>>>> Running {STAGE_NAME} Completed <<<<<<\n\n")

except Exception as e:
    logger.exception(f"Error in {STAGE_NAME}: {e}")
    raise e