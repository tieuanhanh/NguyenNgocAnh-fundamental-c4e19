from models.service import Service
import mlab


mlab.connect()

find_service = Service.objects.with_id("5b5b1c57cc3fc03544d564d2")
# find_service = Service.objects(id = '5b5b1c54cc3fc017148e44f9')
print (find_service['name'])

# find_service.delete()

