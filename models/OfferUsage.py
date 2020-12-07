from database.db import fetch_engine

db = fetch_engine()
from models.Classes import Classes
from models.Instructor import Instructor
from models.Student import Student

class OfferUsage(db.Document):
    created_date = db.DateTimeField(required=True)
    modified_date = db.DateTimeField(required=True)
    offer_usage_id = db.UUIDField(required=True)
    offer_id =  db.UUIDField(required=True)
    class_session_id =  db.UUIDField(required=True)
    class_id =  db.UUIDField(required=True)
    instructor_id =  db.UUIDField(required=True)
    location_id = db.UUIDField(required=True)
    student_id =  db.UUIDField(required=True)
    is_redeemed = db.BooleanField(required=True, default=True)
    value = db.FloatField()
    currency = db.StringField(default="USD")
    offer_type = db.StringField(default="Offer", choices=('Referral', 'Coupon', 'Offer'), required=True)
    redeemed_count = db.IntField(default=1)