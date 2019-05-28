import re
from bs4 import BeautifulSoup
import requests


class UrlProvider:

    def __init__(self, **kwargs):
        self._server_url = kwargs.get('server_url')
        self._base_url = kwargs.get('base_url')
        self._file_name = kwargs.get('file_name')
        self._own_name = kwargs.get('output_file')
        self.latest_pattern = re.compile('Data tables: Historical tables.*')

    def get_download_link(self):
        # First -going to 'Past and future releases to get latest link'

        page_response = requests.get(self._base_url, timeout=10)
        page_content = BeautifulSoup(page_response.content, "html.parser")

        print("Searching for 'Data tables: Historical tables' link")
        partial_url = None
        for tag in page_content.find_all(["a"]):
            if self.latest_pattern.search(tag.text):
                partial_url = tag.get('href')
                break
        if partial_url is None:
            print("We weren't able to  get 'latest' url")
            raise ConnectionError("We weren't able to  get 'latest' url")
        new_url = partial_url
        print(new_url)