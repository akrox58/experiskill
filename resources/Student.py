from flask import jsonify, make_response
from flask_restful import fields, marshal_with, reqparse, Resource
from hashlib import md5
import json
from utils.helper import *
from services.StudentService import *
from flask_jwt_extended import create_access_token
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)


""" 
Body
{
    "email": "akshaya@email.com",
    "username": "akrox61",
    "password": "asfdasf",
    "fname": "Akshaya",
    "lname": "Kumar"
}
"""
class StudentResource(Resource):
    def __init__(self):
        self.student_service = StudentService()

    def get(self, student_id=None):
        if not student_id:
            student = self.student_service.get_all_students()
        else:
            if not is_valid_uuid(student_id):
                return make_response({"statusCode": 409, "message": "Invalid student id"}, 409)
            student = self.student_service.find_student_by_student_id(**{"student_id": student_id})
        return make_response(student, 200)

    @jwt_required
    def patch(self, student_id):
        email_from_jwt = get_jwt_identity()
        reg_parser = reqparse.RequestParser()
        reg_parser.add_argument('fname', type=str)
        reg_parser.add_argument('lname', type=str)
        reg_parser.add_argument('username', type=str)
        reg_parser.add_argument('password', type=str)
        reg_parser.add_argument('email', type=str)
        reg_parser.add_argument('is_active', type=bool)
        body = strip_payload(reg_parser.parse_args())
        if not is_valid_uuid(student_id):
            return make_response({"statusCode": 409, "message": "Invalid student id"}, 409)
        found_user = self.student_service.find_student_by_student_id(**{"student_id": student_id})
        if not found_user:
            return make_response({"statusCode": 409, "message": "Student could not be identified"}, 409)
        found_user = json.loads(found_user)
        if email_from_jwt != found_user["username"]:
            return make_response({"statusCode": 401, "message": "bad credentials"}, 401)

        if body:
            self.student_service.update_student_profile({"student_id": student_id}, **body)

        return make_response({"statusCode": 200, "message": "Student successfully updated"}, 200)

    def delete(self, student_id):
        if not is_valid_uuid(student_id):
            return make_response({"statusCode": 409, "message": "Invalid student id"}, 409)
        found_user = self.student_service.find_student_by_student_id(**{"student_id": student_id})
        if not found_user:
            return make_response({"statusCode": 409, "message": "Student could not be identified"}, 409)

        payload = {
            "is_active": False
        }

        self.student_service.update_student_profile({"student_id": student_id}, **payload)
        return make_response({"statusCode": 200, "message": "Student successfully deactivated"}, 200)