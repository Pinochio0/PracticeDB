import sqlite3

connection = sqlite3.connect('sampleDB.db')
cursor = connection.cursor()

cursor.execute("SELECT * FROM movies")
print(cursor.fetchall())