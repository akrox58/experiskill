from flask import Flask
from flask_restful import Api
from database.db import initialize_db
from utils.JSONEncoder import MongoEngineJSONEncoder
from authentication.jwt import initialize_jwt
from resources.Student import StudentResource
from resources.StudentRegistration import StudentRegistrationResource
from resources.StudentPaymentMethod import StudentPaymentMethodResource
from resources.Instructor import InstructorResource
from resources.InstructorRegistration import InstructorRegistrationResource


app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'experiskill',
    'host': 'mongodb://localhost:27017/'
}

app.config['JWT_SECRET_KEY'] = 'EXPERISKILL-ENCODED-KEY'

initialize_db(app)
jwt = initialize_jwt(app)
app.json_encoder = MongoEngineJSONEncoder
api = Api(app)

api.add_resource(StudentRegistrationResource, '/student/register')
api.add_resource(StudentResource, '/student/<string:student_id>')
api.add_resource(StudentPaymentMethodResource, '/student/<string:student_id>/payment-method')
api.add_resource(InstructorRegistrationResource, '/instructor/register')
api.add_resource(InstructorResource, '/instructor/<string:instructor_id>')

if __name__ == '__main__':
    app.run()
