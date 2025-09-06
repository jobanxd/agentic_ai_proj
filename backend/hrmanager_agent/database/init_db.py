import sqlite3
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

def read_sql_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        return None

def create_database():
    
    # Database file path
    db_path = BASE_DIR / 'hris_database.db'

    # Remove existing database if it exists
    if os.path.exists(db_path):
        os.remove(db_path)
        print(f"Removed existing database: {db_path}")
    
    # Connect to databse (plus creates the db file)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    print(f"Created new database: {db_path}")

    # Read and execuite DDL script
    print("Reading DDL script...")
    ddl_file_path = BASE_DIR / 'ddl' / 'hris_schema.sql'
    ddl_script = read_sql_file(ddl_file_path)
    print(ddl_script)
    try: 
        cursor.executescript(ddl_script)
        print("Database schema created successfully!")
    except Exception as e:
        print(f"Error executing DDL script: {e}")


    # Read and execuite DDL script
    print("Reading DML script...")
    dml_file_path = BASE_DIR / 'dml' / 'hris_sample_data.sql'
    dml_script = read_sql_file(dml_file_path)
    print(dml_script)
    try:
        cursor.executescript(dml_script)
        print("Sample data inserted successfully!")
    except Exception as e:
        print(f"Error executing DML script: {e}")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    print("Initializing HRIS Database...")
    create_database()
