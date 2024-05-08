import sqlite3

db = sqlite3.connect('faculty.db')

cur = db.cursor()

create_table_query = '''CREATE TABLE faculty(
    id INT NOT NULL PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    course TEXT NOT NULL
)'''

cur.execute(create_table_query)

db.commit()

db.close()