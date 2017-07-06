from oncreate.config import db
from oncreate.flask_app import User


# dmytro.kaminskyi92@gmail.com
# add this to GIT collaborators


def create_test_users():
    for i in range(40):
        email = "example_{}@gmail.com".format(i)
        username = "TEST_USERNAME_{}".format(i)
        user = User(
            email=email,
            username=username)
        db.session.add(user)
        db.session.commit()

if __name__ == "__main__":
    while True:
        print("CREATE: 1, DROP: 2, FULLFILL: 3, MAKE ALL: 4, QUIT: q OR quit")
        user_input = input("SELECT OPTION: ")
        if user_input == "1":
            db.create_all()
        elif user_input == "2":
            db.drop_all()
        elif user_input == "3":
            create_test_users()
        elif user_input == "4":
            db.drop_all()
            db.create_all()
            create_test_users()
        elif user_input in ["q", "quit"]:
            break
