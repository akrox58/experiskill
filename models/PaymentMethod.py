from database.db import fetch_engine

db = fetch_engine()

class PaymentMethod(db.Document):
    student_id  = db.StringField(required=True)
    card_number = db.StringField(required=True, max_length = 4, description = "last four digits of a card")
    created_date = db.DateTimeField(required=True)
    modified_date = db.DateTimeField(required=True)
    provider = db.StringField()