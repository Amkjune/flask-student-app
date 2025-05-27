from flask import Flask, request, render_template, redirect
from mysql.connector import connection


app = Flask(__name__)



# Create table if not exists


@app.route('/', methods=['GET', 'POST'])
def student_form():
    if request.method == 'POST':
        name = request.form['student_name']
        roll = request.form['roll_number']
        courses = request.form.getlist('courses')  # list of selected courses
        course_str = ", ".join(courses)

       # sql = "INSERT INTO Student_records (University, Student_name, Roll_number, Courses) VALUES (%s, %s, %s, %s)"
        #val = ('LPU', name, roll, course_str)
        #cursor.execute(sql, val)
       # cnx.commit()

        return redirect('/students')

    return render_template('form.html')

@app.route('/students')
def show_students():
    print("hello")
    #cursor.execute("SELECT * FROM Student_records")
    #records = cursor.fetchall()
    #return f"<h2>Students:</h2>" + "<br>".join(str(row) for row in records)

if __name__ == '__main__':
    app.run(host="host.docker.internal", port=5000, debug=True)
