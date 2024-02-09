from enum import Enum, StrEnum, auto

class TaxRate(Enum):
    food = 0.03
    luxury = 0.0751

class MenuItem:
    def __init__(self, amount, price, tax_rate):
        self._amount = amount
        self._price = price
        self.tax_rate = tax_rate

    def get_total_and_tax(self):
        total = self._price * self._amount
        tax = self.tax_rate.value * total
        return round(total, 2), round(tax, 2)


class Candy(MenuItem):
    price = 4.75
    tax_rate = TaxRate.food

    def __init__(self, weight):
        super().__init__(weight, Candy.price, Candy.tax_rate)

    def __str__(self):
        return f"{self._amount} lbs of candy"


class Cookies(MenuItem):
    price = 6.25
    tax_rate = TaxRate.food

    def __init__(self, count):
        super().__init__(count, Cookies.price, Cookies.tax_rate)

    def __str__(self):
        return f"{self._amount} dozen cookies"

class IceCreamFlavors(StrEnum):
    vanilla = auto()
    chocolate = auto()
    strawberry = auto()
    huckleberry = auto()

class IceCreamConeType(StrEnum):
    bowl = auto()
    cone = auto()
    waffle_cone = auto()

class IceCream(MenuItem):
    price = 1.70
    tax_rate = TaxRate.luxury

    def __init__(self, scoops, flavor, cone_type):
        super().__init__(scoops, IceCream.price, IceCream.tax_rate)
        self.flavor = flavor
        self.cone_type = cone_type

    def __str__(self):
        return f"{self._amount} scoops of {self.flavor.value} ice cream in a {self.cone_type.value}"


class SundaeToppings(Enum):
    hot_fudge = 1.25
    strawberry_syrup = 0.75
    carmel_syrup = 0.50
    peanuts = 0.35
    coconut = 0.20

class Sundae(MenuItem):
    tax_rate = TaxRate.luxury
    ice_cream_scoops = 2

    def __init__(self):
        super().__init__(Sundae.ice_cream_scoops, IceCream.price, Sundae.tax_rate)
        self.toppings = []

    def get_total_and_tax(self):
        total = (Sundae.ice_cream_scoops * IceCream.price) + sum(topping.value for topping in self.toppings)
        tax = Sundae.tax_rate.value * total
        return round(total, 2), round(tax, 2)

    def add_topping(self, topping):
        self.toppings.append(topping)

    def __str__(self):
        toppings_display = [topping.name for topping in self.toppings]
        return f"Sundae with {', '.join(toppings_display)}"
