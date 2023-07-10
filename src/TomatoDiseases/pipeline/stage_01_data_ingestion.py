from TomatoDiseases.config.configuration import *
from TomatoDiseases.components.data_ingestion import *

stage_name = 'Data ingestion stage'

class DataIngestionPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingest = DataIngest(config=data_ingestion_config)
        data_ingest.download_filezip()
        data_ingest.extract_zipfile()

if __name__ == '__main__':
    try:
        logger.info(f'{stage_name} started')
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f'{stage_name} completed')
    except Exception as e:
        raise