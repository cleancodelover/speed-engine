class Model:
    @classmethod
    def insert(cls, connection, **data):
        return connection.get_adapter().insert(cls.__name__.lower(), data)
    
    @classmethod
    def find(cls, connection, **filters):
        return connection.get_adapter().find(cls.__name__.lower(), filters)
    
    @classmethod
    def update(cls, connection, filters, updates):
        return connection.get_adapter().update(cls.__name__.lower(), filters, updates)
    
    @classmethod
    def delete(cls, connection, filters):
        return connection.get_adapter().delete(cls.__name__.lower(), filters)