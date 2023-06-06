from chicken_disease_classification import logger
from chicken_disease_classification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Stage 01: Data Ingestion"

try:
        logger.info(f">>>>>> Running {STAGE_NAME} Started <<<<<<\n")
        
        data_ingestion_training_pipeline_obj = DataIngestionTrainingPipeline()
        data_ingestion_training_pipeline_obj.main()
        
        logger.info(f">>>>>> Running {STAGE_NAME} Completed <<<<<<\n\n")
    
except Exception as e:
        logger.exception(f"Error in {STAGE_NAME}: {e}")
        raise e