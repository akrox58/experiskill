from database.db import fetch_engine

db = fetch_engine()
from models.Location import Location

class Instructor(db.Document):
    created_date = db.DateTimeField(required=True)
    modified_date = db.DateTimeField(required=True)
    fname = db.StringField(required=True)
    lname = db.StringField()
    instructor_id = db.UUIDField(required=True)
    username = db.StringField(required=True)
    email = db.StringField(required=True)
    password = db.StringField(required=True)
    password_hash = db.StringField()
    location_id = db.UUIDField(required=True)
    background_verified = db.BooleanField(default=False)
    is_active = db.BooleanField(default=True)

