import re
import logging
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from app.additional.regex import Regex
import time

logging.basicConfig(level=logging.INFO)


class UrlProvider:

    def __init__(self, **kwargs):

        if Regex(kwargs.get('server_url')).check_url():
            self._server_url = kwargs.get('server_url')
            self._base_url = kwargs.get('base_url')

        self._file_name = kwargs.get('file_name')
        self.latest_pattern = re.compile(self._file_name)

    def get_download_link(self):

        try:
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.get(self._base_url)
        except SystemError:
            logging.warning("Need to updated Chrome")
        time.sleep(3)
        res = driver.execute_script("return document.body.innerHTML")
        soup = BeautifulSoup(res, 'lxml')
        page_content = soup.find('div', {'class': 's-downloadable-resources__results'})

        partial_url = None
        logging.info("Searching link for {}".format(self._file_name[:-2]))
        try:
            for tag in page_content.find_all(["a"]):
                if self.latest_pattern.search(tag.text):
                    partial_url = tag.get('href')
                    break
        except AttributeError:
            logging.warning("We weren't able to get link for {}".format(self._file_name[:-2]))
            return False

        if partial_url is None:
            # logging.warning("We weren't able to get data for {}".format(self._file_name[:-2]))
            raise ConnectionError("We weren't able to  get  link for  {}".format(self._file_name[:-2]))

        new_url = self._server_url + str(partial_url)
        return new_url
