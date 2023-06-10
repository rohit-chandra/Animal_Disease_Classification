from chicken_disease_classification.config.configuration import ConfigurationManager
from chicken_disease_classification.components.evaluation import Evaluation
from chicken_disease_classification import logger


STAGE_NAME = "Stage 04: Evaluation"



class EvaluationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        callbacks_config = config.get_validation_config()
        evaluation_obj = Evaluation(config = callbacks_config)
        evaluation_obj.evaluation()
        evaluation_obj.save_score()



if __name__ == "__main__":
    try:
        logger.info(f"**********************************************")
        logger.info(f">>>>>> Running {STAGE_NAME} Started <<<<<<\n")
        
        evaluation_pipeline_obj = EvaluationPipeline()
        evaluation_pipeline_obj.main()
        
        logger.info(f">>>>>> Running {STAGE_NAME} Completed <<<<<<\n\n")
    
    except Exception as e:
        logger.exception(f"Error in {STAGE_NAME}: {e}")
        raise e