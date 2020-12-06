from services.BaseService import BaseService
from models.Location import Location
from models.PaymentMethod import PaymentMethod
import datetime, uuid, jsonify, bson


class LocationService(BaseService):

    """ Inserting multiple location records or just a single location record"""
    @classmethod
    def create_location_record(cls, **kwargs):
        cls.create_record(Location, "location_id", **kwargs)
        return {"statusCode": 200, "message": "successfully inserted record"}

    @classmethod
    def get_all_locations(cls):
        return cls.get_all_records(Location)

    @classmethod
    def find_location_by_location_id(cls, **payload):
        return cls.get_by_filter(Location, limit=1, **payload)

    @classmethod
    def find_location_by_params(cls, limit=None, **payload):
        return cls.get_by_filter(Location, limit, **payload)

    @classmethod
    def update_location_profile(cls, filters, **payload):
        return cls.update_record(Location, filters, **payload)