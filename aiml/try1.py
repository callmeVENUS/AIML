username = "vedant"
password = "vedant123"

while True:
    a = input("Username: ")
    b = input("Password: ")

    if a == username and b == password:
        print("Login Success")
        break
    else:
        print("Try Again")