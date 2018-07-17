# bao gồm sql, noSQL (mongodb), PostGc, graphql

from pymongo import MongoClient

uri = "mongodb://admin:admin123@ds135441.mlab.com:35441/c4e19_lab"

#1. Connect to database
client = MongoClient(uri)

#2. Get database 
db = client.get_default_database()

#3. Create collection
games = db['games']

#4. Create Document
# new_game = {
#     "name": "Mario",
#     "description": "Best game ever"
# }

# #5. Insert doc into collection
# games.insert_one(new_game)

all_games = games.find()

print(all_games[1]['name'])