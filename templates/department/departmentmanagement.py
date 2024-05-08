from flask import Flask, request, jsonify
import sqlite3

app=Flask(__name__)

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

#Add a new department to the department table
def add_department(code, name):
    conn = sqlite3.connect('department.db')
    cursor = conn.cursor()
    insert_query = """
    INSERT INTO department(code, name)
    VALUES (?,?)
    """
    cursor.execute(insert_query,(code, name))
    conn.commit()
    conn.close()
    
#Flask API routes
@app.route('/api/department/add', methods=['POST'])
def add_department_route():
    print("add department called")
    data.request.json
    print("Received data:", data)
    add_department(data['code'], data['name'])
    return jsonify({"message": "Department data added successfully"})

if __name__ == "__main__":
    app.run(debug=True)