from db_engine.model import Model


class Session:
    def __init__(self, connection):
        self.connection = connection
        self.objects = []
    
    def add(self, obj):
        """Add object to session"""
        self.objects.append(obj)
    
    def commit(self):
        """Save all changes to the database"""
        for obj in self.objects:
            if isinstance(obj, Model):
                obj.insert(self.connection, **obj.__dict__)
        self.connection.commit()
        self.objects.clear()
    
    def rollback(self):
        """Rollback changes."""
        self.objects.clear()
