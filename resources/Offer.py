from flask import jsonify, make_response
from flask_restful import fields, marshal_with, reqparse, Resource
from hashlib import md5
import json
from bson import ObjectId
from services.ClassService import ClassService
from services.InstructorService import InstructorService
from services.StudentService import StudentService
from services.PricingService import PricingService
from services.LocationService import LocationService
from utils.helper import *

""" 
Body
{
    "description": "offer description",
    "value": 5,
    "offer_type": "Referral",
    "max_count": 100,
    "currency": "USD",
    "instructor_id": "instructorId",
    "location_id": "locationId",
    "class_id": "classId",
    "student_id": "studentId"
}
"""

class OfferResource(Resource):
    def __init__(self):
        self.offer_service = PricingService()
        self.class_service = ClassService()
        self.student_service = StudentService()
        self.location_service = LocationService()
        self.instructor_service = InstructorService()

    def get(self, offer_id=None):
        if not offer_id:
            result = self.offer_service.get_all_offers()
        else:
            result = self.offer_service.find_offer_by_offer_id(**{"offer_id": offer_id})
        return make_response(result, 200)

    def post(self):
        reg_parser = reqparse.RequestParser()
        reg_parser.add_argument('description', type=str)
        reg_parser.add_argument('instructor_id', type=str)
        reg_parser.add_argument('student_id', type=str)
        reg_parser.add_argument('location_id', type=str)
        reg_parser.add_argument('class_id', type=str)
        reg_parser.add_argument('offer_type', type=str)
        reg_parser.add_argument('max_count', type=int)
        reg_parser.add_argument('redeemed_count', type=int)
        reg_parser.add_argument('value', type=int)
        reg_parser.add_argument('currency', type=str)
        body = strip_payload(reg_parser.parse_args())
        found_offer = self.offer_service.get_offers_by_filter(limit=1, **body)
        if found_offer:
            return make_response({"statusCode": 400, "message": "Offers with these details already exist"}, 400)
        found_class =  self.class_service.get_classes_by_filter(limit=1, **{"class_id": body["class_id"]})
        if not found_class:
            return make_response({"statusCode": 400, "message": "Unidentified Class"}, 400)
        found_location = self.location_service.find_location_by_location_id(**{"location_id": body["location_id"]})
        if not found_location:
            return make_response({"statusCode": 400, "message": "Unidentified location"}, 400)
        found_instructor = self.instructor_service.find_instructor_by_instructor_id(**{"instructor_id": body["instructor_id"]})
        if not found_instructor:
            return make_response({"statusCode": 400, "message": "Unidentified instructor"}, 400)
        found_student = self.student_service.find_student_by_student_id(**{"student_id": body["student_id"]})
        if not found_student:
            return make_response({"statusCode": 400, "message": "Unidentified student"}, 400)
        self.offer_service.create_offer_record(**body)
        return make_response({"statusCode": 200, "message": "Offer successfully added"}, 200)

    def patch(self, offer_id):
        reg_parser = reqparse.RequestParser()
        reg_parser.add_argument('description', type=str)
        reg_parser.add_argument('instructor_id', type=str)
        reg_parser.add_argument('student_id', type=str)
        reg_parser.add_argument('location_id', type=str)
        reg_parser.add_argument('class_id', type=str)
        reg_parser.add_argument('offer_type', type=str)
        reg_parser.add_argument('max_count', type=int)
        reg_parser.add_argument('redeemed_count', type=int)
        reg_parser.add_argument('value', type=int)
        reg_parser.add_argument('currency', type=str)
        reg_parser.add_argument('is_active', type=bool)
        body = strip_payload(reg_parser.parse_args())
        if not is_valid_uuid(offer_id):
            return make_response({"statusCode": 409, "message": "Invalid offer id"}, 409)
        found_user = self.offer_service.find_offer_by_offer_id(**{"offer_id": offer_id})
        if not found_user:
            return make_response({"statusCode": 409, "message": "Offer could not be identified"}, 409)
        if body:
            self.offer_service.update_offer_details({"offer_id": offer_id}, **body)
        return make_response({"statusCode": 200, "message": "Offer successfully updated"}, 200)

    def delete(self, offer_id):
        if not is_valid_uuid(offer_id):
            return make_response({"statusCode": 409, "message": "Invalid offer id"}, 409)
        found_class = self.offer_service.find_offer_by_offer_id(**{"offer_id": offer_id})
        if not found_class:
            return make_response({"statusCode": 409, "message": "Offer could not be identified"}, 409)

        payload = {
            "is_active": False
        }

        self.offer_service.update_offer_details({"offer_id": offer_id}, **payload)
        return make_response({"statusCode": 200, "message": "Offer successfully deactivated"}, 200)