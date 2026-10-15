from fastapi import FastAPI
app = FastAPI(title="lahari")

students = [
    {"id":1,"name":"x","dept":"python"},
    {"id":2,"name":"y","dept":"java"},
    {"id":3,"name":"z","dept":"python"},
    {"id":4,"name":"a","dept":"java"},
    {"id":5,"name":"p","dept":"c"}
]
@app.get("/students/{student_id}")
def home(student_id : int):
    print(student_id)
    print(type(student_id))
    for student in students:
        if student["id"] == student_id:
            return student

    return {"message" : "student not found or invalid id"}

@app.get("/students")
def dept(dept:str):
    r = []
    for i in students:
        if i["dept"] == dept:
            r.append(i)
    return r
