from flask import jsonify, make_response
from flask_restful import fields, marshal_with, reqparse, Resource
from hashlib import md5
import json
from utils.helper import strip_payload
from services.LocationService import *
from flask_jwt_extended import create_access_token

reg_parser = reqparse.RequestParser()
reg_parser.add_argument('location_id', type=str)
reg_parser.add_argument('city', type=str)
reg_parser.add_argument('state', type=str)
reg_parser.add_argument('country', type=str)
reg_parser.add_argument('zipcode', type=int)
reg_parser.add_argument('latitude', type=float)
reg_parser.add_argument('longitude', type=float)

""" 
Body
{
    "location_id": "",
    "city": "Santa Clara",
    "state": "CA",
    "country": "United States",
    "zipcode": 95051,
    "latitude": 37.3598,
    "longitude":  121.9814
}
"""

class LocationResource(Resource):

    def __init__(self):
        self.location_service = LocationService()

    def get(self, location_id=None):
        reg_parser = reqparse.RequestParser()
        reg_parser.add_argument('location_id', type=str)
        reg_parser.add_argument('city', type=str)
        reg_parser.add_argument('state', type=str)
        reg_parser.add_argument('country', type=str)
        reg_parser.add_argument('zipcode', type=int)
        reg_parser.add_argument('latitude', type=float)
        reg_parser.add_argument('longitude', type=float)
        args = strip_payload(reg_parser.parse_args())
        status_code = 200
        if location_id:
            location = self.location_service.find_location_by_location_id(**{"location_id": location_id})
        elif not args:
            location = self.location_service.get_all_locations()
        else:
            location = self.location_service.find_location_by_params(**args)

        if not location:
            status_code = 404
            #make_response does not accept list so we are converting it to a json string
            location = '[]'
            #keeping output consistent with number of records returned
            #if get all records, return [] else single record for a location id then return {}
            if location_id:
                location = {}
        return make_response(location, status_code)

    def post(self):
        reg_parser = reqparse.RequestParser()
        reg_parser.add_argument('location_id', type=str)
        reg_parser.add_argument('city', type=str, required=True)
        reg_parser.add_argument('state', type=str, required=True)
        reg_parser.add_argument('country', type=str, required=True)
        reg_parser.add_argument('zipcode', type=int, required=True)
        reg_parser.add_argument('latitude', type=float, required=True)
        reg_parser.add_argument('longitude', type=float, required=True)
        payload = strip_payload(reg_parser.parse_args())
        location = self.location_service.find_location_by_params(**{"latitude": payload["latitude"], "longitude": payload["longitude"]})
        location = json.loads(location)
        if len(location):
            print(location)
            return make_response({"message":
                                      "Location with latitude"
                                      + str(payload["latitude"])
                                      + " and longitude"
                                      + str(payload["longitude"])
                                      + " already exists",
                                  "statusCode": 409},
                                 409)

        self.location_service.create_location_record(**payload)
        return make_response({"statusCode": 200, "message": "Location successfully created"}, 200)

    def patch(self, location_id):
        reg_parser = reqparse.RequestParser()
        reg_parser.add_argument('location_id', type=str)
        reg_parser.add_argument('city', type=str)
        reg_parser.add_argument('state', type=str)
        reg_parser.add_argument('country', type=str)
        reg_parser.add_argument('zipcode', type=int)
        reg_parser.add_argument('latitude', type=float)
        reg_parser.add_argument('longitude', type=float)
        args = strip_payload(reg_parser.parse_args())
        location =  self.location_service.find_location_by_location_id(**{"location_id": location_id})
        if not location:
            return make_response({"statusCode": 404, "message": "Location not found"}, 404)
        self.location_service.update_location_profile({"location_id": location_id}, **strip_payload(args, strip_ids=True))
        return make_response({"statusCode": 200, "message": "Location successfully updated"}, 200)