from flask import *
import mlab
from service import Service
from customers import Customers
from user import User,  Order
from admin import Admin
import datetime
from gmail import GMail, Message

app = Flask(__name__)

app.secret_key = 'a super secret key'

mlab.connect()
# design database


@app.route('/')
def index():
    all_service = Service.objects()
    return render_template('index.html', all_service = all_service)

@app.route('/admin-login', methods = ['POST', 'GET'])
def admin_login():
    if request.method == "GET":
        return render_template('admin_login.html')
    if request.method == "POST":
        form = request.form
        username = form['username']
        password = form['password']
        find_admin = Admin.objects(username = username, password = password)
        if len(find_admin) != 0:
            session['admin_login'] = True
            return redirect (url_for('admin'))
        else:
            return "Bạn không có quyền truy cập"

@app.route('/admin-logout')
def admin_logout():
    if 'admin_login' in session:
        del session['admin_login']
        return redirect (url_for('index'))
    else:
        return "Bạn chưa đăng nhập."

@app.route('/admin')
def admin():
    if "admin_login" in session:
        all_service = Service.objects()
        return render_template('admin.html', all_service = all_service)
    else:
        return "Bạn không có quyền truy cập."

@app.route('/sign-in', methods = ['GET', 'POST'])
def sign_in():
    if request.method == 'GET':
        return render_template('sign_in.html')
    elif request.method == 'POST':
        form = request.form
        username = form['username']
        password = form['password']
        email = form['email']
        fullname = form['fullname']
        new_user = User(
            username = username,
            password = password,
            fullname = fullname,
            email = email
        )
        new_user.save()
        return redirect (url_for('index'))

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        form = request.form
        username = form['username']
        password = form['password']
        find = User.objects(username = username, password = password)
        if len(find) != 0:
            session['logged_in'] = True
            session['user_id'] = str(find[0].id)
            return redirect (url_for('index'))
        else:
            return "Bạn nhập sai tên tài khoản hoặc mật khẩu."

@app.route('/logout')
def logout():
    if 'logged_in' in session:
        del session['logged_in']
        return redirect (url_for('index'))
    else:
        return "Bạn chưa đăng nhập."

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
    if "logged_in" in session:
        service = Service.objects.with_id(service_id)
        return render_template ('detail.html', service = service)
    else:
        return redirect(url_for('login'))


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

@app.route('/order/<service_id>')
def order(service_id):
    if "logged_in" in session:
        new_order = Order(
            service_id = service_id,
            user_id = session['user_id'],
            time = datetime.datetime.now,
            is_accepted = False     # False: not accepted yet
        )
        new_order.save()
        return "Đã gửi yêu cầu"
    else:
        return "Bạn chưa đăng nhập"  

@app.route('/order-page')
def order_page():
    all_order = Order.objects(is_accepted = False)
    return render_template('order.html', all_order = all_order)


@app.route('/is-accepted/<order_id>')
def is_accepted(order_id):
    if 'admin_login' in session:
        order = Order.objects.with_id(order_id)
        order.update (set__is_accepted = True )
        order.reload()
        gmail = GMail ('Mua Dong Khong Lanh Admin <nabi.253@gmail.com>', 'Ngocanh123')
        html_content = "Yêu cầu của bạn đã được xử lí. Chúng tôi sẽ liên hệ với bạn trong thời gian sớm nhất. Cảm ơn đã sử dụng dịch vụ."
        msg = Message ('Thư xác nhận yêu cầu', to = order.user_id.email, html = html_content)
        gmail.send(msg)
        return redirect (url_for('order_page'))
    else:
        return redirect (url_for ('admin_login'))

if __name__ == '__main__':
  app.run(debug=True)
 