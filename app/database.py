import sqlite3

DB_FILE = "users.db"

# Initialize SQLite Database
def initialize_database():
    conn = sqlite3.connect(DB_FILE, check_same_thread=False)
    cursor = conn.cursor()

    # Create users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

def get_db_connection():
    return sqlite3.connect("users.db", check_same_thread=False)

def close_db_connection(conn):
    conn.close()

# Run database initialization when this module is imported
initialize_database()