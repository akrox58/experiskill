from flask import jsonify, make_response
from flask_restful import fields, marshal_with, reqparse, Resource
from hashlib import md5
from models.Instructor import Instructor

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
class InstructorRegistrationResource(Resource):
    def __init__(self):
        pass
        self.instructor_service = InstructorService()

    def post(self):
        args = reg_parser.parse_args()
        found_user =  self.instructor_service.find_instructor_by_instructor_id(**{"instructor_id": args.instructor_id})
        if found_user:
            return "Account with this email already exists", 400

        payload = {
            "instructor_id": args.instructor_id,
            "email": args.email,
            "password": args.password,
            "fname": args.fname,
            "lname": args.lname
        }
        self.instructor_service.create_instructor_record(**payload)
        return make_response({"statusCode": 200, "message": "Instructor successfully registered"}, 200)