from flask import jsonify, make_response
from flask_restful import fields, marshal_with, reqparse, Resource
from hashlib import md5
from models.Student import Student
import json
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
class StudentResource(Resource):
    def __init__(self):
        pass
        self.student_service = StudentService()

    def get(self, student_id):
        student = self.student_service.find_student_by_student_id(**{"student_id": student_id})
        result = {
            "first_name": student.fname,
            "last_name": student.lname,
            "student_id": student.student_id,
        }
        return make_response(result, 200)

    def post(self, student_id):
        args = reg_parser.parse_args()
        found_user =  self.student_service.find_student_by_student_id(**{"student_id": student_id})
        if not found_user:
            return "Account with this email does not exist", 400

        payload = {
            "password": args.password
        }

        self.student_service.update_student_profile({"student_id": student_id}, **payload)
        return make_response({"statusCode": 200, "message": "Student successfully updated"}, 200)