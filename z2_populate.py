import sqlite3

connection = sqlite3.connect('sampleDB.db')
cursor = connection.cursor()

def add_movie(title, director, year, genre):
    cursor.execute("""
                INSERT INTO movies (title, director, year, genre) 
                VALUES (?,?,?,?)""",(title,director,year,genre))
    
    connection.commit()
    print("Movie added")

add_movie("Inception","Christopher Nolan",2010,"Sci-Fi")
    
