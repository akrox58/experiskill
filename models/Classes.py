from database.db import fetch_engine

db = fetch_engine()
from models.Location import Location

class Classes(db.Document):
    id = db.UUIDField(required=True)
    created_date = db.DateTimeField(required=True)
    modified_date = db.DateTimeField(required=True)
    #location_id = db.StringField(ReferenceField(Location, 'id'))
    description = db.StringField(description='class description')
    format = db.StringField(choices=('OFFLINE','ONLINE'))
    class_level = db.IntField(choices=(1,2,3,4,5), description='difficulty level')