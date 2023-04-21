from Human import User, Admin, Developer

user = User
admin = Admin
developer = Developer


def main():
    print("User ", user.sey_hello())
    print("Admin ", admin.sey_hello(), admin.mend_something())
    print("Developer ", developer.sey_hello(), developer.mend_something(), developer.write_code())
        

if __name__ == "__main__":

   main()