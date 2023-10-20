from flask import Flask, url_for, render_template
from markupsafe import escape

import os

# Få den aktuella katalogen där den här Python-filen (din Flask-applikation) är placerad
app_path = os.path.dirname(os.path.abspath(__file__))

print("Sökvägen till Flask-applikationen är:", app_path)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<p>Hello, World!</p>'


@app.route('/om-oss')
def om_oss():
    return render_template('om_oss.html')


@app.route('/<name>')
def hello_name(name):
    return f'Hello {escape(name)}!'


@app.route('/index')
def index():
    return 'Index Page'


@app.route('/hello')
def hello():
    return 'Hello, World'


@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {escape(username)}'


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'


@app.route('/lektion_1/<path:subpath>')
def show_subpath(subpath):
    try:
        # Öppna filen som subpath pekar på
        with open(subpath, 'r') as file:
            content = file.read()
        return f'Innehåll i filen {subpath}: {escape(content)}'
    except FileNotFoundError:
        return 'Filen kunde inte hittas.'


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'


@app.route('/login')
def login():
    return 'Login'


@app.route('/user/<username_ex>')
def profile(username_ex):
    return f'{username_ex}\'s profile'


with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username_ex='Lina Romilson'))
    print(url_for('projects'))
    print(url_for('about'))
    print(url_for('show_subpath', subpath='requirements.txt'))
