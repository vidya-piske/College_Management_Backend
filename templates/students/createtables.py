from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Connect to the SQLite database
db = sqlite3.connect('student.db')

# Create a cursor object to execute SQL commands
cursor = db.cursor()

# Define the SQL query to create the table
create_table_query = '''
CREATE TABLE IF NOT EXISTS students (
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

# Add a new student to the student table
def add_student(name, rollno, mobile, dob, department, year, incharge):
    conn = sqlite3.connect('student.db')
    cursor = conn.cursor()
    # SQL query to insert a new student into student table
    insert_query = """
    INSERT INTO students (name, rollno, mobile, dob, department, year, incharge)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """

    # Execute the SQL query with parameters
    cursor.execute(insert_query, (name, rollno, mobile, dob, department, year, incharge))
    conn.commit()
    conn.close()

# Flask API routes
@app.route('/api/student/add', methods=['POST'])
def add_student_route():
    data = request.json
    print("Received data:", data)
    add_student(data['name'], data['rollno'], data['mobile'], data['dob'], data['department'], data['year'], data['incharge'])
    return jsonify({"message": "Student data added successfully"})

if __name__ == "__main__":
    app.run(debug=True) 
