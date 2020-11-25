from database.db import fetch_engine

db = fetch_engine()
from models.Classes import Classes
from models.Instructor import Instructor
from models.Student import Student


class Review(db.Document):
    id = db.UUIDField(required=True)
    created_date = db.DateTimeField(required=True)
    modified_date = db.DateTimeField(required=True)
    description = db.StringField(description='description')
    rating = db.IntField(choices=(1,2,3,4,5), description='star rating')
    class_id = db.ReferenceField(Classes, 'id')
    instructor_id = db.ReferenceField(Instructor, 'id')
    student_id = db.ReferenceField(Student, 'id')
