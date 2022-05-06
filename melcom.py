from hashlib import new
import time # import time t use at the visiting side so as to record the time a user visits.
import random # uses this random number generator to generate random numbers for order numbers.


# Prints the name of the store, time and date of the customer visit.
print("WELCOME TO MELCOME") 
print("Where Ghana Shops...")
print()
print(time.strftime("%A %I:%M:%S %p \n%B %d, %Y"),)

print("_" * 40)

print()

# Converted the discount for male and female to decimals fo right calculation.
products = [{ 'ID' : 1001,'Name': 'Bulb', 'Type': 'Electronics', 'Price': 5.30, 'Quantity': 50, 'Male': 12, 'Female': 15},
            {'ID': 1002, 'Name': 'Heater Cup', 'Type': 'Electronics', 'Price': 109.99, 'Quantity': 34, 'Male': 12, 'Female': 15},
            {'ID': 1003, 'Name': 'Laptop', 'Type': 'Electronics', 'Price': 1249.99, 'Quantity': 14, 'Male': 12, 'Female': 15},
            {'ID': 1004, 'Name': 'Televison', 'Type': 'Electronics', 'Price': 3009.99, 'Quantity': 34, 'Male': 12, 'Female': 15},
            
            {'ID': 1005, 'Name': 'Couch', 'Type': 'Furniture', 'Price': 1000.00, 'Quantity': 50, 'Male': 17, 'Female': 37},
            {'ID': 1006, 'Name': 'TV Stand', 'Type': 'Furniture', 'Price': 549.99, 'Quantity': 26, 'Male': 17, 'Female': 37},
            {'ID': 1007, 'Name': 'Table', 'Type': 'Furniture', 'Price': 765.60, 'Quantity': 14, 'Male': 17, 'Female': 37},
            {'ID': 1008, 'Name': 'Cabinets', 'Type': 'Furniture', 'Price': 1020.33, 'Quantity': 12, 'Male': 17, 'Female': 37},
            
            {'ID': 1009, 'Name': 'Men Suit', 'Type': 'Clothes', 'Price': 250.00, 'Quantity': 35, 'Male': 6, 'Female': 3},
            {'ID': 1010, 'Name': 'Skirt', 'Type': 'Clothes', 'Price': 30.50, 'Quantity': 50, 'Male': 6, 'Female': 3},
            {'ID': 1011, 'Name': 'Slipper', 'Type': 'Clothes', 'Price': 4.80, 'Quantity': 40, 'Male': 6, 'Female': 3},
            {'ID': 1012, 'Name': 'Sneaker', 'Type': 'Furniture', 'Price': 179.99, 'Quantity': 21, 'Male': 6, 'Female': 3},
            
            {'ID': 1004, 'Name': 'Pot', 'Type': 'Kitchenware', 'Price': 35.50, 'Quantity': 50, 'Male': 7, 'Female': 30},
            {'ID': 1004, 'Name': 'Rack', 'Type': 'Kitchenware', 'Price': 5.10, 'Quantity': 50, 'Male': 7, 'Female': 30},
            {'ID': 1004, 'Name': 'Pan', 'Type': 'Kitchenware', 'Price': 25.90, 'Quantity': 31, 'Male': 7, 'Female': 30},
            {'ID': 1004, 'Name': 'Tray', 'Type': 'Kitchenware', 'Price': 35.50, 'Quantity': 15, 'Male': 7, 'Female': 30},
            
]

 

total = 0
shopping = products
temp = []
order = ""


# This functions lists the available options.
def userSelect():
    print()
    print("1.Display Menu")
    print("2.Place order")
    print("3.Cancel order")
    print("4.Logout")
    print("-"* 10)

