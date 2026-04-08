# SQLite setup
import sqlite3
DB_NAME = "studentTracker.db"

def get_connection():
    connection = sqlite3.connect(DB_NAME)
    connection.row_factory = sqlite3.Row
    return connection

def init_db():
    connection = get_connection()
    command = connection.cursor()
    
    command.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            grade TEXT
        )
                    """)
    command.execute("""
        CREATE TABLE IF NOT EXISTS contests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            date TEXT
        )
                    """)
    command.execute("""
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            contest_id INTEGER,
            score REAL,
            FOREIGN KEY (student_id) REFERENCES students(id),
            FOREIGN KEY (contest_id) REFERENCES contest(id)
        )
                    """)
    connection.commit()
    connection.close()