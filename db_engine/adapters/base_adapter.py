from abc import ABC, abstractmethod


class BaseAdapter(ABC):
    """Abstract Base Class for Database Adatapters"""

    @abstractmethod
    def insert(self, table, data):
        pass

    @abstractmethod
    def find(self, table, filters):
        pass

    @abstractmethod
    def update(self, table, filters, updates):
        pass

    @abstractmethod
    def delete(self, table, filters):
        pass