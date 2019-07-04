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

    Attributes
    ----------
    self._server_url: str
        a formatted string that describes a web-link that will be use as begin of query for downloading file
    self._base_url: str
        a formatted string that describes a web-link from where link to download file could be find
    self._file_name: str
         a formatted string that describes part of file name that want to download
    self.latest_pattern: method
        formation of the phrase which will use for finding the web-link
    self.__partial_url: NoneType
        a dummy into which part of founded web-link will write,
         when a certain condition ('div', {'class': 's-downloadable-resources__results'}) is met

    Methods
    -------
    __check_url
       Validates web-links
    __check_driver
        Setups configurations to Selenium
    get_download_link
        Finds web-link for downloading file
    """

    def __init__(self, **kwargs):
        """
        :param kwargs:
        self._server_url: str
            a formatted string that describes a web-link that will be use as begin of query for downloading file
        self._base_url: str
            a formatted string that describes a web-link from where link to download file could be find
        self._file_name: str
            a formatted string that describes part of file name that want to download
        self.latest_pattern: method
            formation of the phrase which will use for finding the web-link
        self.__partial_url: NoneType
             a dummy into which part of founded web-link will write,
             when a certain condition ('div', {'class': 's-downloadable-resources__results'}) is met
        """

        self._server_url = str(kwargs.get('server_url'))
        self._base_url = str(kwargs.get('base_url'))
        self._file_name = str(kwargs.get('file_name'))
        self.latest_pattern = re.compile(self._file_name)
        self.__partial_url = None

    def __check_url(self):
        """
        Validates web-links

        :return:
        self._server_url: str
            a formatted string that describes a web-link that will be use as begin of query for downloading file
        self._base_url: str
            a formatted string that describes a web-link from where link to download file could be find

        Raises
        ------
        AttributeError
            If web-link are not as a web-link
        """
        if UrlRegex(self._server_url).check_url() is None:
            logger.info('Param for server web-link is fine')
            if UrlRegex(self._base_url).check_url() is None:
                logger.info('Param for base web-link is fine')
                return self._server_url, self._base_url
        else:
            raise AttributeError('Params for web-links are not fine')

    def __set_up_driver(self):
        """
        Setups configurations to Selenium

        :return:
        self.driver
            Selenium WebDriver with needful configurations

        Raises
        ------
        SystemError
           If will be problem with Chrome browser
        """

        chrome_options = Options()
        chrome_options.add_argument("--headless")

        try:
            self.driver = webdriver.Chrome(options=chrome_options, executable_path=ChromeDriverManager().install())
            logger.info("Successfully set up driver for selenium")
            return self.driver
        except SystemError:
            logger.warning("Need to update Chrome")

    def get_download_link(self):
        """
        Finds web-link for downloading file

        :return:
        new_url: str
           a formatted string that describes a web-link that will use for downloading file

        Methods
        -------
        __check_url
            Validates web-links
        __check_driver
            Setups configurations to Selenium

        Raises
        ------
        AttributeError
           If  self.latest_pattern cannot be find in web-link content (page_content)
        ConnectionError
           If  parsing_web_result is empty
           If  self.__partial_url is empty
        """
        self.__check_url()
        self.__set_up_driver().get(self._base_url)
        time.sleep(3)
        parsing_web_result = self.driver.execute_script("return document.body.innerHTML")
        if parsing_web_result is None:
            raise ConnectionError("No access for  {}".format(self._base_url))

        soup = BeautifulSoup(parsing_web_result, 'lxml')
        page_content = soup.find('div', {'class': 's-downloadable-resources__results'})

        logger.info("Searching link for {}".format(self._file_name[:-2]))
        try:
            for tag in page_content.find_all(["a"]):
                if self.latest_pattern.search(tag.text):
                    self.__partial_url = tag.get('href')
                    break
        except AttributeError:
            raise ConnectionError("We weren't able to get web-link for downloading file"
                                  " due to {} was not found in current web-link".format(self._file_name)) from None

        new_url = self._server_url + str(self.__partial_url)
        logger.info("Searching web link is {}".format(new_url))
        return new_url
