from database.db import fetch_engine

db = fetch_engine()

class Location(db.Document):
    created_date = db.DateTimeField(required=True)
    modified_date = db.DateTimeField(required=True)
    location_id = db.UUIDField(required=True)
    city = db.StringField(required=True, max_length=200)
    state = db.StringField(required=True, max_length=200)
    country = db.StringField(max_length=200)
    zipcode = db.IntField(max_length=200)
    latitude = db.FloatField()
    longitude = db.FloatField()
    is_active = db.BooleanField(default = True)