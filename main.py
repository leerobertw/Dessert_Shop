def main():
    cmd = '0'
    while cmd != '2':
        print("Welcome to the dessert Shop")
        print("Enter 1 to create an order")
        print("Enter 2 to exit")
        print()
        cmd = input("Enter your choice> ")
        if cmd == '1':
            place_order()
        elif cmd != '2':
            print("Invalid entry, try again")


def place_order():
    pass

