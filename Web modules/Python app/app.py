from flask import Flask, render_template
import mlab
from models.service import Service
from customers import Customers

app = Flask(__name__)

mlab.connect()
# design database


@app.route('/')
def index():
    return render_template('index.html')

# /search
@app.route('/search/<g>')
def search(g):
    all_service = Service.objects(gender=g, yob__lte=1998, address__contains="Hà ")
    return render_template('search.html', all_service = all_service)

@app.route('/customer')
def customer():
    all_customers = Customers.objects()
    return render_template('customers.html', all_customers = all_customers)

@app.route('/10-first-male')
def firstmales():
    all_customers = Customers.objects(gender=1, status = False)
    new_customers = all_customers[0:10]
    return render_template('firstmales.html', new_customers = new_customers)

if __name__ == '__main__':
  app.run(debug=True)
 