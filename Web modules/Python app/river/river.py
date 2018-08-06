import mlab
from mongoengine import *

mlab.connect()

class River(Document):
    name = StringField()
    continent = StringField()
    length = IntField()

for river in River.objects(continent ='Africa'):
    print (river.name)

for river in River.objects(continent ='S. America', length__lt=1000):
    print (river.name)