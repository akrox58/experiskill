from flask import jsonify, make_response
from flask_restful import fields, marshal_with, reqparse, Resource
from hashlib import md5
import json
from utils.helper import *
from services.InstructorService import *
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
class InstructorResource(Resource):
    def __init__(self):
        self.instructor_service = InstructorService()

    def get(self, instructor_id=None):
        if not instructor_id:
            instructor = self.instructor_service.get_all_instructors()
        else:
            if not is_valid_uuid(instructor_id):
                return make_response({"statusCode": 409, "message": "Invalid instructor id"}, 409)
            instructor = self.instructor_service.find_instructor_by_instructor_id(**{"instructor_id": instructor_id})
        return make_response(instructor, 200)

    @jwt_required
    def patch(self, instructor_id):
        email_from_jwt = get_jwt_identity()
        reg_parser = reqparse.RequestParser()
        reg_parser.add_argument('fname', type=str)
        reg_parser.add_argument('lname', type=str)
        reg_parser.add_argument('username', type=str)
        reg_parser.add_argument('password', type=str)
        reg_parser.add_argument('email', type=str)
        reg_parser.add_argument('instructor_id', type=str)
        reg_parser.add_argument('is_active', type=bool)
        body = strip_payload(reg_parser.parse_args())
        if not is_valid_uuid(instructor_id):
            return make_response({"statusCode": 409, "message": "Invalid instructor id"}, 409)
        found_user = self.instructor_service.find_instructor_by_instructor_id(**{"instructor_id": instructor_id})
        if not found_user:
            return make_response({"statusCode": 409, "message": "Instructor could not be identified"}, 409)
        found_user = json.loads(found_user)
        if email_from_jwt != found_user["username"]:
            return make_response({"statusCode": 401, "message": "bad credentials"}, 401)

        if body:
            self.instructor_service.update_instructor_profile({"instructor_id": instructor_id}, **body)

        return make_response({"statusCode": 200, "message": "Instructor successfully updated"}, 200)

    def delete(self, instructor_id):
        if not is_valid_uuid(instructor_id):
            return make_response({"statusCode": 409, "message": "Invalid instructor id"}, 409)
        found_user = self.instructor_service.find_instructor_by_instructor_id(**{"instructor_id": instructor_id})
        if not found_user:
            return make_response({"statusCode": 409, "message": "Instructor could not be identified"}, 409)
        payload = {
            "is_active": False
        }
        self.instructor_service.update_instructor_profile({"instructor_id": instructor_id}, **payload)

        return make_response({"statusCode": 200, "message": "Instructor successfully deactivated"}, 200)