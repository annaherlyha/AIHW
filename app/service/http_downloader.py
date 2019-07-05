import requests
import os.path
import os
from app.utils.logger import logger
import urllib.request
from app.utils.url_regex import UrlRegex


class HttpDownloader:
    # todo: validate path
    """
    This class is responsible for downloading the file from URL,
    the parameter of which is recorded in the configurations_web.ini

    Attributes
    ----------
    self._dest_dir: path
        a formatted string that describes a web-link that will be use as begin of query for downloading file
    self._own_name: str
        a formatted string that describes as the downloaded file will be called
    self.__file_format: str
        a formatted string that describes format file for self._own_name
    self._url: str
         a formatted string that describes a web-link that will use for downloading file

    Methods
    -------
    __check_url
       Validates web-links
    download
        Downloads file
    """

    def __init__(self, **kwargs):
        self._dest_dir = kwargs.get('dest_dir')
        self.__file_format = '.xlsx'
        self._own_name = str(kwargs.get('own_name')) + self.__file_format
        self._url = str(kwargs.get('url', None))
        os.makedirs(self._dest_dir, exist_ok=True)

    def __check_url(self):
        """
        Validates web-links

        :return:
        self._url: str
            a formatted string that describes a web-link that will use for downloading file

        Raises
        ------
        AttributeError
            If web-link are not as a web-link
        """
        if UrlRegex(self._url).check_url() is None:
            logger.info('Param for download web-link is fine')
            return self._url
        else:
            raise AttributeError('Params for download web-links are not fine')

    def download(self):
        # todo: exception
        """
        Downloads file

        Methods
        -------
        __check_url
            Validates web-links
        __check_driver
            Setups configurations to Selenium

        :return:
        filename
           The path of saved file
        """
        self.__check_url()

        filename = os.path.join(self._dest_dir, self._own_name)

        r = requests.get(self._url, stream=True)
        logger.info("Starting download from url {} to {}".format(self._url, filename))
        cnk_size = 1024 * 8 * 8
        cnt = 1
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=cnk_size):
                if chunk:
                    f.write(chunk)
                    f.flush()
                    logger.info('Downloaded {} KB'.format(cnt * cnk_size))
                    cnt += 1
        logger.info('Finished file download: {}'.format(filename))
        return filename
