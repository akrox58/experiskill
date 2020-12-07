from services.BaseService import BaseService
from models.ClassSession import ClassSession
from models.Review import Review
import datetime, uuid, jsonify, bson


class ClassSessionService(BaseService):

    @classmethod
    def create_class_session_record(cls, **kwargs):
        return cls.create_record(ClassSession, "class_session_id", **kwargs)

    @classmethod
    def find_class_session_by_class_session_id(cls, **payload):
        return cls.get_by_filter(ClassSession, limit=1, **payload)

    @classmethod
    def get_all_class_sessions(cls):
        return cls.get_all_records(ClassSession)

    @classmethod
    def find_class_sessions_by_params(cls, limit=None, **payload):
        return cls.get_by_filter(ClassSession, limit, **payload)

    @classmethod
    def find_class_sessions_by_params_and_paginate(cls, limit=1, **payload):
        return cls.get_by_filter_and_paginate(ClassSession, limit, **payload)

    @classmethod
    def update_class_session_details(cls, filters, **payload):
        return cls.update_record(ClassSession, filters, **payload)