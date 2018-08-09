from mongoengine import *
import mlab

mlab.connect()

class Admin(Document):
    username = StringField()
    password = StringField()

# new_admin = Admin(
#     username = 'tieuanhanh',
#     password = 'tieuanhanh'
# )

# new_admin.save()