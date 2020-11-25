from flask import jsonify, make_response
from flask_restful import fields, marshal_with, reqparse, Resource
from hashlib import md5
from models.Student import Student

from services.StudentService import *
from flask_jwt_extended import create_access_token

reg_parser = reqparse.RequestParser()
reg_parser.add_argument('student_id', type=str)
reg_parser.add_argument('email', type=str)
reg_parser.add_argument('password', type=str)
reg_parser.add_argument('fname', type=str)
reg_parser.add_argument('lname', type=str)


""" 
Body
{
    "student_id": "abc",
    "email": "akshaya@email.com",
    "password": "asfdasf"
    "fnmae": "Akshaya"
    "lnmae": "Kumar
}
"""
class StudentRegistrationResource(Resource):
    def __init__(self):
        pass
        self.student_service = StudentService()

    def post(self):
        args = reg_parser.parse_args()
        found_user =  self.student_service.find_student_by_student_id(**{"student_id": args.student_id})
        if found_user:
            return "Account with this email already exists", 400

        payload = {
            "student_id": args.student_id,
            "email": args.email,
            "password": args.password,
            "fname": args.fname,
            "lname": args.lname
        }
        self.student_service.create_student_record(**payload)
        return make_response({"statusCode": 200, "message": "Student successfully registered"}, 200)