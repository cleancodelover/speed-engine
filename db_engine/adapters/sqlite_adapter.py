import sqlite3
from db_engine.adapters.base_adapter import BaseAdapter


class SQLiteAdapter(BaseAdapter):
    def __init__(self):
        self.connection = None
    
    def connect(self, **kwargs):
        import sqlite3
        self.connection = sqlite3.connect(kwargs.get("database"))
    
    def disconnect(self):
        if self.connection:
            self.connection.close()
    
    def execute_query(self, query, params=None):
        cursor = self.connection.cursor()
        cursor.execute(query, params or ())
        return cursor.fetchall()
    
    def commit(self):
        self.connection.commit()
    
    def rollback(self):
        self.connection.rollback()