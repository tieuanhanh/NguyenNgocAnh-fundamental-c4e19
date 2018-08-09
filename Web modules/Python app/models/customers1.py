from mongoengine import *
import mlab

mlab.connect()

class Customers(Document):
    name = StringField()
    gender = IntField()    # 1 female
    email = StringField()
    phonenumber = IntField()
    job = StringField()
    company = StringField()
    contact = StringField()
    status = BooleanField()  # True: have used service 

new_customer= Customers(
    name = "Kiều Anh",
    gender = True,
    email = 'ngocanh.ng95@gmail.com',
    phonenumber = '01684622437',
    job = "student",
    company = "law school",
    contact = "Hoang Mai, Ha Noi",
    status = False)

new_customer.save()


