from unittest import TestCase
from money.money import Money

import MenuItems


class TestSundae(TestCase):
    def test_calculate_total_no_toppings(self):
        sundae = MenuItems.Sundae()
        self.assertEqual(Money('3.40'), sundae.calculate_total(), 'Sundae: calculate total: no toppings')

    def test_calculate_total_hot_fudge(self):
        sundae = MenuItems.Sundae()
        sundae.add_topping(MenuItems.Sundae.HotFudge)
        self.assertEqual(Money('4.65'), sundae.calculate_total(), 'Sundae: calculate total: hot fudge')

    def test_caculate_total_hot_fudge_peanuts(self):
        sundae = MenuItems.Sundae()
        sundae.add_topping(MenuItems.Sundae.HotFudge)
        sundae.add_topping(MenuItems.Sundae.Peanuts)
        self.assertEqual(Money('5.00'), sundae.calculate_total(), 'Sundae: calculate total: hot fudge')

    def test_calc_tax(self):
        sundae = MenuItems.Sundae()
        sundae.add_topping(MenuItems.Sundae.HotFudge)
        sundae.add_topping(MenuItems.Sundae.Peanuts)
        self.assertEqual(Money('0.35'), sundae.calculate_tax(), 'Sundae: calculate tax: hot fudge')


class TestIceCream(TestCase):
    def test_calculate_total_one_scoop(self):
        self.assertEqual(Money('1.70'), IceCream(1).calculate_total())

    def test_calculate_tax(self):
        self.fail()
