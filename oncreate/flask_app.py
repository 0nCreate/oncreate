from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify, request
from flask.views import MethodView


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://oncreate:0987654321qwerty@oncreate.mysql.pythonanywhere-services.com/oncreate$oncreate_db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

from oncreate.user import User


class UserDbApi(MethodView):

    def get(self):
        users = [user.to_dict() for user in User.query.all()]
        context = {
            "users": users
        }
        return jsonify(context)

    def post(self):
        data = request.get_json()
        user = User(
            email=data.get("email"),
            username=data.get("username"),
        )
        user.email = "NEW EMAIL"
        print(user.username)
        db.session.add(user)
        db.session.commit()
        return jsonify({
            "method": "POST",
            "user": user.to_dict(),
            "success": True,
        })


view = UserDbApi.as_view('api')
app.add_url_rule('/', view_func=view, methods=['GET', 'POST'])


if __name__ == "__main__":
    app.run(debug=True)
