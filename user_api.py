from flask import jsonify, request
from flask.views import MethodView
from oncreate.user import User
from oncreate.config import db


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