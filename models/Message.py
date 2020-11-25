from database.db import fetch_engine

db = fetch_engine()
from models.Classes import Classes
from models.Location import Location

class Instructor(db.Document):
    id = db.UUIDField(required=True)
    created_date = db.DateTimeField(required=True)
    modified_date = db.DateTimeField(required=True)
    Fname = db.StringField(max_length=200, required=True)
    lName = db.StringField(max_length=200)
    user_id = db.StringField(max_length=200, required=True)
    password = db.StringField(max_length=200, required=True)
    location_ids = db.ListField(db.ReferenceField(Location, 'id'))
    class_ids = db.ListField(db.ReferenceField(Classes, 'id'))
    background_verified = db.BooleanField(default=False)