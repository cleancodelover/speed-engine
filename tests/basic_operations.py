import unittest
from db_engine.models import Model
from db_engine.connection import DatabaseConnection

class TestORM(unittest.TestCase):
    def test_insert(self):
        connection = DatabaseConnection(db_type='sqlite', database='test.db').connect()
        model = Model()
        model.insert(connection, name="John Doe", age=30)
        #assert something about the database
        connection.close()