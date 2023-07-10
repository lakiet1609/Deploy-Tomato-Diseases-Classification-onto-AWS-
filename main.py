from TomatoDiseases import logger
from TomatoDiseases.pipeline.stage_01_data_ingestion import DataIngestionPipeline

stage_name = 'Data ingestion stage'
try:
    logger.info(f'{stage_name} started')
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f'{stage_name} completed')
except Exception as e:
    raise e