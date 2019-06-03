import requests
import logging
import os.path
import os

logging.basicConfig(level=logging.INFO)


class HttpDownloader:
    def __init__(self, **kwargs):
        self._dest_dir = kwargs.get('dest_dir')
        self._own_name = kwargs.get('own_name')
        # self._own_name = 'end_file.xlsx'
        self._url = kwargs.get('url', None)

    def download(self):

        fname = os.path.join(self._dest_dir, self._own_name)

        r = requests.get(self._url, stream=True)

        logging.info("Starting download from url {} to {}".format(self._url, fname))
        cnk_size = 1024 * 8 * 8
        cnt = 1
        with open(fname, 'wb') as f:
            for chunk in r.iter_content(chunk_size=cnk_size):
                if chunk:
                    f.write(chunk)
                    f.flush()
                    logging.info('downloaded {} KB'.format(cnt * cnk_size))
                    cnt += 1
        logging.info('Finished file download: {}'.format(fname))
        return fname
