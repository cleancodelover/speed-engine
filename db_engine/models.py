class Model:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        
    @classmethod
    def create_table(cls, connection):
        """Create a table based on the model."""
        fields = []
        for key, value in cls.__dict__.items():
            if not key.startswith("__"):
                fields.append(f"{key} TEXT")
        fields_str = ", ".join(fields)
        table_creation_query = f"CREATE TABLE IF NOT EXISTS {cls.__name__} ({fields_str})"
        cursor = connection.cursor()
        cursor.execute(table_creation_query)
        connection.commit()

    
    @classmethod
    def insert(cls, connection, **kwargs):
        """Insert an object into the table"""
        fields = ", ".join(kwargs.keys())
        values = ", ".join(f"'{v}'" for v in kwargs.values())
        query = f"INSERT INTO {cls.__name__} ({fields}) VALUES ({values})"
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
    
    @classmethod
    def delete(cls, connection, **kwargs):
        """Delete an object from the table."""
        query = f"DELETE FROM {cls.__name__} WHERE id={kwargs['id']}"
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()