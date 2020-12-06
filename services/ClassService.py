from services.BaseService import BaseService
from models.Classes import Classes
from models.Review import Review
import datetime, uuid, jsonify, bson

class ClassService(BaseService):

    @classmethod
    def create_class_record(cls, **kwargs):
        return cls.create_record(Classes, "class_id", **kwargs)

    @classmethod
    def find_class_by_class_id(cls, **payload):
        return cls.get_by_filter(Classes, limit=1, **payload)

    @classmethod
    def get_all_classes(cls):
        return cls.get_all_records(Classes)

    @classmethod
    def update_class_details(cls, filters, **payload):
        return cls.update_record(Classes, filters, **payload)

    @classmethod
    def get_classes_by_filter(cls, limit=None, **payload):
        return cls.get_by_filter(Classes, limit, **payload)

    @classmethod
    def create_review_record(cls, **kwargs):
        return cls.create_record(Review, "review_id", **kwargs)

    @classmethod
    def find_review_by_review_id(cls, **payload):
        return cls.get_by_filter(Review, limit=1, **payload)

    @classmethod
    def get_all_reviews(cls):
        return cls.get_all_records(Review)

    @classmethod
    def update_review_details(cls, filters, **payload):
        return cls.update_record(Review, filters, **payload)

    @classmethod
    def get_reviews_by_filter(cls, limit=None, **payload):
        return cls.get_by_filter(Review, limit, **payload)


