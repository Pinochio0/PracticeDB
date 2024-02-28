import sqlite3

connection = sqlite3.connect('sampleDB.db')
cursor = connection.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS movies (
               id INTEGER PRIMARY KEY,
               title TEXT,
               director TEXT,
               year INTEGER,
               genre TEXT)
               """)