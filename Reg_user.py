from main import User

try:
    User_name = input("Enter Your Name \n")
    User_email = input("Enter Your email \n")
    User_Password = input("Enter Your Password \n")

    User.create(name=User_name, email=User_email, password=User_Password)
    print("User Created Successfully")

except:
    print("Failed to create a User,use another email")
