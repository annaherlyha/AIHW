from abc import ABC, abstractmethod


class AbstractInputModel(ABC):

    @property
    @abstractmethod
    def output_file(self):
        pass

    @property
    @abstractmethod
    def output_dir(self):
        pass

    @property
    @abstractmethod
    def base_dir(self):
        pass

    @property
    @abstractmethod
    def temp_dir(self):
        pass

    @property
    @abstractmethod
    def work_dir(self):
        pass

    @property
    @abstractmethod
    def own_name(self):
        pass
