from database.db import fetch_engine

db = fetch_engine()
from models.Classes import Classes
from models.Location import Location

class Instructor(db.Document):
    created_date = db.DateTimeField(required=True)
    modified_date = db.DateTimeField(required=True)
    fname = db.StringField(max_length=200, required=True)
    lname = db.StringField(max_length=200)
    instructor_id = db.StringField(max_length=200, required=True)
    email = db.StringField(required=True)
    password = db.StringField(required=True)
    password_hash = db.StringField(required=True)
    #location_ids = db.ListField(ReferenceField(Location, 'id'))
    #class_ids = db.ListField(ReferenceField(Classes, 'id'))
    background_verified = db.BooleanField(default=False)
