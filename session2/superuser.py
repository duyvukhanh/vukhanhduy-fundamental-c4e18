# from getpass import getpass # hide pass
username = "duyvukhanh"
password = "123456"
count = 0
while True:
    user = input("Username: ")

    if user == username:
        passs = input("Password: ")
        if passs != password:
            print("Wrong pass")
            count += 1
            if count == 3:
                print("Go away")
                break
                
               
        else:
            print("You are welcome")
            break
    else:
        print("You are not superuser")
        



