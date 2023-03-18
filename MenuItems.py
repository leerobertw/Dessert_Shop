from abc import ABC, abstractmethod
from money.money import Money

entertainment_tax_rate = 0.07
food_tax_rate = 0.0625

class MenuItem(ABC):

    @abstractmethod
    def calculate_total(self):
        pass

    @abstractmethod
    def calculate_tax(self):
        pass


class Candy(MenuItem):
    price_per_pound = Money('4.75')

    def __init__(self, weight):
        self.weight = weight

    def calculate_total(self):
        return Candy.price_per_pound * self.weight

    def calculate_tax(self):
        return self.calculate_total() * food_tax_rate


class Cookies(MenuItem):
    price_per_dozen = Money('6.25')

    def __init__(self, count):
        self.count = count

    def calculate_total(self):
        return Cookies.price_per_dozen * self.count

    def calculate_tax(self):
        return self.calculate_total() * food_tax_rate


class IceCream(MenuItem):
    price_per_scoop = Money('1.70')

    def __init__(self, scoops):
        self.scoops = scoops

    def calculate_total(self):
        return IceCream.price_per_scoop * self.scoops

    def calculate_tax(self):
        return self.calculate_total() * entertainment_tax_rate


class Sundae(MenuItem):
    class HotFudge:
        cost = Money('1.25')

    class StrawberrySyrup:
        cost = Money('0.75')

    class CarmelSyrup:
        cost = Money('0.50')

    class Peanuts:
        cost = Money('0.35')

    class Coconut:
        cost = Money('0.20')

    def __init__(self):
        self.ice_cream_cost = IceCream(2).calculate_total()
        self.toppings = []

    def calculate_total(self):
        total = self.ice_cream_cost
        for topping in self.toppings:
            total += topping.cost
        return total

    def calculate_tax(self):
        return self.calculate_total() * entertainment_tax_rate

    def add_topping(self, topping):
        self.toppings.append(topping)