# This function gives the user to select from multiple options.
def userChoiceSelect():
    choice = int(input("Please enter user choice: "))
    if choice == 1:
        displayProducts()
        print("-"*50)
        
        userSelect()
        print("-"*50)
        userChoiceSelect()
    elif choice == 2:
        placeOrder()
        print("-"*50)
        
        userSelect()
        print("-"*50)
        
        userChoiceSelect()
        print("-"*50)
        
    elif choice == 3:
        cancelOrder()
        print("-"*50)
        
        userSelect()
        print("-"*50)
        
        userChoiceSelect()
        print("-"*50)
        
    elif choice == 4:
        logout()
    else:
        print("Invalid Choice. Please enter valid choice")

def displayProducts():
    print("ID \tProduct       \tType             \tPrice     \tQuantity")
    print("-" * 75)
    
    for product in shopping:
        print(f'{product["ID"]} \t{product["Name"]}     \t{product["Type"]}         \t{product["Price"]:.2f}        \t{product["Quantity"]}')

    print("-" * 75)
 
# def genderSelect():
    # gender = input("Please select your gender M/F: ")
    # if gender == "M" or gender == "m":
    #                    print(f"You've got a discount of {product['Male']}%")
    #                    print()
    #                    price = 100 - product["Male"]
    #                    new_price = price  / 100 * product["Price"]
    #                    print()
    #                    print(f"Amount: GHS{product['Price']:.2f}")
    #                    print(f"Total with Discount: GHS{new_price:.2f}")
    #                    if new_price >= 1200:
    #                        total = new_price * (100 - 5)/100
    #                        print(f"Total: GHS{total:.2f}")
    #                    else:
    #                        print("-" * 15)
    #                        print(f"Total: GHS{new_price:.2f}")
    # elif gender == 'F' or 'f':
    #     print(f"You've got  a discount of {product['Female']}%")
    #     print()
    #     price = 100 - product["Female"]
    #     new_price = price  / 100 * product["Price"]
    #     print()
    #     print(f"Amount: GHS{product['Price']:.2f}")
    #     print(f"Total with Discount: GHS{new_price:.2f}")
    #     if new_price >= 1200:
    #         total = new_price * (100 - 5)/100
    #         print(f"Total: GHS{total:.2f}")
    #     else:
    #             print("-" * 15)
    #             print(f"Total: GHS{new_price:.2f}")   
