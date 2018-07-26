from flask import Flask
app = Flask(__name__)


@app.route('/user/<username>')
def user(username):
    users = {
        "quan": {"name": "Nguyen Anh Quan", 
        "age": 16},
        "tuananh": {"name": "Huynh Tuan Anh", 
        "age": 23}
        }
    if username in users:
        return "Your name is {} and your age is {}.".format(users[username]["name"], users[username]["age"])
        # for i in users[username].keys():
        #     return users[username][i]
    else:
        return "Not found"

if __name__ == '__main__':
  app.run( debug=True)
 