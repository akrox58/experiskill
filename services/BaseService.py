
import uuid, datetime

class BaseService:

    @classmethod
    def create_record(self, ServiceModel, **kwargs):
        new_record = ServiceModel(**kwargs)
        new_record.save(validate=False)
        return {"statusCode": 200, "message": "successfully inserted record"}

    @classmethod
    def get_by_id(self, model, id):
        return model.objects.get(id=id).first()

    @classmethod
    def get_by_filter(self, model, **payload):
        return model.objects.filter(**payload).all()


    @classmethod
    def update_record(self, model, filters, **body):
        model.objects.get(**filters).update(**body)
        return {"statusCode": 200, "message": "successfully updated record"}