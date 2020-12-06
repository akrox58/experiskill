from services.BaseService import BaseService
from models.Offer import Offer
import datetime, uuid, jsonify, bson

class PricingService(BaseService):

    @classmethod
    def create_offer_record(cls, **kwargs):
        return cls.create_record(Offer, "offer_id", **kwargs)

    @classmethod
    def find_offer_by_offer_id(cls, **payload):
        return cls.get_by_filter(Offer, limit=1, **payload)

    @classmethod
    def get_all_offers(cls):
        return cls.get_all_records(Offer)

    @classmethod
    def update_offer_details(cls, filters, **payload):
        return cls.update_record(Offer, filters, **payload)

    @classmethod
    def get_offers_by_filter(cls, limit=None, **payload):
        return cls.get_by_filter(Offer, limit, **payload)