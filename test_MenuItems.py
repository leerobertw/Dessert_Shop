from unittest import TestCase
from money.money import Money

from MenuItems import Candy, Cookies, IceCream, Sundae, SundaeToppings


class TestSundae(TestCase):
    def test_calculate_total_no_toppings(self):
        sundae = Sundae()
        self.assertEqual(Money('3.40'), sundae.calculate_total(), 'Sundae: calculate total: no toppings')

    def test_calculate_total_hot_fudge(self):
        sundae = Sundae()
        sundae.add_topping(SundaeToppings.Hot_Fudge)
        self.assertEqual(Money('4.65'), sundae.calculate_total(), 'Sundae: calculate total: hot fudge')

    def test_calculate_total_hot_fudge_peanuts(self):
        sundae = Sundae()
        sundae.add_topping(SundaeToppings.Hot_Fudge)
        sundae.add_topping(SundaeToppings.Peanuts)
        self.assertEqual(Money('5.00'), sundae.calculate_total(), 'Sundae: calculate total: hot fudge, peanuts')

    def test_calc_total_double_hot_fudge_peanuts(self):
        sundae = Sundae()
        sundae.add_topping(SundaeToppings.Hot_Fudge)
        sundae.add_topping(SundaeToppings.Hot_Fudge)
        sundae.add_topping(SundaeToppings.Peanuts)
        self.assertEqual(Money('6.25'), sundae.calculate_total(), 'Sundae: calculate total: double hot fudge, peanuts')

    def test_calculate_total_strawberry_double_coconut(self):
        sundae = Sundae()
        sundae.add_topping(SundaeToppings.Strawberry_Syrup)
        sundae.add_topping(SundaeToppings.Coconut)
        self.assertEqual(Money('4.35'), sundae.calculate_total(), 'Sundae: calculate total: Strawberry Syrup, coconut')

    def test_calc_tax(self):
        sundae = Sundae()
        sundae.add_topping(SundaeToppings.Hot_Fudge)
        sundae.add_topping(SundaeToppings.Peanuts)
        self.assertEqual(Money('0.35'), sundae.calculate_tax(), 'Sundae: calculate tax: hot fudge, peanuts')

    def test_str(self):
        sundae = Sundae()
        sundae.add_topping(SundaeToppings.Hot_Fudge)
        sundae.add_topping(SundaeToppings.Carmel_Syrup)
        sundae.add_topping(SundaeToppings.Peanuts)
        self.assertEqual('Sundae with Hot_Fudge, Carmel_Syrup, Peanuts', str(sundae))

class TestIceCream(TestCase):
    def test_calculate_total_one_scoop(self):
        self.assertEqual(Money('1.70'), IceCream(1).calculate_total(), 'Cal total, one scoop')

    def test_calculate_tax_one_scoop(self):
        self.assertEqual(Money('0.12'), IceCream(1).calculate_tax(), 'Cal tax, one scoop')
