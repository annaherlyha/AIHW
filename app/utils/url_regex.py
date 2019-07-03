import re


class UrlRegex:
    """
    This class checks correctness value for web-link

    ....

    Attributes
    ----------
    self._config_attribute: str
        a formatted string that describes a web-link
    self._url_regex: class
        class that include regex for checking if string is web-link or not

    Methods
    -------
    check_url
        Check if value is web-link or not

    """

    def __init__(self, config_attribute):
        """
        Parameters
        ----------
        self._config_attribute: str
                a formatted string that describes a web-link
        self._url_regex: class
                class that include regex for checking if string is web-link or not
        """
        self._config_attribute = config_attribute
        self._url_regex = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?))', re.IGNORECASE)

    def check_url(self):
        """
        Check if value is web-link or not

        Parameters
        ----------
        self._config_attribute: str
                a formatted string that describes a web-link
        self._url_regex: class
                class that include regex for checking if string is web-link or not

        Returns
        ------
        None
          If  _config_attribute is set as a web-link

        Raises
        ------
        TypeError
             If _config_attribute is not as a str type
        AttributeError
            If _config_attribute is not set or not as a web-link

        """

        if isinstance(self._config_attribute, str):
            if re.match(self._url_regex, self._config_attribute) is None:
                raise AttributeError("WRONG config_attribute: {} IN WEB CONFIG".format(self._config_attribute))
        else:
            raise TypeError("Wrong type for value that use for URL")
