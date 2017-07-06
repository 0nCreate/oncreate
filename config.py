import socket
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

if socket.gethostname() == "MacBook-Air-Vladimir.local":
    PRODUCTION = False
else:
    PRODUCTION = True

app = Flask(__name__)
if PRODUCTION:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://oncreate:0987654321qwerty@oncreate.mysql.pythonanywhere-services.com/oncreate$oncreate_db'
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
