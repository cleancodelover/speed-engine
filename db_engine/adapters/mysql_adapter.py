from db_engine.adapters.base_adapter import BaseAdapter


class MySQLAdapter(BaseAdapter):
    def __init__(self):
        self.connection = None
    
    def connect(self, **kwargs):
        import mysql.connector
        self.connection = mysql.connector.connect(
            host=kwargs.get("host"),
            user=kwargs.get("user"),
            password=kwargs.get("password"),
            database=kwargs.get("database")
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
    
