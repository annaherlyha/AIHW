from app.controller.processing import ProcessFlow
from app.model.input_config_model import InputDataModelFromConfig

# for now australia only is supported


if __name__ == '__main__':

    data_model = InputDataModelFromConfig()
    processor = ProcessFlow(config_model=data_model)
    processor.download()

