from TomatoDiseases.config.configuration import *
from TomatoDiseases.components.prepare_model import *

stage_name = 'Prepare model stage'

class PrepareModelPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigManager()
        prepare_base_model_config = config.prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.updated_base_model()

if __name__ == '__main__':
    try:
        logger.info(f'{stage_name} started')
        obj = PrepareModelPipeline()
        obj.main()
        logger.info(f'{stage_name} completed')
    except Exception as e:
        raise