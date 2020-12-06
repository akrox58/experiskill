from flask import jsonify, make_response
from flask_restful import fields, marshal_with, reqparse, Resource
from hashlib import md5
import json
from bson import ObjectId
from services.ClassService import ClassService
from services.InstructorService import InstructorService
from services.LocationService import LocationService
from utils.helper import *

""" 
Body
{
    "description": "class description",
    "instructor_id": "afsfasd",
    "location_id": "asfdasf",
    "class_level": 1
}
"""

class ClassResource(Resource):
    def __init__(self):
        self.class_service = ClassService()
        self.location_service = LocationService()
        self.instructor_service = InstructorService()

    def get(self, class_id=None):
        if not class_id:
            result = self.class_service.get_all_classes()
        else:
            result = self.class_service.find_class_by_class_id(**{"class_id": class_id})
        return make_response(result, 200)

    def post(self):
        reg_parser = reqparse.RequestParser()
        reg_parser.add_argument('description', type=str)
        reg_parser.add_argument('instructor_id', type=str)
        reg_parser.add_argument('location_id', type=str)
        reg_parser.add_argument('format', type=str)
        reg_parser.add_argument('class_level', type=int)
        body = strip_payload(reg_parser.parse_args())
        found_class =  self.class_service.get_classes_by_filter(limit=1, **body)
        if found_class:
            return make_response({"statusCode": 400, "message": "Class with these details already exist"}, 400)
        found_instructor = self.instructor_service.find_instructor_by_instructor_id(**{"instructor_id": body["instructor_id"]})
        if not found_instructor:
            return make_response({"statusCode": 400, "message": "Unidentified instructor"}, 400)
        found_location = self.location_service.find_location_by_location_id(**{"location_id": body["location_id"] })
        if not found_location:
            return make_response({"statusCode": 400, "message": "Unidentified location"}, 400)
        self.class_service.create_class_record(**body)
        return make_response({"statusCode": 200, "message": "Class successfully added"}, 200)

    def patch(self, class_id):
        reg_parser = reqparse.RequestParser()
        reg_parser.add_argument('description', type=str)
        reg_parser.add_argument('instructor_id', type=str)
        reg_parser.add_argument('location_id', type=str)
        reg_parser.add_argument('format', type=str)
        reg_parser.add_argument('class_level', type=int)
        reg_parser.add_argument('is_active', type=bool)
        body = strip_payload(reg_parser.parse_args())
        if not is_valid_uuid(class_id):
            return make_response({"statusCode": 409, "message": "Invalid class id"}, 409)
        found_user = self.class_service.find_class_by_class_id(**{"class_id": class_id})
        if not found_user:
            return make_response({"statusCode": 409, "message": "Class could not be identified"}, 409)
        if body:
            self.class_service.update_class_details({"class_id": class_id}, **body)
        return make_response({"statusCode": 200, "message": "Class successfully updated"}, 200)

    def delete(self, class_id):
        if not is_valid_uuid(class_id):
            return make_response({"statusCode": 409, "message": "Invalid class id"}, 409)
        found_class = self.class_service.find_class_by_class_id(**{"class_id": class_id})
        if not found_class:
            return make_response({"statusCode": 409, "message": "Class could not be identified"}, 409)

        payload = {
            "is_active": False
        }

        self.class_service.update_class_details({"class_id": class_id}, **payload)
        return make_response({"statusCode": 200, "message": "Class successfully deactivated"}, 200)