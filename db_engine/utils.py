from db_engine.adapters.mongodb_adapter import MongoDBAdapter
from db_engine.adapters.mssql_adapter import MSSQLAdapter
from db_engine.adapters.mysql_adapter import MySQLAdapter
from db_engine.adapters.postgress_adapter import PostgreSQLAdapter
from db_engine.adapters.sqlite_adapter import SQLiteAdapter


def get_adapter(adapter_name):
    """Dynamically import and return the required adapter."""
    try:
        if adapter_name == "sqlite":
            import sqlite3
            return SQLiteAdapter
        elif adapter_name == "mysql":
            import mysql.connector
            return MySQLAdapter
        elif adapter_name == "postgresql":
            import psycopg2
            return PostgreSQLAdapter
        elif adapter_name == "mssql":
            import pyodbc
            return MSSQLAdapter
        elif adapter_name == "mongodb":
            from pymongo import MongoClient
            return MongoDBAdapter
        else:
            raise ValueError(f"Unsuported adapter: {adapter_name}")
    except ImportError as e: 
        raise ImportError(f"Missing dependency for {adapter_name}"
                          f"Install it with: pip install speed-engine[{adapter_name}]")