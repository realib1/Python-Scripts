import time


print("WELCOME TO MELCOME") 
print("Where Ghana Shops...")
print()
print(time.strftime("%A %I:%M:%S %p \n%B %d, %Y"),)

print("_" * 40)

print()

products = [{ 'Bulb': 1001, 'Price': 5.30, 'Quantity': 50, 'Male': 0.12, 'Female': 0.15},
            {'Iron': 1002, 'Price': 109.99, 'Quantity': 34, 'Male': 0.12, 'Female': 0.15},
            {'Fan': 1003, 'Price': 1249.99, 'Quantity': 14, 'Male': 0.12, 'Female': 0.15},
            {'Television': 1004, 'Price': 3009.99, 'Quantity': 34, 'Male': 0.12, 'Female': 0.15}
]

 

def login():
    pin = "Melcom"
    user = input("Enter your username: ")
    password = input("Enter your password: ")
    if password == pin:
        print("Login successful.")
        print(f"Wlecome {user}, Happy to see you today...")
    elif password != pin:
        print("Wrong input. Login failed, Please try again.")
        
        
        
# def options():
#     print("1.Login\n2. Explore store")
#     option = ("Please choose from the options: ")
#     if option == 1:
#         login()
#     elif option == 2:
#         pass

def logout():
        pass

login()