from flask import Flask, render_template
app = Flask(__name__)

# duong dan:
@app.route('/')
def index():
    posts = [
        {
        "title": "Thơ con cóc",
        "content": """
                    Hôm nay trăng lên thấp quá
                    Anh dẫn em đi ăn cá""",
        "author": "NA",
        "gender": 1
        },
        {
        "title": "Thơ xàm",
        'content':"""Ngồi buồn ngồi cắn móng tay
                    Căn đi cắn lại vẫn không hết buồn""",
        "author": "NA",
        "gender": 0
        }
    ]
    return render_template("index.html", posts = posts)

@app.route('/hello')
def hello():
    return " Hello C4E 19"

@app.route('/say-hi/<name>/<age>')
def say_hi(name, age):
    return " Hi {}, your age is {}.".format(name, age)

# @app.route('/sum/<x>/<y>')
# def cal( x, y):
#     sum = int (x) + int (y)
#     return "{}".format(sum)
    # chi return lai string
    # cach 2: 
    # return str(sum)

# cach 2: 
@app.route('/sum/<int:x>/<int:y>')
def cal( x, y):
    sum = x + y
    return "{}".format(sum)

# khi file app dc chay truc tiep, run server, khac voi khi chay gian tiep: "import tu cho khac vao"
if __name__ == '__main__':
    app.run( debug=True) 
# debug = True: tu dong  cap nhat cac code moi 
 
#  1 link dan bao gom:
#  local host: 
# port 