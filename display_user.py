from main import User

my_user = User.select()
for User in my_user:
    print(User.name, User.email, User.password)
