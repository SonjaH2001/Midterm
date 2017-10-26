# starting to determine routes
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')

@app.route('/index', methods=['Get'])#route to home page
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run() #kind of like the web server
#google flask template