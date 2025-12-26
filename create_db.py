import sqlite3
conn = sqlite3.connect('students.db')
conn . execute('''
CREATE TABLE students (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
roll TEXT,
department TEXT,
email TEXT,
phone TEXT
)
''')
conn.close()
