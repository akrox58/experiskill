from flask import jsonify, make_response
from flask_restful import fields, marshal_with, reqparse, Resource
from hashlib import md5
import math
import json
from bson import ObjectId
from services.ClassSessionService import ClassSessionService
from services.InstructorService import InstructorService
from services.LocationService import LocationService
from services.ClassService import ClassService
from services.StudentService import StudentService
from services.PricingService import PricingService
from utils.helper import *

""" 
Body
{
    "description": "class description",
    "class_id": "afsfasd",
    "student_id": "afsfasd",
    "instructor_id": "afsfasd",
    "location_id": "asfdasf",
    "class_cost": 1,
    "class_date": "2020-12-06 16:30:49.134899",
    "duration": 100
}
"""

class ClassSessionResource(Resource):
    def __init__(self):
        self.class_session_service = ClassSessionService()
        self.location_service = LocationService()
        self.instructor_service = InstructorService()
        self.student_service = StudentService()
        self.class_service = ClassService()
        self.pricing_service = PricingService()

    def get(self):
        reg_parser = reqparse.RequestParser()
        reg_parser.add_argument('location', type=str)
        reg_parser.add_argument('total_cost')
        reg_parser.add_argument('student', type=str)
        reg_parser.add_argument('instructor', type=str)
        reg_parser.add_argument('offer', type=str)
        body = strip_payload(reg_parser.parse_args())
        result = {}
        total = 0
        if "total_cost" in body:
            result = self.class_session_service.find_class_sessions_and_paginate()
            for page_number in result.iter_pages():
                page_result = self.class_session_service.paginate_class_session(page_number, 1)
                for doc in page_result.items:
                    print(doc.total)
                    total = float(doc.total) + total
        return make_response({"total_cost": total, "message": "total cost for location"}, 200)

    def post(self):
        reg_parser = reqparse.RequestParser()
        reg_parser.add_argument('class_session_id', type=str)
        reg_parser.add_argument('offer_usage_id', type=str, required=True)
        reg_parser.add_argument('class_id', type=str, required=True)
        reg_parser.add_argument('student_id', type=str, required=True)
        reg_parser.add_argument('offer_id', type=str)
        reg_parser.add_argument('count', type=int, default=1)

        body = strip_payload(reg_parser.parse_args())
        found_class_sessions =  self.class_session_service.find_class_sessions_by_params(**{"class_id": body["class_id"]})
        class_sessions = json.loads(found_class_sessions)
        already_scheduled_classes = 0
        for class_session in class_sessions:
            already_scheduled_classes = class_session["class_count"] + already_scheduled_classes

        found_student = self.student_service.find_student_by_student_id(**{"student_id": body["student_id"] })
        if not found_student:
            return make_response({"statusCode": 400, "message": "Unidentified student"}, 400)

        found_class = self.class_service.find_class_by_class_id(**{"class_id": body["class_id"]})
        if not found_class:
            return make_response({"statusCode": 400, "message": "Unidentified class"}, 400)

        offer_details = {}
        if "offer_id" in body:
            offer = self.pricing_service.find_offer_by_offer_id(**{"offer_id": body["offer_id"]})
            if not offer:
                return make_response({"statusCode": 400, "message": "Unidentified offer"}, 400)
            offer_details = json.loads(offer)
            found_offers_usages = self.pricing_service.find_offer_usage_by_params(**{"offer_id": body["offer_id"]})
            offers_usages = json.loads(found_offers_usages)
            already_used_offers = 0
            for offer_usage in offers_usages:
                if "redeemed_count" in offer_usage:
                    already_used_offers = offer_usage["redeemed_count"] + already_used_offers
            if already_used_offers + 1 > offer_details["max_count"]:
                return make_response({"statusCode": 409, "message": "Offer cannot be applied. Offer used too many times."}, 409)

        class_details = json.loads(found_class)
        if already_scheduled_classes >= class_details["class_count"]:
            return make_response({"statusCode": 409, "message": "All classes booked already. Sorry!"}, 400)

        body["instructor_id"] = class_details["instructor_id"]["$uuid"]
        body["location_id"] = class_details["location_id"]["$uuid"]
        discount = 0
        if offer_details:
            discount = offer_details["value"]
        if class_details["class_cost"] - discount > 0:
            total = class_details["class_cost"] - discount
        else:
            total = 0
        body["discount"] = discount
        body["total"] = total
        body["class_cost"] = class_details["class_cost"]
        body["duration"] = class_details["duration"]

        offer_body = {
            "offer_usage_id": body["offer_usage_id"],
            "offer_id": body["offer_id"],
            "class_id": body["class_id"],
            "class_session_id": body["class_session_id"],
            "student_id": body["student_id"],
            "instructor_id": body["instructor_id"],
            "location_id": body["location_id"],
            "value": offer_details["value"],
            "redeemed_count": body["count"]
        }

        body["class_count"] = body["count"]
        del body["offer_usage_id"]
        del body["count"]

        self.class_session_service.create_class_session_record(**body)
        self.pricing_service.create_offer_usage_record(**offer_body)
        return make_response({"statusCode": 200, "message": "ClassSession successfully added", "class-data": body, "offer-data": offer_body}, 200)