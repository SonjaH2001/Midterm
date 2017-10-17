# starting to determine routes
from flask import Flask

app = Flask(__name__)

@app.route('/')#route to home page
def hello_world():
    return 'hello world'

if __name__ == '__main__':
    app.run() #kind of like the web server
#google flask template