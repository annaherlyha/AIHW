import requests
import os.path
import os
from app.utils.logger import logger


class HttpDownloader:
    """
    This class is responsible for downloading the file from URL,
    the parameter of which is recorded in the configurations_web.ini
    """
    def __init__(self, **kwargs):
        self._dest_dir = kwargs.get('dest_dir')
        self._own_name = kwargs.get('own_name')
        self._url = kwargs.get('url', None)
        os.makedirs(self._dest_dir, exist_ok=True)

    def download(self):

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
                    logger.info('downloaded {} KB'.format(cnt * cnk_size))
                    cnt += 1
        logger.info('Finished file download: {}'.format(filename))
        return filename
