from db_engine.adapters.base_adapter import BaseAdapter


class MSSQLAdapter(BaseAdapter):
    def __init__(self):
        self.connection = None
    
    def connect(self, **kwargs):
        import pyodbc
        self.connection = pyodbc.connect(
            f"DRIVER={{ODBC Driver 17 for SQL Server}};",
            f"SERVER={kwargs.get('host')};",
            f"DATABASE={kwargs.get('database')};",
            f"UID={kwargs.get('user')};",
            f"PWD={kwargs.get('password')}"
        )
    
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