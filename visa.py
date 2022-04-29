balance = 1000
chances = 0

while chances < 5:
    pin = 12345
    pin_input = int(input("Please Enter Your Pin: "))
    if pin == pin_input:
        print("Login Successfully")
        purchase = int(input("Please enter amount to pay: "))
        if purchase > balance:
            print("Balance too low.")
        else:
            balance = balance - purchase
            print("Item Amount: " + str(purchase))
            print("Purchase Successfully")
            print("Remaining Balnce:" + str(balance))
    elif pin != pin_input:
        print("Wrong Pin, Try again")
        chances += 1
        
    else:
        pass