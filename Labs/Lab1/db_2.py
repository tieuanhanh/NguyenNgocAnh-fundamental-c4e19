from pymongo import MongoClient

uri = "mongodb://admin:admin123@ds135441.mlab.com:35441/c4e19_lab"

client = MongoClient(uri)

db = client.get_default_database()

manga = db['manga']

manga_1 = {
    "name": "Conan",
    "description": "Best detective ever"
}

# manga_2 = {
#     "name": "CCS",
#     "description"L "Best romance"
# }

manga.insert_one(manga_1)