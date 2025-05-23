from flask import Flask, request, render_template, redirect
from mysql.connector import connection


app = Flask(__name__)

# MySQL connection
cnx = connection.MySQLConnection(user='root', password='Ammy@123', host='host.docker.internal', database='mydb')
cursor = cnx.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS Student_records (
    id INT AUTO_INCREMENT PRIMARY KEY,
    University VARCHAR(100),
    Student_name VARCHAR(100),
    Roll_number VARCHAR(100),
    Courses TEXT
)
""")
cnx.commit()

@app.route('/', methods=['GET', 'POST'])
def student_form():
    if request.method == 'POST':
        name = request.form['student_name']
        roll = request.form['roll_number']
        courses = request.form.getlist('courses')  # list of selected courses
        course_str = ", ".join(courses)

        sql = "INSERT INTO Student_records (University, Student_name, Roll_number, Courses) VALUES (%s, %s, %s, %s)"
        val = ('LPU', name, roll, course_str)
        cursor.execute(sql, val)
        cnx.commit()

        return redirect('/students')

    return render_template('form.html')

@app.route('/students')
def show_students():
    cursor.execute("SELECT * FROM Student_records")
    records = cursor.fetchall()
    return f"<h2>Students:</h2>" + "<br>".join(str(row) for row in records)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
