from flask import jsonify, make_response
from flask_restful import fields, marshal_with, reqparse, Resource
from hashlib import md5
from services.BaseService import BaseService
from models.Classes import Classes
from models.ClassSession import ClassSession
from models.Student import Student
from models.Location import Location
from models.Instructor import Instructor
from models.PaymentMethod import PaymentMethod
from models.Offer import Offer
from models.Review import Review

import json
from bson import ObjectId
from utils.helper import *

class ResetResource(Resource):
    def __init__(self):
        self.service = BaseService()
        pass

    def delete(self):
        self.service.delete_all(Offer)
        self.service.delete_all(Review)
        self.service.delete_all(ClassSession)
        self.service.delete_all(Classes)
        self.service.delete_all(PaymentMethod)
        self.service.delete_all(Instructor)
        self.service.delete_all(Student)
        self.service.delete_all(Location)
        return make_response({"statusCode": 200, "message": "Database successfully reset"}, 200)