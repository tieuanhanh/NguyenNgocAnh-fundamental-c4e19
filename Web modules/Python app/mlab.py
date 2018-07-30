import mongoengine

# mongodb://c4e19:253a137a14@ds155461.mlab.com:55461/mua_dong_khong_lanh_c4e19

host = "ds155461.mlab.com"
port = 55461
db_name = "mua_dong_khong_lanh_c4e19"
user_name = "c4e19"
password = "253a137a14"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())