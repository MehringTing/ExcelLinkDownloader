from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
    return 'hello world'


@app.route('/users')
def get_users():
    return 'abc.'


@app.route('/users/<int:user_id>')
def show_user(user_id):
    return 'user %d' % user_id
