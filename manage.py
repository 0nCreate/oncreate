from flask_app import app, db, User

def create_test_users():
    for i in range(40):
        email = "example_{}@gmail.com".format(i)
        username = "TEST_USERNAME_{}".format(i)
        user = User(email=email,
                    username=username)
        db.session.add(user)
        db.session.commit()

if __name__ == "__main__":
    user_input = input("SELECT OPTION: ")
    if user_input == "1":
        db.create_all()
    elif user_input == "2":
        db.drop_all()
    elif user_input == "3":
        create_test_users()
