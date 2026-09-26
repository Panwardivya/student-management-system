from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)


# =========================
# DATABASE CONNECTION
# =========================

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        use_pure=True
    )


# =========================
# HOME
# =========================

@app.route("/")
def home():
    return "Student Management Backend is Running!"


# =========================
# GET ALL STUDENTS
# =========================

@app.route("/students", methods=["GET"])
def get_students():

    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    cursor.close()
    db.close()

    return jsonify(students)


# =========================
# ADD STUDENT
# =========================

@app.route("/students", methods=["POST"])
def add_student():

    data = request.json

    name = data["name"]
    age = data["age"]
    gender = data["gender"]
    email = data["email"]
    phone = data["phone"]
    course = data["course"]
    semester = data["semester"]
    state = data["state"]

    db = get_db_connection()
    cursor = db.cursor()

    sql = """
        INSERT INTO students
        (name, age, gender, email, phone, course, semester, state)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        name,
        age,
        gender,
        email,
        phone,
        course,
        semester,
        state
    )

    cursor.execute(sql, values)

    db.commit()

    cursor.close()
    db.close()

    return jsonify({
        "message": "Student added successfully"
    })


# =========================
# DELETE STUDENT
# =========================

@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):

    db = get_db_connection()
    cursor = db.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id = %s",
        (id,)
    )

    db.commit()

    cursor.close()
    db.close()

    return jsonify({
        "message": "Student deleted successfully"
    })


# =========================
# RUN SERVER
# =========================

if __name__ == "__main__":
    app.run(debug=True)

