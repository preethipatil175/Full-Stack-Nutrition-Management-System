from mongoengine import connect

connect(
    db="student_db",
    host="localhost",
    port=27017
)