# this function gives the user the chance to place an order in the store.
def placeOrder():
    order_number = random.randint(10000000, 1000000000000)
    displayProducts()
    product_id = int(input("\nEnter the ID: "))
    # product_ids = str(product_id).split('\n')
    # gender = input("Please select your gender M/F: ")

    for product in shopping:
        if product["ID"] == product_id:
            print("Amzaing! We have a discount for you...")
            print("\nID\tProduct    \tType      \tPrice")
            print("=============================================================")
            print(f'{product["ID"]}\t{product["Name"]}\t{product["Type"]}\t{product["Price"]:.2f}')
            order = f'{product["ID"]}       \t{product["Name"]}     \t{product["Type"]}     \t{product["Price"]:.2f}'
            confirm = input("\nDo you want to place an order on the above shown product Y/N: ")
            print()
            gender = input("Please select your gender M/F: ")
                # if gender == "M" or gender == "m":
                #                    print(f"You've got a discount of {product['Male']}%")
                #                    print()
                #                    price = 100 - product["Male"]
                #                    new_price = price  / 100 * product["Price"]
                #                    print()
                #                    print(f"Amount: GHS{product['Price']:.2f}")
                #                    print(f"Total with Discount: GHS{new_price:.2f}")
                #                    if new_price >= 1200:
                #                        total = new_price * (100 - 5)/100
                #                        print(f"Total: GHS{total:.2f}")
                #                    else:
                #                        print("-" * 15)
                #                        print(f"Total: GHS{new_price:.2f}")
                # elif gender == 'F' or 'f':
                #     print(f"You've got  a discount of {product['Female']}%")
                #     print()
                #     price = 100 - product["Female"]
                #     new_price = price  / 100 * product["Price"]
                #     print()
                #     print(f"Amount: GHS{product['Price']:.2f}")
                #     print(f"Total with Discount: GHS{new_price:.2f}")
                #     if new_price >= 1200:
                #         total = new_price * (100 - 5)/100
                #         print(f"Total: GHS{total:.2f}")
                #     else:
                #             print("-" * 15)
                #             print(f"Total: GHS{new_price:.2f}")
            if confirm == 'Y' or confirm == 'y':
                print("\nSuccessfully placed the order on the product {} {}".format(product["ID"], product["Name"]))
                order_number *= 1000
                print("Your order number is : ", order_number)
                product["Quantity"] -= 1
                
                if gender == "M" or gender == "m":
                               print(f"You've got a discount of {product['Male']}%")
                               print()
                               price = 100 - product["Male"]
                               new_price = price  / 100 * product["Price"]
                               print()
                               print("Product Summary")
                               print('-'* 15)
                               print(f"Amount: GHS{product['Price']:.2f}")
                               print(f"Discounted Amount: GHS{new_price:.2f}")
                               if product['Price'] >= 1200:
                                   print("Addtional discount for purchase of GHS1200 or more 5%\n")
                                   total = new_price * (100 - 5)/100
                                   print(f"Addtional discounted Amount: GHS{total:.2f}")
                                   print('-'* 20)
                                   print()
                                   print(f"Total: GHS{total:.2f}")
                                   print("\nThank you for shopping with us today, See you again!\n")
                               else:
                                   print("-" * 15)
                                   print()
                                   print(f"Total: GHS{new_price:.2f}")
                                   print("\nThank you for shopping with us today, See you again!\n")
                elif gender == 'F' or 'f':
                    print(f"You've got  a discount of {product['Female']}%")
                    print()
                    price = 100 - product["Female"]
                    new_price = price  / 100 * product["Price"]
                    print()
                    print('-'* 15)
                    print(f"Amount: GHS{product['Price']:.2f}")
                    print(f"Discounted Amount: GHS{new_price:.2f}")
                    if product['Price'] >= 1200:
                        print("Addtional discount for purchase of GHS1200 or more 5%\n")
                        total = new_price * (100 - 5)/100
                        print(f"Addtional discounted Amount: GHS{total:.2f}\n")
                        print('-'* 20)
                        print(f"Total: GHS{total:.2f}")
                    else:
                            print("-" * 15)
                            print(f"Total: GHS{new_price:.2f}")
                break
            elif confirm == 'N' or confirm == 'n':
                print("The order is not placed. You can explore more on our store... Great shopping with us!!!!")
                break
            else:
                print("\nYou have entered wrong option. Please enter again\n")
                confirm = input("\nDo you want to place an order on the above shown product : Y/N ")
                break

    if product["ID"] != product_id:
        print("\nYou have entered invalid id. Please enter valid id\n")
        user_id()
    # print("\nAvailable products : \n")
    # displayProducts()
      
      
def user_id():
    displayProducts()
    p_id = int(input("\nEnter the id : "))
    
# This function gives a user the chance to cancel and order.    
def cancelOrder():
    found = False
    temp = []
    order_id = input("Enter order ID: ")
    for product in shopping:
        found = product["ID"] == order_id
        if found != True:
            temp.append(product)
    if len(temp) == product:
        print(f'{order_id} is not found')
    else:
        print(f'{order_id} is removed from the placed order')


def login():
    username = input("Enter Username: ")
    chances = 0
    while chances < 3:
        userLogin = input("Enter Password to login: ")
        if userLogin == "Melcom":
            print(f"Hey {username}, it is great to shop with us today...")
            userSelect()
            userChoiceSelect()
        else:
        
            print("\nInvalid password. Please enter valid password\n")
            chances += 1
            
    print("Sorry, You've enter wrong password three times, please try again in an hour or reset your password.")


def tryAgain():
    response = input("Would you like to try logging in again? (Y/N): ")
    response = response.upper()
    if response == "Y":
        return True
    else:
        return False


# Gives user the chance to logout.
def logout():
    login()

login()

while tryAgain():
    login()
