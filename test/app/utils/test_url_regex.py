import unittest
from app.utils.url_regex import UrlRegex


# noinspection SpellCheckingInspection
class TestUrlRegex(unittest.TestCase):
    """
    Test that it can check work for class UrlRegex

    ....

    Attributes
    ----------
    self.__test_value_good: str
        a formatted string that describes a web-link
    self.__test_value_bad: str
        a formatted string that doesnt describe a web-link
    self.__test_value_type: float
        any other type except string that doesnt describe a web-link

    Methods
    -------
    test_check_url_good
        Test that it can check web-link
    test_check_url_bad
        Test that it can check value with type string that it is not web-link
    test_check_url_type
        Test that it can check string that value is not string
    """

    __test_value_good = 'https://realpython.com'
    __test_value_bad = '//realpython.com/python-testing'
    __test_value_type = 1.2

    def test_check_url_good(self):
        """
        Test that it can check web-link

        If the argument __test_value_good is web-link, test will pass

        Parameters
        ----------
        self.__test_value_good: str
                a formatted string that describes a web-link
        """
        self.assertEqual(UrlRegex(self.__test_value_good).check_url(), None)

    def test_check_url_bad(self):
        """
        Test that it can check value with type string that it is not web-link

        If the argument __test_value_bad is string, but is no web-link, test will pass

        Parameters
        ----------
        self.__test_value_bad: str
                a formatted string that doesnt describe a web-link
        """
        with self.assertRaisesRegex(AttributeError,
                                    "WRONG config_attribute: {} IN WEB CONFIG".format(self.__test_value_bad)):
            UrlRegex(self.__test_value_bad).check_url()

    def test_check_url_type(self):
        """
        Test that it can check string that value is not string

        If the argument __test_value_type is no string, test will pass

        Parameters
        ----------
        self.__test_value_type: float
                any other type except string that doesnt describe a web-link
        """
        with self.assertRaisesRegex(TypeError,
                                    "Wrong type for value that use for URL"):
            UrlRegex(self.__test_value_type).check_url()


if __name__ == '__main__':
    unittest.main()
