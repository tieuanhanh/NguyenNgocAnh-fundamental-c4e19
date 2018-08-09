import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds115472.mlab.com:15472/css

host = "ds115472.mlab.com"
port = 15472
db_name = "css"
user_name = "tieuanhanh"
password = "tieuanhanh123"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())