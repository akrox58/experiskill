from flask import jsonify, make_response
from flask_restful import fields, marshal_with, reqparse, Resource
from hashlib import md5
from utils.helper import *
from services.InstructorService import *
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

class InstructorLoginResource(Resource):
    def __init__(self):
        self.instructor_service = InstructorService()

    def post(self):
        body = strip_payload(reg_parser.parse_args())
        instructor =  self.instructor_service.find_instructor_by_params(limit=1, **{"username": body["username"]})
        instructor = json.loads(instructor)
        if instructor:
            hasher = md5()
            password = body["password"].encode('utf-8')
            hasher.update(password)
            password_hash = hasher.hexdigest()

            if password_hash == instructor["password"]:
                access_token = create_access_token(identity=body["username"])
                return make_response({"access_token": access_token}, 200)
        return make_response({"statusCode": 401, "message": "Incorrect username/password"}, 401)