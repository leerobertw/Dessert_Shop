from enum import Enum

from money.money import Money

entertainment_tax_rate = 0.07
food_tax_rate = 0.0625


class Candy:
    price_per_pound = Money('4.75')

    def __init__(self, weight):
        self.weight = weight

    def calculate_total(self):
        return Candy.price_per_pound * self.weight

    def calculate_tax(self):
        return self.calculate_total() * food_tax_rate

    def __str__(self):
        return f"{self.weight} lbs of candy"

class Cookies:
    price_per_dozen = Money('6.25')

    def __init__(self, count):
        self.count = count

    def calculate_total(self):
        return Cookies.price_per_dozen * self.count

    def calculate_tax(self):
        return self.calculate_total() * food_tax_rate

    def __str__(self):
        return f"{self.count} dozen cookies"

class IceCream:
    price_per_scoop = Money('1.70')

    def __init__(self, scoops):
        self.scoops = scoops

    def calculate_total(self):
        return IceCream.price_per_scoop * self.scoops

    def calculate_tax(self):
        return self.calculate_total() * entertainment_tax_rate

    def __str__(self):
        return f"{self.scoops} scoops of ice cream"


class SundaeToppings(Enum):
    Hot_Fudge = Money('1.25')
    Strawberry_Syrup = Money('0.75')
    Carmel_Syrup = Money('0.50')
    Peanuts = Money('0.35')
    Coconut = Money('0.20')

class Sundae:
    def __init__(self):
        self.ice_cream_cost = IceCream(2).calculate_total()
        self.toppings = []

    def calculate_total(self):
        total = self.ice_cream_cost
        for topping in self.toppings:
            total += topping.value
        return total

    def calculate_tax(self):
        return self.calculate_total() * entertainment_tax_rate

    def add_topping(self, topping):
        self.toppings.append(topping)

    def __str__(self):
        toppings_display = [topping.name for topping in self.toppings]
        return f"Sundae with {', '.join(toppings_display)}"
