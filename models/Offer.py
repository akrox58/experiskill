from database.db import fetch_engine

db = fetch_engine()
from models.Classes import Classes
from models.Instructor import Instructor
from models.Student import Student

class Offer(db.Document):
    id = db.UUIDField(required=True)
    created_date = db.DateTimeField(required=True)
    modified_date = db.DateTimeField(required=True)
    description = db.StringField(description='description')
    class_id = db.ReferenceField(Classes, 'id')
    instructor_id = db.ReferenceField(Instructor, 'id')
    student_id = db.ReferenceField(Student, 'id')
    offer_start_date = db.DateTimeField()
    offer_expiry_date = db.DateTimeField()
    is_active = db.BooleanField(required=True, default=True)
    value = db.FloatField()
    offer_type = db.StringField(choices=('Referral', 'Coupon', 'Offer'))
    max_count = db.IntField(required=True)
    redeemed_count = db.IntField(default=0)