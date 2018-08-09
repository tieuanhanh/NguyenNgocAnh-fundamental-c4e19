from mongoengine import *
import mlab

mlab.connect()

class Service(Document): 
    image = StringField()
    name = StringField()
    yob = IntField()
    gender = IntField()
    description = StringField()
    height = IntField()
    measurements = ListField()
    phone = StringField()
    address = StringField()
    status = BooleanField()

# new_service = Service(
#     image = "https://scontent.fhan5-2.fna.fbcdn.net/v/t1.0-9/14264853_1174245952633618_8869505366815706281_n.jpg?_nc_cat=0&oh=581567e57fb1248dd4920df227d65ee0&oe=5BC7AC98",
#     name = "Ngọc Anh",
#     yob = 1995,
#     gender = 0,  #0: female
#     description = "No thing ",
#     height = 165,
#     measurements = [83, 63, 88],
#     phone = "09000000000",
#     address = "Hải Dương",
#     status = True  #Fale: available
# )
# new_service.save()

# new_service = Service(
#     image = "https://scontent.fhan5-2.fna.fbcdn.net/v/t1.0-9/22894203_852563721569364_7637480182014460547_n.jpg?_nc_cat=0&oh=0690a1945ab8dfffe87d5e1c6315b8b0&oe=5C060432",
#     name = "Việt Linh",
#     yob = 1999,
#     gender = 1,  #0: female
#     description = "ngáo đá nhưng chiều bạn gái, biết chơi đàn, làm thơ, còn gì mà nó không biết không? @_@. Hoa đã có chủ nhá há há",
#     height = 165,
#     measurements = [90, 63, 85],
#     phone = "09000000001",
#     address = "Hà Nội",
#     status = True  #Fale: available
# )

# new_service.save()

# new_service = Service(
#     image = "https://scontent.fhan5-2.fna.fbcdn.net/v/t1.0-9/36664411_1945058055784796_7367104493126680576_n.jpg?_nc_cat=0&oh=fcc29f8e1e787dd7e8656ce70c4a91f2&oe=5BC5C825",
#     name = "Liên",
#     yob = 1999,
#     gender = 0,  #0: female
#     description = "đáng iu, lễ phép, ngây thơ vô số tội",
#     height = 158,
#     measurements = [85, 63, 85],
#     phone = "09000000002",
#     address = "Nam Định",
#     status = False  #Fale: available
# )

# new_service.save()

# new_service = Service(
#     image = "https://scontent.fhan5-2.fna.fbcdn.net/v/t1.0-9/37010173_1694446137336477_6512956010439639040_n.jpg?_nc_cat=0&oh=bc006d174d4d04aefb73a24cf3dff2a0&oe=5C03CEAF",
#     name = "Quân",
#     yob = 1996,
#     gender = 1,  #0: female
#     description = "ngáo ngơ cộng hòa, nhiệt tình với học viên",
#     height = 170,
#     measurements = [80, 70, 80],
#     phone = "09000000003",
#     address = "Long Biên, Hà Nội",
#     status = False  #Fale: available
# )

# new_service.save()
