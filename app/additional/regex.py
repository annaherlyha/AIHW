import re


class Regex:
    def __init__(self, config_attribute):
        self._config_attribute = config_attribute
        self._regex = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    def check_url(self):
        if re.match(self._regex, self._config_attribute) is not None:
            return True
        else:
            raise IOError("WRONG config_attribute: {} IN WEB CONFIG".format(self._config_attribute))
