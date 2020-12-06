from services.BaseService import BaseService
from models.Instructor import Instructor
from models.PaymentMethod import PaymentMethod
import datetime, uuid, jsonify, bson


class InstructorService(BaseService):

    @classmethod
    def create_instructor_record(cls, **kwargs):
        return cls.create_record(Instructor, "instructor_id", **kwargs)

    @classmethod
    def get_all_instructors(cls):
        return cls.get_all_records(Instructor)

    @classmethod
    def find_instructor_by_instructor_id(cls, **payload):
        return cls.get_by_filter(Instructor, limit=1, **payload)

    @classmethod
    def find_instructor_by_params(cls, **payload):
        return cls.get_by_filter(Instructor, limit=None, **payload)

    @classmethod
    def update_instructor_profile(cls, filters, **payload):
        return cls.update_record(Instructor, filters, **payload)


