import configparser
from app.model.abstract_input_model_web import AbstractInputModelWeb


class InputModelFromConfigWeb(AbstractInputModelWeb):
    def __init__(self):

        self.config_file_web = 'Configs/ConfigurationsWeb.ini'
        config_web = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
        config_web.read(self.config_file_web)
        self._config_web = config_web

    @property
    def config_web(self):
        return self._config_web

    @property
    def server_url(self):
        return self.config_web.get('web_config', 'server_url')

    @property
    def base_url(self):
        return self.config_web.get('web_config', 'base_url')

    @property
    def file_name(self):
        return self.config_web.get('web_config', 'file_name')