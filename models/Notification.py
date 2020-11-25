from database.db import fetch_engine

db = fetch_engine()
from models.Classes import Classes
from models.Instructor import Instructor
from models.Student import Student

class Notifications(db.Document):
    id = db.UUIDField(required=True)
    created_date = db.DateTimeField(required=True)
    modified_date = db.DateTimeField(required=True)
    status = db.StringField(choices=('Scheduled', 'Sent'))
    class_id = db.ReferenceField(Classes, 'id')
    instructor_id = db.ReferenceField(Instructor, 'id')
    student_id = db.ReferenceField(Student, 'id')
    notification_date = db.DateTimeField()
    notification_type = db.StringField(required=True)

