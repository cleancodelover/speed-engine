class QueryBuilder:
    def __init__(self, model):
        self.model = model
        self.query = f"SELECT * FROM {model.__name__}"

    def filter(self, **conditions):
        """Apply filters to the query."""
        conditions_str = " AND ".join([f"{k}='{v}'" for k, v in conditions.items()])
        self.query += f" WHERE {conditions_str}"
        return self
    
    def all(self, connection):
        """Execute the query and return results"""
        cursor = connection.cursor()
        cursor.execute(self.query)
        return cursor.fetchall()
    
    def execute(self, connection):
        """Execute any type of query."""
        cursor = connection.cursor()
        cursor.execute(self.query)
        connection.commit()
    
    