from app.service.flie_url_loader import UrlProvider
import logging
from app.service.file_download import HttpDownloader

logging.basicConfig(level=logging.INFO)


class ProcessFlow:
    def __init__(self, config_model):
        self._config_model = config_model

    @property
    def config(self):
        return self._config_model

    def get_link(self):
        config = self.config
        logging.info("STEP: DOWNLOAD - START")
        link_dict = dict()
        link_dict['server_url'] = config.server_url
        link_dict['base_url'] = config.base_url
        link_dict['file_name'] = config.file_name
        urlprov = UrlProvider(**link_dict)
        url = urlprov.get_download_link()
        return url

    def download_file(self):

        logging.info("Starting Download")
        config = self.config
        down_dict = {}
        down_dict['dest_dir'] = config.temp_dir
        down_dict['work_dir'] = config.work_dir
        down_dict['own_name'] = config.own_name
        down_dict['url'] = self.get_link()
        try:
            downloader = HttpDownloader(**down_dict)
            result = downloader.download()
        except Exception as err:
            logging.warning('FAILED TO PROCESS STEP; {}'.format(err))
            return False

        logging.info("STEP: DOWNLOAD ARCHIVE - DONE")
        return result
