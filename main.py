from app.controller.process_flow import ProcessFlow
from app.model.input_model_from_config import InputModelFromConfig

# for now australia only is supported


if __name__ == '__main__':

    data_model = InputModelFromConfig()
    processor = ProcessFlow(config_model=data_model)
    processor.download_file()

