from flask import Flask, jsonify, request

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://oncreate:0987654321qwerty@oncreate.mysql.pythonanywhere-services.com/oncreate$oncreate_db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
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

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
        }


@app.route('/', methods=["GET", "POST"])
def hello_world():
    if request.method == "GET":
        users = [user.to_dict() for user in User.query.all()]
        context = {
            "users": users
        }
        return jsonify(context)
    elif request.method == "POST":
        data = request.get_json()
        user = User(
            email=data.get("email"),
            username=data.get("username"),
        )
        db.session.add(user)
        db.session.commit()
        return jsonify({
            "method": "POST",
            "user": user.to_dict(),
            "success": True,
        })

if __name__ == "__main__":
    app.run(debug=True)
