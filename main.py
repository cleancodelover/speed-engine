from db_engine.connection import DatabaseConnection
from db_engine.models import Model
from db_engine.query_builder import QueryBuilder
from db_engine.session import Session

# Initialize the database connection
db = DatabaseConnection("test.db")
connection = db.connect()

session = Session(connection)

#Define a sample model
class User(Model):
    name = None
    age = None

"""use this if you are not using the ORM"""
# # Create the table
# User.create_table(connection)

# # Insert a record
# User.insert(connection, name="Regina", Age=2)

# query = QueryBuilder(User)
# results = query.filter(name="Peter").all(connection)


"""When using ORM, use it in this way."""
user = User()
user.name = "Peter"
user.age = 3

session.add(user)
session.commit()

query = QueryBuilder(User)
results = query.filter(name="Peter").all(connection)

print(results)

#Close the connection
db.close()