from abc import ABC, abstractmethod
from src.data_access.query import QueryParameters


class ImagerySource(ABC):
    @abstractmethod
    def search(self, query: QueryParameters):
        pass

    @abstractmethod
    def fetch(self, item):
        pass
