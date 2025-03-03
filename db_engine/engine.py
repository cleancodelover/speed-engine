import importlib
import importlib.util
import os
from db_engine.utils import get_adapter


class DatabaseEngine:
    def __init__(self, adapter_name, **kwargs):
        self.adapter = get_adapter(adapter_name)
        self.adapter.connect(**kwargs)
    
    def execute(self, query, params=None):
        return self.adapter.execute_query(query, params)
    
    def commit(self):
        self.adapter.commit()
    
    def rollback(self):
        self.adapter.rollback()
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.rollback()
        else:
            self.commit()
        self.adapter.disconnect()
    
    def create_tables_from_folder(self, folder_path):
        """Scan a folder for python classes and create corresponding tables."""
        for root, _, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".py") and file != "__init__.py":
                    module_path = os.path.join(root, file)
                    module_name = os.path.splitext(file)[0]
                    spec = importlib.util.spec_from_file_location(module_name, module_path)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)

                    for name, obj in module.__dict__.items():
                        if isinstance(obj, type) and name != "Model":
                            self._create_table_from_class(obj)
    
    def _create_table_from_class(self, cls):
        """Create a table from a class definition"""
        table_name = cls.__name__.lower()
        columns = []
        for attr, value in cls.__dict__.items():
            if not attr.startswith("__"):
                if isinstance(value, str):
                    columns.append(f"{attr} TEXT")
                elif isinstance(value, int):
                    columns.append(f"{attr} INTEGER")
                elif isinstance(value, float):
                    columns.append(f"{attr} REAL")
                else:
                    raise ValueError(f"Unsuported attribute type: {type(value)} on {attr}")
            if not columns:
                raise ValueError(f"No attributes found for class: {cls.__name__}")
            
            columns_str = ", ".join(columns)
            query = f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT, {columns_str});"
            self.execute(query)