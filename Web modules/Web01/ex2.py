from flask import Flask, render_template
app = Flask(__name__)


@app.route('/bmi/<int:weight>/<int:height>')
def bmi (weight, height):
    bmi_numb =  weight / ((height/100)**2)
    return render_template ("bmi.html", bmi_cal = bmi_numb)

if __name__ == '__main__':
  app.run(debug=True) 

