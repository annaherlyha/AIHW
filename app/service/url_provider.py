import re
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from app.utils.url_regex import UrlRegex
from app.utils.logger import logger
import time


class UrlProvider:
    """
    This class is responsible for getting the link,
    the parameter of which is recorded in the configurations_web.ini
    """

    def __init__(self, **kwargs):

        if UrlRegex(kwargs.get('server_url')).check_url() is None:
            self._server_url = kwargs.get('server_url')
            self._base_url = kwargs.get('base_url')

        self._file_name = kwargs.get('file_name')
        self.latest_pattern = re.compile(self._file_name)

    def get_download_link(self):

        chrome_options = Options()
        chrome_options.add_argument("--headless")

        try:
            driver = webdriver.Chrome(options=chrome_options, executable_path=ChromeDriverManager().install())
            driver.get(self._base_url)
        except SystemError:
            logger.warning("Need to updated Chrome")
        time.sleep(3)
        res = driver.execute_script("return document.body.innerHTML")
        soup = BeautifulSoup(res, 'lxml')
        page_content = soup.find('div', {'class': 's-downloadable-resources__results'})

        partial_url = None
        logger.info("Searching link for {}".format(self._file_name[:-2]))
        try:
            for tag in page_content.find_all(["a"]):
                if self.latest_pattern.search(tag.text):
                    partial_url = tag.get('href')
                    break
        except AttributeError:
            logger.warning("We weren't able to get link for {}".format(self._file_name[:-2]))
            return False

        if partial_url is None:
            raise ConnectionError("We weren't able to  get  link for  {}".format(self._file_name[:-2]))

        new_url = self._server_url + str(partial_url)
        return new_url
