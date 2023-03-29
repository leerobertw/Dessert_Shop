from unittest import TestCase
from money.money import Money

from MenuItems import Candy, Cookies, IceCream, Sundae


class TestSundae(TestCase):
    def test_calculate_total_no_toppings(self):
        sundae = Sundae()
        self.assertEqual(Money('3.40', 'USD'), sundae.calculate_total(), 'Sundae: calculate total: no toppings')

    def test_calculate_total_hot_fudge(self):
        sundae = Sundae()
        sundae.add_topping(Sundae.HotFudge)
        self.assertEqual(Money('4.65', 'USD'), sundae.calculate_total(), 'Sundae: calculate total: hot fudge')

    def test_calculate_total_hot_fudge_peanuts(self):
        sundae = Sundae()
        sundae.add_topping(Sundae.HotFudge)
        sundae.add_topping(Sundae.Peanuts)
        self.assertEqual(Money('5.00', 'USD'), sundae.calculate_total(), 'Sundae: calculate total: hot fudge, peanuts')

    def test_calc_total_double_hot_fudge_peanuts(self):
        sundae = Sundae()
        sundae.add_topping(Sundae.HotFudge)
        sundae.add_topping(Sundae.HotFudge)
        sundae.add_topping(Sundae.Peanuts)
        self.assertEqual(Money('6.25', 'USD'), sundae.calculate_total(), 'Sundae: calculate total: double hot fudge, peanuts')

    def test_calculate_total_strawberry_double_coconut(self):
        sundae = Sundae()
        sundae.add_topping(Sundae.StrawberrySyrup)
        sundae.add_topping(Sundae.Coconut)
        self.assertEqual(Money('4.35', 'USD'), sundae.calculate_total(), 'Sundae: calculate total: Strawberry Syrup, coconut')

    def test_calc_tax(self):
        sundae = Sundae()
        sundae.add_topping(Sundae.HotFudge)
        sundae.add_topping(Sundae.Peanuts)
        self.assertEqual(Money('0.35', 'USD'), sundae.calculate_tax(), 'Sundae: calculate tax: hot fudge, peanuts')


class TestIceCream(TestCase):
    def test_calculate_total_one_scoop(self):
        self.assertEqual(Money('1.70', 'USD'), IceCream(1).calculate_total(), 'Cal total, one scoop')

    def test_calculate_tax_one_scoop(self):
        self.assertEqual(Money('0.12', 'USD'), IceCream(1).calculate_tax(), 'Cal tax, one scoop')

class TestCandy(TestCase):
    def test_float_rounding(self):
        candy = Candy('0.354343')
        self.assertEqual(Money('1.68', 'USD'), candy.calculate_total())