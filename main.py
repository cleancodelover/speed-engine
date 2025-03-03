from config import DATABASE_CONFIG
from db_engine.engine import DatabaseEngine


def main():
    db = DatabaseEngine(DATABASE_CONFIG["adapter"], **DATABASE_CONFIG)
    db.crea