import unittest

import mock
import pytest
from unittest.mock import patch


class TestRequestService:
    @patch('app.service.url_provider.UrlProvider')
    def test_custom_request(self, my_request_mock):
        my_request_mock.request.side_effect = ConnectionError

        with pytest.raises(ConnectionError):
            my_request_mock.request()


if __name__ == '__main__':
    unittest.main()
