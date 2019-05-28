import re
from bs4 import BeautifulSoup
import requests


class UrlProvider:

    def __init__(self, **kwargs):
        self._server_url = kwargs.get('server_url')
        self._base_url = kwargs.get('base_url')
        self._file_name = kwargs.get('file_name')
        self._own_name = kwargs.get('output_file')
        self.latest_pattern = re.compile((kwargs.get('file_name')))

    def get_download_link(self):

        page_response = requests.get(self._base_url, timeout=10)
        page_content = BeautifulSoup(page_response.content, "html.parser")

        print("Searching for 'Data tables: Historical tables' link")
        partial_url = None
        print("We weren't able to  get 'Data tables: Historical tables' url")

        new_url = partial_url
        return new_url

