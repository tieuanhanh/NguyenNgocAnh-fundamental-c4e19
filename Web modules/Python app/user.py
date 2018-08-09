import mlab
from mongoengine import *
from service import Service

mlab.connect()

class User (Document):
    fullname = StringField()
    email = StringField()
    username = StringField()
    password = StringField()
    
class Order(Document):
    service_id = ReferenceField(Service)
    user_id = ReferenceField(User)
    time = DateTimeField()    
    is_accepted = BooleanField()

