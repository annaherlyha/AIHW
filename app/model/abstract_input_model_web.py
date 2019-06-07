from abc import ABC, abstractmethod


class AbstractInputModelWeb(ABC):

    @property
    @abstractmethod
    def file_name(self):
        pass

    @property
    @abstractmethod
    def base_url(self):
        pass

    @property
    @abstractmethod
    def server_url(self):
        pass
