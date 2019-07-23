import unittest
from unittest.mock import patch
from app.service.url_provider import UrlProvider
from unittest import mock


class TestUrlProvider(unittest.TestCase):
    """
    Test that it can check work for class UrlProvider
    """
    __test_value_bad = '//realpython.com/python-testing'

    def test_custom_request(self):
        self.assertEqual(UrlProvider({"a1": self.__test_value_bad, "a2": self.__test_value_bad, "a3": self.__test_value_bad}).get_download_link(), 'o')




if __name__ == '__main__':
    unittest.main()
