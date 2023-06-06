from chicken_disease_classification.constants import *
from chicken_disease_classification.utils.common import read_yaml, create_directories
from chicken_disease_classification.entity.config_entity import DataIngestionConfig

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