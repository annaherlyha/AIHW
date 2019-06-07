from app.service.url_provider import UrlProvider
import logging
from app.service.http_downloader import HttpDownloader

logging.basicConfig(level=logging.INFO)


class ProcessFlow:
    def __init__(self, config_model, config_model_web):
        self._config_model = config_model
        self._config_model_web = config_model_web

    @property
    def config(self):
        return self._config_model

    @property
    def config_web(self):
        return self._config_model_web

    def _get_link(self):
        config_web = self.config_web
        logging.info("STEP: DOWNLOAD - START")
        link_dict = dict()
        link_dict['server_url'] = config_web.server_url
        link_dict['base_url'] = config_web.base_url
        link_dict['file_name'] = config_web.file_name
        url_prov = UrlProvider(**link_dict)
        url = url_prov.get_download_link()
        return url

    def download_file(self):

        logging.info("Starting Download")
        config = self.config
        down_dict = dict()
        down_dict['dest_dir'] = config.temp_dir
        down_dict['work_dir'] = config.work_dir
        down_dict['own_name'] = config.own_name
        down_dict['url'] = self._get_link()
        try:
            downloader = HttpDownloader(**down_dict)
            result = downloader.download()
        except Exception as err:
            logging.warning('FAILED TO PROCESS STEP; {}'.format(err))
            return False

        logging.info("STEP: DOWNLOAD ARCHIVE - DONE")
        return result
