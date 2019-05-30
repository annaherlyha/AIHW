import re
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import numpy as np
import pandas as pd
import os
import time


class UrlProvider:

    def __init__(self, **kwargs):
        self._server_url = kwargs.get('server_url')
        self._base_url = kwargs.get('base_url')
        self._file_name = kwargs.get('file_name')
        self._own_name = kwargs.get('output_file')
        self.latest_pattern = re.compile('Data tables: Historical tables SHSC 2011–12 to 2017–18')

    def get_download_link(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(self._base_url)
        time.sleep(3)
        res = driver.execute_script("return document.body.innerHTML")
        soup = BeautifulSoup(res, 'lxml')
        page_content = soup.find('div', {'class': 's-downloadable-resources__results'})

        partial_url = None
        for tag in page_content.find_all(["a"]):

            if self.latest_pattern.search(tag.text):
                partial_url = tag.get('href')
                break

        print("Searching for 'Data tables: Historical tables' link")
        print("We weren't able to  get 'Data tables: Historical tables' url")

        new_url = self._server_url + str(partial_url)
        print(new_url)
        return new_url
