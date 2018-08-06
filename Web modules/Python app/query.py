from models.service import Service
import mlab

mlab.connect()

# all_service = Service.objects()

# first_service = all_service[0]

# print(first_service['name'])

id_to_find = "5b5b1e0bcc3fc00e5077673d"

# service = Service.objects(id=id_to_find) # => []

# service = Service.objects.get(id=id_to_find)  # => object
service = Service.objects.with_id(id_to_find) # => object

# print(service)
# # print(service[0].name) dung cho list
# print(service.to_mongo())


if service is not None: 
    # delete
    # service.delete()
    # print ("Delete")

    # update
    print("Before", service.to_mongo())
    service.update(set__name= "Lan", set__yob= 2000)
    service.reload()
    print("After", service.to_mongo())
else:
    print ("Not found")
