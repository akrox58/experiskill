from flask import jsonify, make_response
from flask_restful import reqparse, Resource

from services.StudentService import *

reg_parser = reqparse.RequestParser()
reg_parser.add_argument('card_number', type=str)
reg_parser.add_argument('provider', type=str)


class StudentPaymentMethodResource(Resource):
    def __init__(self):
        self.student_service = StudentService()

    def get(self, student_id, payment_method_id=None):
        if payment_method_id:
            payments = self.student_service.get_payment_methods(**{"student_id": student_id})
        payments = self.student_service.get_payment_methods(**{"student_id": student_id})
        list_of_payments = []
        for payment in payments:
            if payment:
                payment_method = {
                    "card_number": payment.card_number,
                    "provider": payment.provider,
                }
                list_of_payments.append(payment_method)

        return make_response(payments, 200)

    def post(self, student_id):
        args = reg_parser.parse_args()
        payment = self.student_service.get_payment_methods(**{"student_id": student_id})
        payload = {
            "student_id": student_id,
            "card_number": args.card_number,
            "provider": args.provider
        }

        self.student_service.create_payment_method(**payload)
        return make_response({"statusCode": 200, "message": "Payment Method successfully added"}, 200)

    def patch(self, student_id):
        args = reg_parser.parse_args()

        payload = {
            "card_number": args.card_number,
            "provider": args.provider
        }

        self.student_service.create_payment_method(**payload)
        return make_response({"statusCode": 200, "message": "Payment Method successfully added"}, 200)

    def delete(self, student_id):
        args = reg_parser.parse_args()

        payload = {
            "card_number": args.card_number,
            "provider": args.provider
        }

        self.student_service.create_payment_method(**payload)
        return make_response({"statusCode": 200, "message": "Payment Method successfully added"}, 200)