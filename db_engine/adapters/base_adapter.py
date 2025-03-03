from abc import ABC, abstractmethod


class BaseAdapter(ABC):
    """Abstract Base Class for Database Adatapters"""

    @abstractmethod
    def connect(self, **kwargs):
        """Connect to the database"""
        pass

    @abstractmethod
    def disconnect(self):
        """Disconnect from the database"""
        pass

    @abstractmethod
    def execute_query(self, query, params=None):
        """Execute a SQL query and return the result"""
        pass

    @abstractmethod
    def commit(self):
        """Commit the transaction"""
        pass

    @abstractmethod
    def rollback(self):
        """Rollback the transaction"""
        pass