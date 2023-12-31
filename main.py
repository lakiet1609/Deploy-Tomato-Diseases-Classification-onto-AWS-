from TomatoDiseases import logger
from TomatoDiseases.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from TomatoDiseases.pipeline.stage_02_prepare_model import PrepareModelPipeline
from TomatoDiseases.pipeline.stage_03_training import ModelTrainerPipeline
from TomatoDiseases.pipeline.stage_04_model_evaluation import ModelEvaluationPipeline


stage_name = 'Data ingestion stage'
try:
    logger.info(f'{stage_name} started')
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f'{stage_name} completed')
except Exception as e:
    raise e


stage_name = 'Prepare model stage'
try:
    logger.info(f'{stage_name} started')
    obj = PrepareModelPipeline()
    obj.main()
    logger.info(f'{stage_name} completed')
except Exception as e:
    raise e


stage_name = 'Training model stage'
try:
    logger.info(f'{stage_name} started')
    obj = ModelTrainerPipeline()
    obj.main()
    logger.info(f'{stage_name} completed')
except Exception as e:
    raise


stage_name = 'Evaluating model stage'
try:
    logger.info(f'{stage_name} started')
    obj = ModelEvaluationPipeline()
    obj.main()
    logger.info(f'{stage_name} completed')
except Exception as e:
    raise
