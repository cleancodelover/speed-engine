import sqlite3
import psycopg2
import pymysql
import pyodbc
from pymongo import MongoClient

class DatabaseConnection:
    def __init__(self, db_type, **params):
        self.db_type = db_type
        self.params = params
        self.connection = None
    
    def connect(self):
        """Establish a connection to the database"""
        if self.db_type == 'sqlite':
            self.connection = sqlite3.connect(self.params.get("database"))
        elif self.db_type == 'postgresql':
            self.connection = psycopg2.connect(**self.params)
        elif self.db_type == 'mysql':
            self.connection = pymysql.connect(**self.params)
        elif self.db_type == 'mssql':
            self.connection = pyodbc.connect(self.params.get("connection_string"))
        elif self.db_type == 'mongodb':
            self.connection = MongoClient(self.params.get("uri"))
        else:
            raise ValueError("Unsupported database type")
        return self.connection
    
    def close(self):
        """Close hte database connection"""
        if self.connection:
            self.connection.close()