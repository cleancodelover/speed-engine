from db_engine.adapters.mongodb_adapter import MongoDBAdapter
from db_engine.adapters.sql_adapter import SQLAdapter

class DatabaseConnection:
    def __init__(self, db_type, **kwargs):
        self.db_type = db_type
        self.kwargs = kwargs
        self.adapter = self._initialize_adapter()
    
    def _initialize_adapter(self):
        """Returns the correct database adapter"""
        if self.db_type == "mongodb":
            return MongoDBAdapter(self.kwargs["url"], self.kwargs["db_name"], self.kwargs["collection"])
        return SQLAdapter(self.db_type, **self.kwargs)
    
    def get_adapter(self):
        return self.adapter
    
    