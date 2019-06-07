import configparser
from app.model.abstract_input_model import AbstractInputModel


class InputModelFromConfig(AbstractInputModel):
    def __init__(self):

        self.config_file = 'Configs/Configurations.ini'
        config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
        config.read(self.config_file)
        self._config = config

    @property
    def config(self):
        return self._config

    @property
    def base_dir(self):
        return self.config.get('file_system', 'root_dir')

    @property
    def temp_dir(self):
        return self.config.get('file_system', 'temp_dir')

    @property
    def work_dir(self):
        return self.config.get('file_system', 'work_dir')

    @property
    def output_dir(self):
        return self.config.get('file_system', 'output_dir')

    @property
    def output_file(self):
        return self.config.get('data_processor', 'output_file')

    @property
    def own_name(self):
        return self.config.get('data_processor', 'own_name')
