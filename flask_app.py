import sys
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://oncreate:0987654321qwerty@oncreate.mysql.pythonanywhere-services.com/oncreate$oncreate_db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/')
def hello_world():
    path = sys.path
    db.drop_all()
    db.create_all()

    return 'Hello from Flask!{}'.format(path)

if __name__ == "__main__":
    db.create_all()
