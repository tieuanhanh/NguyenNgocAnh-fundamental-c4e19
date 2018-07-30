from mongoengine import *
import mlab
from random import choice, randint
from faker import Faker

mlab.connect()

fake = Faker()

class Customers(Document):
    name = StringField()
    gender = IntField()    # 1 female
    email = StringField()
    phonenumber = StringField()
    job = StringField()
    company = StringField()
    address = StringField()
    status = BooleanField()  # True: have used service 

# for i in range (30):
#     print ("Saving service", i + 1, "..." )
#     new_customer= Customers(
        # name = "Ngoc Anh",
        # gender = 0,
        # email = 'ngocanh.ng95@gmail.com',
        # phonenumber = '01684622437',
        # job = "student",
        # company = "law school",
        # address = "Hoang Mai, Ha Noi",
        # status = False)

    #     name = fake.name(),
    #     gender = randint(0,1),
    #     email = fake.email(),
    #     phonenumber = fake.phone_number(),
    #     job = fake.job(),
    #     company = fake.company(),
    #     address = fake.address(),
    #     status = choice([True, False])
    # )

    # new_customer.save()


