import sqlite3

db = sqlite3.connect('department.db')

cur = db.cursor()

create_table_query = '''CREATE TABLE department(
    id INT NOT NULL PRIMARY KEY,
    code TEXT NOT NULL,
    name TEXT NOT NULL
    )
'''

cur.execute(create_table_query)

db.commit()

db.close()