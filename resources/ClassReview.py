from flask import jsonify, make_response
from flask_restful import fields, marshal_with, reqparse, Resource
from hashlib import md5
import json
from bson import ObjectId
from services.ClassService import ClassService
from services.InstructorService import InstructorService
from services.StudentService import StudentService
from utils.helper import *

""" 
Body
{
    "description": "review description",
    "rating": 5,
    "review_id": "classId",
    "instructor_id": "instructorId",
    "class_id": "classId",
    "student_id": "studentId"
}
"""

class ClassReviewResource(Resource):
    def __init__(self):
        self.class_service = ClassService()
        self.student_service = StudentService()
        self.instructor_service = InstructorService()

    def get(self, class_id, review_id=None):
        if not review_id:
            result = self.class_service.get_reviews_by_filter(None, **{"class_id": class_id})
        else:
            result = self.class_service.find_review_by_review_id(**{"review_id": review_id})
        return make_response(result, 200)

    def post(self, class_id):
        reg_parser = reqparse.RequestParser()
        reg_parser.add_argument('description', type=str)
        reg_parser.add_argument('instructor_id', type=str)
        reg_parser.add_argument('student_id', type=str)
        reg_parser.add_argument('rating', type=int)
        body = strip_payload(reg_parser.parse_args())
        body["class_id"] = class_id
        found_class = self.class_service.get_reviews_by_filter(limit=1, **body)
        if found_class:
            return make_response({"statusCode": 400, "message": "Reviews with these details already exist"}, 400)
        found_class =  self.class_service.get_classes_by_filter(limit=1, **{"class_id": class_id})
        if not found_class:
            return make_response({"statusCode": 400, "message": "Class with these details already exist"}, 400)
        found_instructor = self.instructor_service.find_instructor_by_instructor_id(**{"instructor_id": body["instructor_id"]})
        if not found_instructor:
            return make_response({"statusCode": 400, "message": "Unidentified instructor"}, 400)
        found_student = self.student_service.find_student_by_student_id(**{"student_id": body["student_id"]})
        if not found_student:
            return make_response({"statusCode": 400, "message": "Unidentified student"}, 400)
        self.class_service.create_review_record(**body)
        return make_response({"statusCode": 200, "message": "Review successfully added"}, 200)

    def patch(self, class_id, review_id):
        reg_parser = reqparse.RequestParser()
        reg_parser.add_argument('class_review_id', type=str)
        reg_parser.add_argument('description', type=str)
        reg_parser.add_argument('instructor_id', type=str)
        reg_parser.add_argument('student_id', type=str)
        reg_parser.add_argument('rating', type=int)
        reg_parser.add_argument('is_active', type=bool)
        body = strip_payload(reg_parser.parse_args())
        body["class_id"] = class_id
        if not is_valid_uuid(review_id):
            return make_response({"statusCode": 409, "message": "Invalid review id"}, 409)
        found_user = self.class_service.find_review_by_review_id(**{"review_id": review_id})
        if not found_user:
            return make_response({"statusCode": 409, "message": "Review could not be identified"}, 409)
        if body:
            self.class_service.update_review_details({"review_id": review_id}, **body)
        return make_response({"statusCode": 200, "message": "Review successfully updated"}, 200)

    def delete(self, class_id, review_id):
        if not is_valid_uuid(review_id):
            return make_response({"statusCode": 409, "message": "Invalid review id"}, 409)
        found_class = self.class_service.find_review_by_review_id(**{"review_id": review_id})
        if not found_class:
            return make_response({"statusCode": 409, "message": "Review could not be identified"}, 409)

        payload = {
            "is_active": False
        }

        self.class_service.update_review_details({"review_id": review_id}, **payload)
        return make_response({"statusCode": 200, "message": "Review successfully deactivated"}, 200)