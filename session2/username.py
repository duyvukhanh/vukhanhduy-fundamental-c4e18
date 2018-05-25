from getpass import getpass # hide pass
username = "duyvukhanh"
password = "123456"
user = input("Username: ")
passs = getpass("Password: ")

if user != username:
    print("No suck user!")
elif user == username and passs != password:
    print("Wrong pw!")
elif user == username and passs == password:
    print("Welcome")
