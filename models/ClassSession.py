from database.db import fetch_engine

db = fetch_engine()

from models.Classes import Classes
from models.Instructor import Instructor
from models.Student import Student
from models.PaymentMethod import PaymentMethod
from models.Offer import Offer

class ClassSession(db.Document):
    id = db.UUIDField(required=True)
    created_date = db.DateTimeField(required=True)
    modified_date = db.DateTimeField(required=True)
    class_id = db.ReferenceField(Classes, 'id')
    instructor_id = db.ReferenceField(Instructor, 'id')
    student_id = db.ReferenceField(Student, 'id')
    class_cost = db.FloatField()
    currency = db.StringField(choices=('USD'), description='only usd for now')
    payment_method = db.ReferenceField(PaymentMethod, 'id')
    class_date = db.DateTimeField()
    duration = db.IntField(description = "number of minutes of the class")
    offer_id = db.ReferenceField(Offer, 'id')
