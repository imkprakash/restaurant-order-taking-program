
# This is a program that will let you choose the food item that you want to order, the number of units of
# each food item. In the end this program will generate a receipt for you along with your name on it.
import sys
from datetime import date
from prettytable import PrettyTable

today = date.today()
today = today.strftime("%B %d, %Y")
# Stores Item Id : Item Name
menu = {1: "Pasta", 2: "Pizza", 3: "Fried Chicken (6 Pc.)", 4: "Burger", 5: "Baguette",
        6: "Sandwich", 7: "French Fries", 8: "Beer", 9: "Wine", 10: "Whiskey"}

# Stores Item Id : Item Cost
price = {1: 7.15, 2: 10.00, 3: 13.00, 4: 6.19,
         5: 3.00, 6: 4.50, 7: 2.00, 8: 4.75, 9: 6.00, 10: 4.00}

# This dictionary will store the Orders in the form of Item Id : Number of units ordered
orders = {}
# Variable to keep track if the person is ordering or not, this is the variable using which the main loop
# executes
ordering = True


# This table will store the menu.
menu_table = PrettyTable(["Item Id", "Food Item", "Cost / Unit ($)"])
for id, item in menu.items():
    menu_table.add_row([id, item, price[id]])

# Function to display the menu


def showMenu():
    print(menu_table)


# Function to order items that we want, it will keep asking for the order until we type clear,
# or we enter a valid id and amount

def orderItems():
    id, amount = 0, 0
    while id <= 0 and amount <= 0:
        print("Please enter the Item Id of the Food Item that you want to order:")
        print("If you would like to clear your order, type 'clear'")
        itemId = input()
        if itemId == 'clear':
            break
        if itemId.isnumeric():
            itemId = int(itemId)
            if itemId <= 0 or itemId > 10:
                print("Oops, this is not a valid Id for any Item. Please try again!")
                id, amount = 0, 0
                continue
            else:
                id = itemId
        else:
            print("Oops, this is not a valid Id for any Item. Please try again!")
            id, amount = 0, 0
            continue

        print("Please enter the number of units that you would like to order of this item:")
        print("If you would like to clear your order, type 'clear'")
        no_of_units = input()
        if no_of_units == 'clear':
            break
        if no_of_units.isnumeric():
            no_of_units = int(no_of_units)
            if no_of_units <= 0:
                print("Oops, this is not a valid number for ordering. Please try again")
                id, amount = 0, 0
                continue
            else:
                amount = no_of_units
        else:
            print("Oops, this is not a valid number for ordering. Please try again")
            id, amount = 0, 0
            continue

        if id not in orders:
            orders[id] = amount
        else:
            orders[id] += amount


# Table that will store the ordered items.
ordered_items_table = PrettyTable(
    ["Item Id", "Food Item", "Units Ordered", "Cost / Unit ($)", "Total cost for this item ($)"])
# Function for checkout


def checkout():
    Total = 0
    # Code for generating receipt
    original_stdout = sys.stdout
    with open('receipt.txt', 'w') as f:
        sys.stdout = f
        print("====================================================================================================")
        print("                                          RECEIPT")
        print("====================================================================================================")
        print("Name of the customer : {}".format(name))
        print("Date : {}".format(today))
        print("                                        ORDER SUMMARY")
        print("====================================================================================================")
        for id, item in menu.items():
            if id in orders:
                ordered_items_table.add_row(
                    [id, item, orders[id], price[id], round(price[id]*orders[id], 2)])
                Total += price[id]*orders[id]
        print(ordered_items_table)
        print("====================================================================================================")
        print("Total amount to be paid is : {} $".format(round(Total, 2)))
        print("====================================================================================================")
        print("Thank you for giving us a chance, we hope to see you soon!")
        sys.stdout = original_stdout
    print(ordered_items_table)
    print("Total amount to be paid is : {} $".format(round(Total, 2)))
    print("Thank you for giving us a chance, we hope to see you soon!")
    print("Thank you for visiting us! Your receipt containing your order summary has been generated.")


# Welcome message
print("==================================================")
print("             Hello and welcome!      ")
print("Please enter your name to proceed: ")
name = input()
print("==================================================")

# Asking the order
print("Hi there, {}".format(name))
print("What would you like to order today?")

# Main loop
while ordering:
    keep_ordering = -1
    showMenu()
    orderItems()
    while True:
        print("Enter '1' if you would like to order again or '0' if you would like to checkout:")
        x = input()
        if x.isnumeric():
            x = int(x)
            if x == 1:
                keep_ordering = 1
                break
            if x == 0:
                keep_ordering = 0
                break
            else:
                continue
        else:
            continue

    if keep_ordering == 0:
        ordering = False


# If the customer has ordered something, then only we generate a receipt
if len(orders):
    checkout()
else:
    print("Thanks for the visit!")
