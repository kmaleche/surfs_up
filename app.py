# import dependency
from flask import Flask

# create app
app = Flask(__name__)

# create routes
@app.route('/')
def hello_world():
    return 'Hello world'

