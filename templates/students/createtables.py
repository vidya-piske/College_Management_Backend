import sqlite3

# Connect to the SQLite database
db = sqlite3.connect('student.db')

# Create a cursor object to execute SQL commands
cursor = db.cursor()

# Define the SQL query to create the table 
create_table_query = '''
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    rollno INT NOT NULL,
    mobile INT NOT NULL,
    dob INT NOT NULL,
    department TEXT NOT NULL,
    year INT NOT NULL,
    incharge TEXT NOT NULL
)
'''

# Execute the SQL query to create the table
cursor.execute(create_table_query)

# Commit the changes to the database
db.commit()

# Close the database connection
db.close()
