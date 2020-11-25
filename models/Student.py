from database.db import fetch_engine

db = fetch_engine()



class Student(db.Document):
    created_date = db.DateTimeField(required=True)
    modified_date = db.DateTimeField(required=True)
    fname = db.StringField( required=True)
    lname = db.StringField()
    student_id = db.StringField(required=True)
    email = db.StringField(required=True)
    password = db.StringField(required=True)
    password_hash = db.StringField(required=True)
    #location_ids = db.ListField(ReferenceField(Location))
    #background_verified = db.BooleanField(default=False)
