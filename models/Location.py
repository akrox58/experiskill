from database.db import fetch_engine

db = fetch_engine()

class Location(db.Document):
    id = db.UUIDField(required=True)
    created_date = db.DateTimeField(required=True)
    modified_date = db.DateTimeField(required=True)
    line1 = db.StringField(max_length=200)
    line2 = db.StringField(max_length=200)
    line3 = db.StringField(max_length=200)
    state = db.StringField(max_length=200)
    country = db.StringField(max_length=200)
    zipcode = db.StringField(max_length=200)
    latitude = db.FloatField()
    longitude = db.FloatField()