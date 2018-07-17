from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)

db = client.get_default_database()

posts = db['posts']

new_post = {
    "title": "Tuyển tập những câu nói yêu thích của NA",
    "author": "NA chế",
    "content": """ 
    1. Người lướt qua nhau đã khó, được gặp nhau lại càng khó hơn, vì vậy hãy trân trọng những giây phút ở bên nhau. 
    2. Không có việc gì là không thể, chỉ có bản thân đã chọn sẽ không làm.
    3. Nếu không có nơi mình muốn đến, thì đi đường nào có khác gì nhau?
    """
}

posts.insert_one(new_post) 
