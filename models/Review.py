from database.db import fetch_engine

db = fetch_engine()
from models.Classes import Classes
from models.Instructor import Instructor
from models.Student import Student


class Review(db.Document):
    created_date = db.DateTimeField(required=True)
    modified_date = db.DateTimeField(required=True)
    description = db.StringField(description='description')
    rating = db.IntField(choices=(1,2,3,4,5), description='star rating')
    review_id = db.UUIDField(required=True)
    class_id = db.UUIDField(required=True)
    instructor_id = db.UUIDField(required=True)
    student_id = db.UUIDField(required=True)
    is_active = db.BooleanField(default=True)