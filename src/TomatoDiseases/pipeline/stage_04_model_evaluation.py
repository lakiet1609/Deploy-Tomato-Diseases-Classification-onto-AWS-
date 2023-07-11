from TomatoDiseases.config.configuration import *
from TomatoDiseases.components.model_trainer import *
from TomatoDiseases.components.model_evaluation import Evaluation
from TomatoDiseases import logger

stage_name = 'Evaluating model stage'

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigManager()
        evaluation_config = config.get_evaluation_config()
        evaluation = Evaluation(config=evaluation_config)
        evaluation.evaluate()
        evaluation.save_score()

if __name__ == '__main__':
    try:
        logger.info(f'{stage_name} started')
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f'{stage_name} completed')
    except Exception as e:
        raise


