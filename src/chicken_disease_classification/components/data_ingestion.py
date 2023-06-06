import os
# to download the file
import urllib.request as request
# to unzip the file
import zipfile
from chicken_disease_classification import logger
from chicken_disease_classification.utils.common import get_size
from chicken_disease_classification.entity.config_entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    # download the file from the source url
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            file_name, headers = request.urlretrieve(url = self.config.source_url, filename = self.config.local_data_file)
            logger.info(f"{file_name} downloaded successfully with the following headers: {headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")
    
    
    # unzip the file after downloading
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory.
        
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)