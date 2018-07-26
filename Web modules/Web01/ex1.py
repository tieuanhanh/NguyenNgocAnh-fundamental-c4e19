from flask import Flask, redirect, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template ("bio.html")

@app.route('/school')
def school():
    return redirect ("http://techkids.vn")

@app.route('/bmi/<int:weight>/<int:height>')
def bmi (weight, height):
    bmi_numb = weight/((height/100) ** 2)
    if bmi_numb < 16:
        condition = "Severerly underweight"
    elif 16 <= bmi_numb < 18.5:
        condition = "Underweight"
    elif 18.5 <= bmi_numb < 25:
        condition = "Normal"
    elif 25 <= bmi_numb <30:
        condition = "Overweight"
    else:
        condition = "Obese"
    return "Your BMI is {0}. Your condition is {1}.".format(bmi_numb, condition)

@app.route('/user/<username>')
def user(username):
    users = {
        "quan": {"name": "Nguyen Anh Quan", 
        "age": 16},
        "tuananh": {"name": "Huynh Tuan Anh", 
        "age": 23}
        }
    if username in users:
        us = users[username]
        return render_template ("username.html", us = us)
    else:
        return "Not found"

if __name__ == '__main__':
  app.run(debug=True)
 