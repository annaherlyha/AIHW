from app.service.flie_url_loader import UrlProvider


class ProcessFlow:
    def __init__(self, config_model):
        self._config_model = config_model

    @property
    def config(self):
        return self._config_model

    def download_archive(self):
        config = self.config
        print("STEP: DOWNLOAD - START")
        data_proc_dict = dict()
        data_proc_dict['work_dir'] = config.work_dir
        data_proc_dict['server_url'] = config.server_url
        data_proc_dict['base_url'] = config.base_url
        data_proc_dict['base_url'] = config.base_url
        data_proc_dict['file_name'] = config.file_name
        urlprov = UrlProvider(**data_proc_dict)
        url = urlprov.get_download_link()
        return url




