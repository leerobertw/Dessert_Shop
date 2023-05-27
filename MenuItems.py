from enum import Enum
from decimal import Decimal
from overrides import override

entertainment_tax_rate = '0.07'
food_tax_rate = '0.0625'

class MenuItem:
    def __init__(self, amount, price, tax_rate):
        self._amount = Decimal(amount)
        self.__price = Decimal(price)
        self.__tax_rate = Decimal(tax_rate)

    def calculate_total(self):
        return self.__price * self._amount

    def get_total_and_tax(self):
        total_cost = self.calculate_total()
        return total_cost, total_cost * self.__tax_rate


class Candy(MenuItem):
    price_per_pound = '4.75'

    def __init__(self, weight):
        super().__init__(weight, Candy.price_per_pound, food_tax_rate)

    def __str__(self):
        return f"{self._amount} lbs of candy"


class Cookies(MenuItem):
    price_per_dozen = '6.25'

    def __init__(self, count):
        super().__init__(count, Cookies.price_per_dozen, food_tax_rate)

    def __str__(self):
        return f"{self._amount} dozen cookies"


class IceCream(MenuItem):
    price_per_scoop = '1.70'

    def __init__(self, scoops):
        super().__init__(scoops, IceCream.price_per_scoop, entertainment_tax_rate)

    def __str__(self):
        return f"{self._amount} scoops of ice cream"


class SundaeToppings(Enum):
    Hot_Fudge = '1.25'
    Strawberry_Syrup = '0.75'
    Carmel_Syrup = '0.50'
    Peanuts = '0.35'
    Coconut = '0.20'

class Sundae(IceCream):
    def __init__(self):
        super().__init__(2)
        self.toppings = []

    @override
    def calculate_total(self):
        return super().calculate_total() + sum(Decimal(topping.value) for topping in self.toppings)

    def add_topping(self, topping):
        self.toppings.append(topping)

    def __str__(self):
        toppings_display = [topping.name for topping in self.toppings]
        return f"Sundae with {', '.join(toppings_display)}"
