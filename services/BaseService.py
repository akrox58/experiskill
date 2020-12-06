
import uuid, datetime, json

class BaseService:

    @classmethod
    def create_record(self, ServiceModel, record_id, **kwargs):
        payload = kwargs
        payload['created_date'] = datetime.datetime.utcnow()
        payload['modified_date'] = datetime.datetime.utcnow()
        payload[record_id] = uuid.uuid4()
        new_record = ServiceModel(**payload)
        new_record.save()
        return {"statusCode": 200, "message": "successfully inserted record"}

    @classmethod
    def get_by_id(self, model, id):
        data = model.objects.get(id=id).first()
        if data is None:
            return {}
        return data.to_json()

    @classmethod
    def get_all_records(self, model):
        data = model.objects.limit(100000)
        if data is None:
            return []
        return data.to_json()

    @classmethod
    def get_by_filter(self, model, limit=1, **payload):
        if not limit:
            data = model.objects.filter(**payload).all()
        elif limit == 1:
            data = model.objects.filter(**payload).first()
        else:
            data = model.objects.filter(**payload).limit(limit)

        if data is None:
            return []
        return data.to_json()

    @classmethod
    def update_record(self, model, filters, **body):
        model.objects.get(**filters).update(**body)
        return {"statusCode": 200, "message": "successfully updated record"}


    @classmethod
    def delete_record(self, model, **filters):
        model.objects.delete_many(**filters)
        return {"statusCode": 200, "message": "successfully deleted record"}


    @classmethod
    def delete_all(self, model):
        model.objects.delete_many()
        return {"statusCode": 200, "message": "successfully deleted records"}