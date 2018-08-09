from flask import *
from models.video import Video
import mlab
from youtube_dl import YoutubeDL

app = Flask(__name__)

# session requires a secret key
app.secret_key = 'a super secrect key'

mlab.connect()

@app.route('/')
def index():
    videos = Video.objects()
    return render_template('index.html', videos = videos)

@app.route('/logout')
def logout():
    # cach 1: xoa logged in khoi session
    # cach 2: tat cookies
    del session['logged in']
    return redirect (url_for('index'))

@app.route('/login', methods =['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template ('login.html')
    elif request.method == 'POST':
        form = request.form 
        username = form['username']
        password = form['password']

        if username == 'admin' and password == 'admin':
            session['logged in'] = True
            return redirect(url_for('admin'))
        else:
            return "Sai ten dang nhap hoac mat khau"

@app.route('/detail/<youtube_id>')
def detail(youtube_id):
    return render_template('detail.html', youtube_id = youtube_id)

@app.route('/admin', methods = ['GET', 'POST'])
def admin():
    if 'logged in' in session:
        if request.method == 'GET':
            videos = Video.objects()
            return render_template ('admin.html', videos = videos)
        elif request.method == 'POST':
            form = request.form
            link = form['link']

            ydl = YoutubeDL()
            data = ydl.extract_info(link, download=False)
            title = data['title']
            views = data['view_count']
            thumbnail = data['thumbnail']
            youtube_id = data['id']

            new_video = Video(
                title = title,
                link = link,
                thumbnail = thumbnail,
                views = views,
                youtube_id = youtube_id
            )
            new_video.save()

            return redirect(url_for('admin'))
    else:
        return "Di cho khac"

if __name__ == '__main__':
  app.run(debug=True)
 