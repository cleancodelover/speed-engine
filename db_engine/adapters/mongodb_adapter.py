from db_engine.adapters.base_adapter import BaseAdapter


class MongoDBAdapter(BaseAdapter):
    def __init__(self):
        self.client = None
        self.db = None
    
    def connect(self, **kwargs):
        from pymongo import MongoClient
        self.client = MongoClient(kwargs.get("uri"))
        self.db = self.client[kwargs.get("database")]
    
    def disconnect(self):
        if self.client:
            self.client.close()
    
    def execute_query(self, query, params=None):
        collection = self.db[query.get("collection")]
        operation = query.get("operation")

        if operation == "find":
            return list(collection.find(params))
        elif operation == "insert_one":
            return collection.insert_one(params)
        elif operation == "update_one":
            return collection.update_one(params["filter"], params["update"])
        elif operation == "delete_one":
            return collection.delete_one(params)
        else:
            raise ValueError(f"Unsuported MongoDB operation: {operation}")
    
    def commit(self):
        pass #MongoDB is non-transactional by default

    def rollback(self):
        pass # MongoDB is non-transactional by default