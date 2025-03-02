import sqlite3
from db_engine.adapters.base_adapter import BaseAdapter
import psycopg2
import mysql.connector
from db_engine.adapters.mongodb_adapter import MongoDBAdapter
import pyodbc


class SQLAdapter(BaseAdapter):
    def __init__(self, db_type, **kwargs):
        self.db_type = db_type
        self.kwargs = kwargs
        self.connection = self._connect()
    
    def _connect(self):
        """Connects to the appropriate SQL database"""
        if self.db_type == "sqlite":
            return sqlite3.connect(self.kwargs.get("database", "database.db"))
        
        elif self.db_type == "postgresql":
            return psycopg2.connect(**self.kwargs)
        
        elif self.db_type == "mysql":
            return mysql.connector.connect(**self.kwargs)
        
        elif self.db_type == "mssql":
            return pyodbc.connect(**self.kwargs)
        else:
            raise ValueError(f"Unsupported database type: {self.db_type}")
    
    def insert(self, table, data):
        columns = ", ".join(data.keys())
        values = ", ".join(["%s"] * len(data))
        sql = f"INSERT INTO {table} ({columns}) VALUES ({values})"

        cursor = self.connection.cursor()
        cursor.execute(sql, tuple(data.values()))
        self.connection.commit()
        return cursor.lastrowid
    
    def find(self, table, filters=None):
        """Select records with filters"""
        sql = f"SELECT * FROM {table}"
        if filters:
            conditions = " AND ".join([f"{key} = %s" for key in filters.keys()])
            sql += f" WHERE {conditions}"
        cursor = self.connection.cursor()
        cursor.execute(sql, tuple(filters.values()) if filters else ())
        return cursor.fetchall()
    
    def update(self, table, filters, updates):
        set_clause = ", ".join([f"{key} = %s" for key in updates.keys()])
        where_clause = ", AND ".join(f"{key} = %s" for key in filters.keys())

        sql = f"UPDATE {table} SET {set_clause} WHERE {where_clause}"
        values = tuple(updates.values())+tuple(filters.values())

        cursor = self.connection.cursor()
        cursor.execute(sql, values)
        self.connection.commit()
        return cursor.rowcount
    
    def delete(self, table, filters):
        where_clause = " AND ".join([f"{key} = %s" for key in filters.keys()])
        sql = f"DELETE FROM {table} WHERE {where_clause}"

        cursor = self.connection.cursor()
        cursor.execute(sql, tuple(filters.values()))
        self.connection.commit()
        return cursor.rowcount
