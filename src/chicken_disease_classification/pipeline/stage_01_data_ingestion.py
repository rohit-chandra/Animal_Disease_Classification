from chicken_disease_classification.config.configuration import ConfigurationManager
from chicken_disease_classification.components.data_ingestion import DataIngestion
from chicken_disease_classification import logger

STAGE_NAME = "Stage 01: Data Ingestion"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    
    def main(self):
        config_manager = ConfigurationManager()
        data_ingestion_config = config_manager.get_data_ingestion_config()
        data_ingestion = DataIngestion(config = data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()



if __name__ == "__main__":
    try:
        logger.info(f">>>>>> Running {STAGE_NAME} Started <<<<<<\n")
        
        data_ingestion_training_pipeline_obj = DataIngestionTrainingPipeline()
        data_ingestion_training_pipeline_obj.main()
        
        logger.info(f">>>>>> Running {STAGE_NAME} Completed <<<<<<\n\n")
    
    except Exception as e:
        logger.exception(f"Error in {STAGE_NAME}: {e}")
        raise e


