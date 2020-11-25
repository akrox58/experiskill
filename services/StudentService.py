from services.BaseService import BaseService
from models.Student import Student
from models.PaymentMethod import PaymentMethod
import datetime, uuid, jsonify, bson


class StudentService(BaseService):

    @classmethod
    def create_student_record(cls, **kwargs):
        payload = kwargs
        payload['created_date'] = datetime.datetime.utcnow()
        payload['modified_date'] = datetime.datetime.utcnow()
        return cls.create_record(Student, **kwargs)

    @classmethod
    def find_student_by_student_id(cls, **payload):
        return cls.get_by_filter(Student, **payload).first()

    @classmethod
    def update_student_profile(cls, filters, **payload):
        return cls.update_record(Student, filters, **payload)

    @classmethod
    def create_payment_method(cls, **kwargs):
        payload = kwargs
        payload['created_date'] = datetime.datetime.utcnow()
        payload['modified_date'] = datetime.datetime.utcnow()
        return cls.create_record(PaymentMethod, **kwargs)

    @classmethod
    def get_payment_methods(cls, **payload):
        student = cls.get_by_filter(PaymentMethod, **payload)
        return student

