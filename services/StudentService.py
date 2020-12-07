from services.BaseService import BaseService
from models.Student import Student
import datetime, uuid, jsonify, bson


class StudentService(BaseService):

    @classmethod
    def create_student_record(cls, **kwargs):
        return cls.create_record(Student, "student_id", **kwargs)

    @classmethod
    def get_all_students(cls):
        return cls.get_all_records(Student)

    @classmethod
    def find_student_by_student_id(cls, **payload):
        return cls.get_by_filter(Student, limit=1, **payload)

    @classmethod
    def find_student_by_params(cls, limit = None, **payload):
        return cls.get_by_filter(Student, limit=limit, **payload)

    @classmethod
    def update_student_profile(cls, filters, **payload):
        return cls.update_record(Student, filters, **payload)

