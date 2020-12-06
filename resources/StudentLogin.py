from flask import jsonify, make_response
from flask_restful import fields, marshal_with, reqparse, Resource
from hashlib import md5
from utils.helper import *
from services.StudentService import *
from flask_jwt_extended import create_access_token
import json

reg_parser = reqparse.RequestParser()
reg_parser.add_argument('username', type=str, required=True)
reg_parser.add_argument('password', type=str, required=True)

""" 
Body
{
    "username": "username",
    "password": "asfdasf"
}
"""

class StudentLoginResource(Resource):
    def __init__(self):
        self.student_service = StudentService()

    def post(self):
        body = strip_payload(reg_parser.parse_args())
        student =  self.student_service.find_student_by_params(limit=1, **{"username": body["username"]})
        student = json.loads(student)
        if student:
            hasher = md5()
            password = body["password"].encode('utf-8')
            hasher.update(password)
            password_hash = hasher.hexdigest()

            print(student, password, password_hash, body)
            if password_hash == student["password"]:
                access_token = create_access_token(identity=body["username"])
                return make_response({"access_token": access_token}, 200)

        return make_response({"statusCode": 401, "message": "Incorrect username/password"}, 401)