from enum import Enum, StrEnum, auto


entertainment_tax_rate = 0.07
food_tax_rate = 0.0625

class MenuItem:
    def __init__(self, amount, price, tax_rate):
        self._amount = amount
        self._price = price
        self._tax_rate = tax_rate

    def calculate_total(self):
        return round(self._price * self._amount, 2)

    def get_total_and_tax(self):
        total_cost = self.calculate_total()
        return total_cost, round(total_cost * self._tax_rate, 2)


class Candy(MenuItem):
    price = 4.75

    def __init__(self, weight):
        super().__init__(weight, Candy.price, food_tax_rate)

    def __str__(self):
        return f"{self._amount} lbs of candy"


class Cookies(MenuItem):
    price = 6.25

    def __init__(self, count):
        super().__init__(count, Cookies.price, food_tax_rate)

    def __str__(self):
        return f"{self._amount} dozen cookies"

class IceCreamFlavors(StrEnum):
    Vanilla = auto()
    Chocolate = auto()
    Strawberry = auto()
    Huckleberry = auto()

class IceCreamConeType(StrEnum):
    Bowl = auto()
    Cone = auto()
    Waffle_Cone = "waffle cone"

class IceCream(MenuItem):
    price = 1.70

    def __init__(self, scoops, flavor, cone_type):
        super().__init__(scoops, IceCream.price, entertainment_tax_rate)
        self.flavor = flavor
        self.cone_type = cone_type

    def __str__(self):
        return f"{self._amount} scoops of {self.flavor.value} ice cream in a {self.cone_type.value}"


class SundaeToppings(Enum):
    Hot_Fudge = 1.25
    Strawberry_Syrup = 0.75
    Carmel_Syrup = 0.50
    Peanuts = 0.35
    Coconut = 0.20

class Sundae(MenuItem):
    def __init__(self):
        super().__init__(2, IceCream.price, entertainment_tax_rate)
        self.toppings = []

    def calculate_total(self):
        return round(super().calculate_total() + sum(topping.value for topping in self.toppings), 2)

    def add_topping(self, topping):
        self.toppings.append(topping)

    def __str__(self):
        toppings_display = [topping.name for topping in self.toppings]
        return f"Sundae with {', '.join(toppings_display)}"
