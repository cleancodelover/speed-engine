class MongoDBAdapter:
    def __init__(self, db_connection, collection_name):
        self.db = db_connection
        self.collection = self.db[collection_name]
    
    def insert(self, document):
        """Insert a document into MongoDB"""
        self.collection.insert_one(document)
    
    def find(self, filter_criteria):
        """Find documents based on filter criteria"""
        return self.collection.find(filter_criteria)
    
    def update(self, filter_criteria, update_values):
        """Update documents in mongodb"""
        self.collection.update_many(filter_criteria, {'$set': update_values})

    def delete(self, filter_criteria):
        """Delete documents in mongodb."""
        self.collection.delete_many(filter_criteria)