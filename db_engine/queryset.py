class QuerySet:
    def __init__(self, model, query=None, params=None):
        self.model = model
        self._query = query or f"SELECT * FROM {model.__table__}"
        self._params = params or []
    
    def where(self, condition):
        """Filter records using a lambda function"""
        condition_str = self._parse_lambda(condition)
        if "WHERE" in self._query:
            self._query += f" AND {condition_str}"
        else:
            self._query += f" WHERE {condition_str}"
        return self
    
    def order_by(self, column, order="ASC"):
        self._query += f" ORDER BY {column} {order}"
        return self
    
    def limit(self, count):
        """Limit records"""
        self._query += f" LIMIT {count}"
    
    def all(self):
        """Fetch all records matching the query"""
        db = self.model._get_db()
        results = db.execute(self._query, self._params)
        return [self.model(**dict(row)) for row in results]
    
    def first(self):
        """Fetch the first record matching the query."""
        db = self.model._get_db()
        results = db.execute(self._query + " LIMIT 1", self._params)
        if results:
            return self.model(**dict(results[0]))
        return None
    
    def _parse_lambda(self, condition):
        """Parse a lambda function into a SQL condition"""
        condition_str = str(condition)
        condition_str = condition_str.split(":")[1].strip().rstrip("}")
        condition_str = condition_str.replace("==", "=")
        condition_str = condition_str.replace(".", "_")
        return condition_str
    