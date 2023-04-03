from Order import Order
from MenuItems import Candy, Cookies, IceCream, Sundae, SundaeToppings


def main():
    cmd = '0'
    while cmd != '2':
        print("Welcome to the dessert Shop")
        print("Enter 1 to create an order")
        print("Enter 2 to exit")
        print()
        cmd = input("Enter your choice> ").strip()
        if cmd == '1':
            place_order()
        elif cmd != '2':
            print("Invalid entry, try again")


def place_order():
    order = Order()
    cmd = '0'
    while cmd != '5':
        print("Enter 1 to add candy")
        print("Enter 2 to add cookies")
        print("Enter 3 to add ice cream")
        print("Enter 4 to add a sundae")
        print("Enter 5 to print receipt\n")
        cmd = input("Enter choice: ").strip()
        if cmd == '1':
            add_candy(order)
        elif cmd == '2':
            add_cookies(order)
        elif cmd == '3':
            add_icecream(order)
        elif cmd == '4':
            add_sundae(order)
        elif cmd == '5':
            print_receipt(order)
        else:
            print("Invalid entry")

def add_candy(order):
    weight = input("Enter amount of candy in lbs: ")
    if weight.replace('.', '').isdecimal():
        weight = float(weight)
        candy = Candy(weight)
        order.add_item(candy)
    else:
        print("Invalid entry")

def add_cookies(order):
    amount = input("How many dozens of cookies: ")
    if amount.isdecimal():
        order.add_item(Cookies(int(amount)))
    else:
        print("Invalid entry")

def add_icecream(order):
    scoops = input("How many scoops: ")
    if scoops.isdecimal():
        order.add_item(IceCream(int(scoops)))
    else:
        print("Invalid entry")

def add_sundae(order):
    sundae = Sundae()
    add_sundae_toppings(sundae)
    order.add_item(sundae)

def add_sundae_toppings(sundae):
    cmd = 0
    while cmd != '6':
        print("Add toppings:")
        print("1 - Hot Fudge")
        print("2 - Carmel Syrup")
        print("3 - Strawberry Syrup")
        print("4 - Peanuts")
        print("5 - Coconut")
        print("6 - Complete Order")
        cmd = input("Enter choice: ").strip()
        if cmd == '1':
            sundae.add_topping(SundaeToppings.Hot_Fudge)
        elif cmd == '2':
            sundae.add_topping(SundaeToppings.Carmel_Syrup)
        elif cmd == '3':
            sundae.add_topping(SundaeToppings.Strawberry_Syrup)
        elif cmd == '4':
            sundae.add_topping(SundaeToppings.Peanuts)
        elif cmd == '5':
            sundae.add_topping(SundaeToppings.Coconut)
        elif cmd == '6':
            break
        else:
            print("Invalid entry")

def print_receipt(order):
    items = order.get_items()
    print("Dessert Shop Purchase Receipt")
    print("-----------------------------")
    for item in items:
        print(item)


if __name__ == '__main__':
    main()
