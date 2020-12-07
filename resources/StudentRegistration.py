from flask import jsonify, make_response
from flask_restful import fields, marshal_with, reqparse, Resource
from hashlib import md5
from utils.helper import *
from services.StudentService import *
from services.LocationService import *
from flask_jwt_extended import create_access_token
import json

reg_parser = reqparse.RequestParser()
reg_parser.add_argument('email', type=str, required=True)
reg_parser.add_argument('username', type=str, required=True)
reg_parser.add_argument('password', type=str, required=True)
reg_parser.add_argument('fname', type=str, required=True)
reg_parser.add_argument('lname', type=str, required=True)
reg_parser.add_argument('city', type=str, required=True)
reg_parser.add_argument('state', type=str, required=True)
reg_parser.add_argument('zipcode', type=str, required=True)
reg_parser.add_argument('student_id', type=str)
""" 
Body
{
    "email": "akshaya@email.com",
    "username": "akrox58",
    "password": "asfdasf",
    "fname": "Akshaya",
    "lname": "Kumar",
    "city": "Santa Clara",
    "state": "CA",
    "zipcode": 95051
}
"""

class StudentRegistrationResource(Resource):
    def __init__(self):
        self.student_service = StudentService()
        self.location_service = LocationService()

    def post(self):
        body = strip_payload(reg_parser.parse_args())
        found_user =  self.student_service.find_student_by_student_id(**{"username": body["username"]})
        if found_user:
            return make_response({"statusCode": 400, "message": "Account with this username already exists"}, 400)
        location_details = self.location_service.find_location_by_params(limit = 1, **{"city": body["city"], "state": body["state"], "zipcode": body["zipcode"]})
        if not location_details:
            return make_response({"statusCode": 409, "message": "Location could not be identified"}, 409)
        location_details = json.loads(location_details)
        body["location_id"] = location_details["location_id"]["$uuid"]
        del body["city"]
        del body["state"]
        del body["zipcode"]
        hasher = md5()
        password = body["password"].encode('utf-8')
        hasher.update(password)
        password_hash = hasher.hexdigest()
        body["password"] = password_hash
        self.student_service.create_student_record(**body)
        access_token = create_access_token(identity=body["username"])
        return make_response({"access_token": access_token}, 200)