from database.db import fetch_engine

db = fetch_engine()
from models.Classes import Classes
from models.Instructor import Instructor
from models.Student import Student

class Offer(db.Document):
    created_date = db.DateTimeField(required=True)
    modified_date = db.DateTimeField(required=True)
    description = db.StringField(description='description')
    offer_id =  db.UUIDField(required=True)
    location_id = db.UUIDField()
    class_id =  db.UUIDField()
    instructor_id =  db.UUIDField(required=True)
    student_id =  db.UUIDField()
    is_active = db.BooleanField(required=True, default=True)
    value = db.FloatField()
    currency = db.StringField(default="USD")
    offer_type = db.StringField(default="Offer", choices=('Referral', 'Coupon', 'Offer'), required=True)
    max_count = db.IntField(default=100, required=True)