from flask import jsonify, make_response
from flask_restful import fields, marshal_with, reqparse, Resource
from hashlib import md5
from models.Student import Student

from services.StudentService import *
from flask_jwt_extended import create_access_token

reg_parser = reqparse.RequestParser()
reg_parser.add_argument('card_number', type=str)
reg_parser.add_argument('provider', type=str)


class StudentPaymentMethodResource(Resource):
    def __init__(self):
        pass
        self.student_service = StudentService()

    def get(self, student_id):
        payments = self.student_service.get_payment_methods(**{"student_id": student_id})
        list_of_payments = []
        for payment in payments:
            if payment:
                payment_method = {
                    "card_number": payment.card_number,
                    "provider": payment.provider,
                }
                list_of_payments.append(payment_method)

        return make_response({"card_number": "2345", "provider": "visa"}, 200)

    def post(self, student_id):
        args = reg_parser.parse_args()

        payload = {
            "student_id": student_id,
            "card_number": args.card_number,
            "provider": args.provider
        }

        self.student_service.create_payment_method(**payload)
        return make_response({"statusCode": 200, "message": "Payment Method successfully added"}, 200)


    def put(self):
        return True