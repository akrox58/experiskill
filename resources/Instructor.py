from flask import jsonify, make_response
from flask_restful import fields, marshal_with, reqparse, Resource
from hashlib import md5
from models.Instructor import Instructor
import json
from services.InstructorService import *
from flask_jwt_extended import create_access_token

reg_parser = reqparse.RequestParser()
reg_parser.add_argument('instructor_id', type=str)
reg_parser.add_argument('email', type=str)
reg_parser.add_argument('password', type=str)
reg_parser.add_argument('fname', type=str)
reg_parser.add_argument('lname', type=str)


""" 
Body
{
    "instructor_id": "abc",
    "email": "akshaya@email.com",
    "password": "asfdasf"
    "fnmae": "Akshaya"
    "lnmae": "Kumar
}
"""
class InstructorResource(Resource):
    def __init__(self):
        pass
        self.instructor_service = InstructorService()

    def get(self, instructor_id):
        instructor = self.instructor_service.find_instructor_by_instructor_id(**{"instructor_id": instructor_id})
        result = {
            "first_name": instructor.fname,
            "last_name": instructor.lname,
            "instructor_id": instructor.instructor_id,
        }
        return make_response(result, 200)

    def post(self, instructor_id):
        args = reg_parser.parse_args()
        found_user =  self.instructor_service.find_instructor_by_instructor_id(**{"instructor_id": instructor_id})
        if not found_user:
            return "Account with this email does not exist", 400

        payload = {
            "password": args.password
        }

        self.instructor_service.update_instructor_profile({"instructor_id": instructor_id}, **payload)
        return make_response({"statusCode": 200, "message": "Instructor successfully updated"}, 200)