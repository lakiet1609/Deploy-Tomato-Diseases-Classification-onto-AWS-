from TomatoDiseases.config.configuration import *
from TomatoDiseases.components.model_trainer import *
from TomatoDiseases.components.prepare_callbacks import PrepareCallbacks
from TomatoDiseases import logger

stage_name = 'Training model stage'

class ModelTrainerPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigManager()
        model_trainer_callbacks_config = config.get_callbacks_config()
        model_trainer_callbacks_config = PrepareCallbacks(config=model_trainer_callbacks_config)
        callbacks_list = model_trainer_callbacks_config.get_tensorboard_and_checkpoint()
        
        model_trainer_config = config.get_model_training_config()
        model_trainer_config = Training(config=model_trainer_config)
        model_trainer_config.get_base_model()
        model_trainer_config.train_valid_generator()
        model_trainer_config.train(callbacks_list=callbacks_list)

if __name__ == '__main__':
    try:
        logger.info(f'{stage_name} started')
        obj = ModelTrainerPipeline()
        obj.main()
        logger.info(f'{stage_name} completed')
    except Exception as e:
        raise