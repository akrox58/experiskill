from services.BaseService import BaseService
from models.Instructor import Instructor
from models.PaymentMethod import PaymentMethod
import datetime, uuid, jsonify, bson


class InstructorService(BaseService):

    @classmethod
    def create_instructor_record(cls, **kwargs):
        payload = kwargs
        payload['created_date'] = datetime.datetime.utcnow()
        payload['modified_date'] = datetime.datetime.utcnow()
        return cls.create_record(Instructor, **kwargs)

    @classmethod
    def find_instructor_by_instructor_id(cls, **payload):
        return cls.get_by_filter(Instructor, **payload).first()

    @classmethod
    def update_instructor_profile(cls, filters, **payload):
        return cls.update_record(Instructor, filters, **payload)

    @classmethod
    def create_payment_method(cls, **kwargs):
        payload = kwargs
        payload['created_date'] = datetime.datetime.utcnow()
        payload['modified_date'] = datetime.datetime.utcnow()
        return cls.create_record(PaymentMethod, **kwargs)

    @classmethod
    def get_payment_methods(cls, **payload):
        instructor = cls.get_by_filter(PaymentMethod, **payload)
        return instructor

