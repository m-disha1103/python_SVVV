#28 april 2026
#login attempt lock
flag=0
for i in range(3):
    password = input("enter your password: ")

    if password == "333":
        print("Login successful!")
        flag=1
        break
    else:
        print("Incorrect password. Try again.")

if not flag:
    print("account locked!!")

