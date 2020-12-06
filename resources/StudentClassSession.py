from flask import jsonify, make_response
from flask_restful import fields, marshal_with, reqparse, Resource
from hashlib import md5
import json
from services.StudentService import *
from services.ClassSessionService import *
from flask_jwt_extended import create_access_token

reg_parser = reqparse.RequestParser()
reg_parser.add_argument('instructor_id', type=str)
reg_parser.add_argument('class_cost', type=float)
reg_parser.add_argument('currency', type=str)
reg_parser.add_argument('format', type=str)
reg_parser.add_argument('class_level', type=int)
reg_parser.add_argument('payment_method', type=int)
reg_parser.add_argument('class_date', type=str)


class StudentClassSessionResource(Resource):
    def __init__(self):
        self.class_session_service = ClassSessionService()

    def get(self, student_id, class_session_id=None):
        class_sessions = self.class_session_service.find_class_sessions_by_params(**{"student_id": student_id, "class_session_id": class_session_id})
        return make_response(class_sessions, 200)


    def post(self, student_id):
        args = reg_parser.parse_args()
        payload = {
            "instructor_id": args.instructor_id,
            "student_id": student_id,
            "class_cost": args.class_cost,
            "currency": args.currency,
            "format": args.format,
            "class_level": args.class_level,
            "payment_method": args.payment_method,
            "class_date": args.class_date
        }
        self.class_session_service.create_class_session_record(**payload)
        return make_response({"statusCode": 200, "message": "Student successfully registered"}, 200)

    def patch(self, class_session_id):
        args = reg_parser.parse_args()
        found_user =  self.class_session_service.find_class_session_by_class_session_id(**{"class_session_id": class_session_id})

        payload = {
            "class_session_id": class_session_id
        }

        self.class_session_service.update_class_session_details({"class_session_id": class_session_id}, **payload)
        return make_response({"statusCode": 200, "message": "StudentClassSession successfully updated"}, 200)