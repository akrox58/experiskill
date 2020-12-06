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
    location_id = db.UUIDField(required=True)
    class_id =  db.UUIDField(required=True)
    instructor_id =  db.UUIDField(required=True)
    student_id =  db.UUIDField(required=True)
    is_active = db.BooleanField(required=True, default=True)
    value = db.FloatField()
    currency = db.StringField()
    offer_type = db.StringField(choices=('Referral', 'Coupon', 'Offer'), required=True)
    max_count = db.IntField(required=True)
    redeemed_count = db.IntField(default=0)