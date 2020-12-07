from database.db import fetch_engine

db = fetch_engine()
from models.Location import Location
from models.Instructor import Instructor

class Classes(db.Document):
    created_date = db.DateTimeField(required=True)
    modified_date = db.DateTimeField(required=True)
    class_id = db.UUIDField(required=True)
    instructor_id = db.UUIDField(required=True)
    location_id = db.UUIDField(required=True)
    description = db.StringField(description='class description')
    format = db.StringField(choices=('OFFLINE','ONLINE'), default='OFFLINE')
    class_level = db.IntField(choices=(1,2,3,4,5), description='difficulty level')
    class_cost = db.FloatField(required=True)
    is_active = db.BooleanField(default=True)
    duration = db.IntField(required=True, description="number of minutes of the class")
    class_count = db.IntField(default=1, required=True, description="number of minutes of the class")