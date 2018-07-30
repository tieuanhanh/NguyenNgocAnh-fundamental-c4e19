from mongoengine import *
import mlab

mlab.connect()

class Service(Document): 
    name = StringField()
    yob = IntField()
    gender = IntField()
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()

new_service = Service(
    name = "T Anh",
    yob = 1995,
    gender = 1,  #0: female
    height = 170,
    phone = "0987654324",
    address = "Hà Đông, Hà Nội",
    status = False  #Fale: available
)


# new_service.save()

