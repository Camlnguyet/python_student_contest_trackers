# FastAPI
from fastapi import FastAPI, HTTPException
from database import get_connection, init_db
from models import Student, Contest, Score

app = FastAPI()

init_db()

@app.post("/students")
def add_student(student: Student):
    connection = get_connection()
    command = connection.cursor()
    command.execute("INSERT INTO students (name, grade) VALUES (?, ?)",
                    (student.name, student.grade))
    connection.commit()
    new_id = command.lastrowid
    connection.close()
    return {"id: ": new_id, "name: ": student.name, "grade: ": student.grade}

@app.get("/students")
def get_student():
    connection = get_connection()
    command = connection.cursor()
    command.execute("SELECT * FROM students")
    rows = command.fetchall()
    connection.close()
    return [dict(row) for row in rows]  

@app.post("/contests")
def add_contest(contest: Contest):
    connection = get_connection()
    command = connection.cursor()
    command.execute("INSERT INTO contests (name, date) VALUES (?,?)", (contest.name, contest.date))
    connection.commit()
    new_id = command.lastrowid
    connection.close()
    return {"id: ": new_id, "name: ": contest.name, "date: ": contest.date}

@app.get("/contest")
def get_contest():
    connection = get_connection()
    command = connection.cursor()
    command.execute("SELECT * FROM contests")
    rows = command.fetchall()
    connection.close()
    return [dict(row) for row in rows]

@app.post("/score")
def add_score(score: Score):
    connection = get_connection()
    command = connection.cursor()
    command.execute("INSERT INTO scores (student_id, contest_id, score) VALUES (?, ?, ?)",
                    (score.student_id, score.contest_id, score.score)
                    )
    connection.commit()
    new_id = command.lastrowid
    connection.close()
    return {"id: ": new_id, "student_id: ": score.student_id, "contest_id: ": score.contest_id, "score: ": score.score}

@app.get("/score")
def get_score():
    connection = get_connection()
    command = connection.cursor()
    command.execute("SELECT * FROM scores")
    rows = command.fetchall()
    connection.close()
    return [dict(row) for row in rows]
    