import sqlite3

db = sqlite3.connect('semester.db')

cur = db.cursor()

create_table_query = '''CREATE TABLE semester(
    id INT NOT NULL PRIMARY KEY,
    year INT NOT NULL
)'''

cur.execute(create_table_query)

db.commit()

db.close()