print('1.Sign up \n 2.Sign in')
choice = int(input("Enter your choice: "))
if choice == 1:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    mob = input("Enter mobile number: ")
    with open('signupinfo.json', 'a') as f:
        f.write( username + ' ' + password + ' ' + mob + '\n')
else:
    flag= 0
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    with open('signupinfo.json', 'r') as f:
        for x in f.readlines():
            values = x.split(' ')
            if(username == values[0] and password == values[1]):
                print("welcome to the device!!")
                print("your info")
                print("username: " + values[0])
                print("password: " + values[1])
                print("mobile: " + values[2])
                flag = 0
                break
            else:
                flag = 1
    if(flag == 1):
        print("Incorrect Credentials ")