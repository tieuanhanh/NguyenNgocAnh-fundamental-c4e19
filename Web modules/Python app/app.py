from flask import *
import mlab
from service import Service
from customers import Customers

app = Flask(__name__)

mlab.connect()
# design database


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin():
    all_service = Service.objects()
    return render_template('admin.html', all_service = all_service)

@app.route('/delete/<service_id>')
def delete(service_id):
    service = Service.objects.with_id(service_id)
    if service is not None:
        service.delete()
        return redirect(url_for('admin'))
    else:
        return "Service not found"

# /search
@app.route('/search/<g>')
def search(g):
    all_service = Service.objects(gender=g) # yob__lte=1998, address__contains="Hà Nội"
    return render_template('search.html', all_service = all_service)

@app.route('/detail/<service_id>')
def detail(service_id):
    service = Service.objects.with_id(service_id)
    return render_template ('detail.html', service = service)

@app.route('/new-service', methods =["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template('new-service.html')
    elif request.method == "POST":
        form = request.form
        name = form['name']
        gender = form['gender']
        yob = form['yob']
        phone = form['phone']
        height = form['height']
        address = form['address']
        status = form['status']
        if status == '0':
            status_save = False
        else:
            status_save = True
        new_service = Service(
            name = name,
            yob = yob,
            phone = phone,
            gender = gender,
            height = height,
            address = address,
            status = status_save
        )
        new_service.save()
        return redirect(url_for('admin'))

@app.route('/update-service/<service_id>', methods = ['GET', 'POST'])
def update_service(service_id):    
    service = Service.objects.with_id(service_id)
    if request.method == 'GET':
        return render_template('update_service.html', service = service)
    elif request.method == 'POST':
        form = request.form
        name = form['name']
        yob = form['yob']
        gender = form['gender']
        phone = form['phone']
        height = form['height']
        address = form['address']
        status = form['status']
        if status == '0':
            status_save = False
        else:
            status_save = True
        service.update(set__name = name,
                        set__yob = yob,
                        set__gender = gender,
                        set__phone = phone,
                        set__height = height,
                        set__address = address,
                        set__status = status_save)
        service.reload()
        return redirect(url_for('admin'))

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
 