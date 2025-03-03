from db_engine.engine import DatabaseEngine
from db_engine.queryset import QuerySet


class Model:
    __table__ = None
    __primary_key__ = "id"

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    @classmethod
    def _get_db(cls):
        from config import DATABASE_CONFIG
        return DatabaseEngine(DATABASE_CONFIG["adapter"], **DATABASE_CONFIG)
    
    @classmethod
    def query(cls):
        """Return a QuerySet for this model"""
        return QuerySet(cls)
    
    @classmethod
    def find_all(cls):
        """Fetch all records from the table"""
        return cls.query().all()
    
    @classmethod
    def find_by_id(cls, id):
        """Fetch a record by its primary key"""
        return cls.query().where(lambda x: getattr(x, cls.__primary_key__) == id).first()
    

    @classmethod
    def create(self):
        """Insert a new record into the table"""
        db = self._get_db()
        columns = []
        values = []
        for key, value in self.__dict__.items():
            if not key.startswith("_"):
                columns.append(key)
                values.append(value)
        columns_str = ", ".join(columns)
        placeholders = ", ".join(["?"] * len(values))
        query = f"INSERT INTO {self.__table__} ({columns_str}) VALUES ({placeholders})"
        db.execute(query, values)
        db.commit()
    
    @classmethod
    def update(self):
        """Update an existing record in the table"""
        db = self._get_db()
        updates = []
        values = []
        for key, value in self.__dict__.items():
            if not key.startswith("_") and key != self.__primary_key__:
                updates.append(f"{key} = ?")
                values.append(value)
        values.append(getattr(self, self.__primary_key__))
        updates_str = ", ".join(updates)
        query = f"UPDATE {self.__table__} SET {updates_str} WHERE {self.__primary_key__} = ?;"
        db.execute(query, values)
        db.commit()
    
    @classmethod
    def delete(self):
        """Delete a record from the table"""
        db = self._get_db()
        query = f"DELETE FROM {self.__table__} WHERE {self.__primary_key__} = ?;"
        db.execute(query, (getattr(self, self.__primary_key__),))
        db.commit()