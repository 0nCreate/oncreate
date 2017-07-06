from oncreate.config import app
from oncreate.user_api import UserDbApi


view = UserDbApi.as_view('api')
app.add_url_rule('/', view_func=view, methods=['GET', 'POST'])


if __name__ == "__main__":
    app.run(debug=True)
