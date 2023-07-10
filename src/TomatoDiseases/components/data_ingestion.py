import os
import urllib.request as request
import zipfile
from TomatoDiseases import logger
from TomatoDiseases.utils.common import *
from TomatoDiseases.entity.config_entity import DataIngestionConfig

class DataIngest:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_filezip(self):
        if not os.path.exists(self.config.local_data_file):
            filename, header = request.urlretrieve(
                url= self.config.source_url,
                filename= self.config.local_data_file
            )
            logger.info(f'{filename} downloaded with the following info: {header}')
        else:
            logger.info(f'File already existed of size: {get_size(Path(self.config.local_data_file))}')
    
    def extract_zipfile(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)