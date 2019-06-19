from app.controller.process_flow import ProcessFlow
from app.model.input_model_from_config import InputModelFromConfig
from app.model.input_model_from_config_web import InputModelFromConfigWeb

# for now australia only is supported


if __name__ == '__main__':
    data_model, data_model_web = InputModelFromConfig(), InputModelFromConfigWeb()
    processor = ProcessFlow(config_model=data_model, config_model_web=data_model_web)
    processor.get_converter()
