from abc import ABC, abstractmethod
import yaml

class YmlReader(ABC):
    def __init__(self):
        with open(self.get_file_name()) as f:
            self.raw_data = yaml.safe_load(f)
        self.data = self.get_data()
    
    @abstractmethod
    def get_file_name(self):
        pass

    @abstractmethod
    def get_data(self):
        pass